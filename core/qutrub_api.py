#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  qutrub_api.py
#  
#  Copyright 2021 zerrouki <zerrouki@majd4>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#
import re
import sqlite3 as sqlite
import os
        
import pyarabic.araby as araby

VERB_STAMP_PAT = re.compile(u"[%s%s%s%s%s%s]"%(araby.ALEF, araby.YEH, araby.WAW,
        araby.ALEF_MAKSURA, araby.HAMZA, araby.SHADDA), re.UNICODE)

import libqutrub.conjugator
import libqutrub.classverb as verbclass
import libqutrub.verb_db
import libqutrub.ar_verb as ar_verb
import libqutrub.verb_const as verb_const
import libqutrub.mosaref_main as mosaref

from libqutrub.verb_valid import is_valid_infinitive_verb, suggest_verb
import logging
class QutrubApi:
    """
    a class as conjugator wraper
    """
    def __init__(self, db_path="."):
        """
        init qutrub api
        """
        self.db_path = db_path
        self.display_format = "HTML"
        
        self.tab_type = {0: '', 1: '', 2: '', 
            3: 'فعل ثلاثي', 
            4: 'فعل رباعي', 
            5: 'فعل خماسي', 
            6: 'فعل سداسي', 
            7: 'فعل سباعي', 
            8: 'فعل ثماني', 
            9: 'فعل تساعي'}
        self.my_verb_class = None
        self.listetenses = verb_const.TABLE_TENSE
        self.verb_stamp_pat = VERB_STAMP_PAT
    
    def set_db_path(self, db_path):
        """
        set the db path
        """
        self.db_path = db_path
        

    def set_display_format(self, display_format):
        """
        set the display_format
        """
        self.display_format = display_format


    def find_verb(self, word, given_future_type):
        """
        lookup for tri verb from database
        """
        # remove harakat keep shadda
        verb_nm = araby.strip_harakat(word)
        if len(verb_nm) == 3:
            verb_list = self.find_tri_verb(word,  given_future_type)
        else:
            verb_list = self.find_nontri_verb(word)            
            
        return verb_list
        
    def find_tri_verb(self, word, given_future_type):
        """
        lookup for tri verb from database
        """
        verb_list = libqutrub.verb_db.find_triliteral_verb(self.db_path, 
                word,    given_future_type)        
        return verb_list
        
    def find_nontri_verb(self, word):
        """
        lookup for non tri verb from database
        """
        verb_list = self.lookup_nontri_verb(word)
        return verb_list
        
    def is_valid_infinitive(self, verb):
        """
        check if the given verb is valid 
        """
        return is_valid_infinitive_verb(verb)
        
    def manage_tenses(self,all=True, past=False,future=False,passive=False,imperative=False,future_moode=False,confirmed=False,transitive=False):
        """
        manage tenses according to given parameters
        """
        listetenses=[];
        if all :
            if transitive :
                listetenses= verb_const.TABLE_TENSE
            else:
                listetenses = verb_const.TableIndicativeTense;
        else:
            if past : listetenses.append(verb_const.TensePast);
            if (past and passive and transitive) : listetenses.append(verb_const.TensePassivePast)
            if future : listetenses.append(verb_const.TenseFuture);
            if (future and passive and transitive) : listetenses.append(verb_const.TensePassiveFuture)
            if (future_moode) :
                listetenses.append(verb_const.TenseSubjunctiveFuture)
                listetenses.append(verb_const.TenseJussiveFuture)
            if (confirmed) :
                if (future):listetenses.append(verb_const.TenseConfirmedFuture);
                if (imperative):listetenses.append(verb_const.TenseConfirmedImperative);
            if (future and passive and transitive and confirmed) :
                listetenses.append(verb_const.TensePassiveConfirmedFuture);
            if (passive and transitive and future_moode) :
                listetenses.append(verb_const.TensePassiveSubjunctiveFuture)
                listetenses.append(verb_const.TensePassiveJussiveFuture)
            if imperative : listetenses.append(verb_const.TenseImperative)
        
        self.listetenses = listetenses ;
        
        return   listetenses 
    def conjugate_all_tenses(self, tenses= [] ):
        """ conjugate verb in input wwith tenses"""
        if not tenses:
            tenses = self.listetenses
        if not self.my_verb_class:
            return None
        result = self.my_verb_class.conjugate_all_tenses(tenses)
        
        return result;
              
    def  get_future_type_by_name(self, future_type):
        """
        translate future type by name
        """
        return ar_verb.get_future_type_by_name(future_type)

    def display(self):
        """
        """
        if not self.my_verb_class:
            return None        
        resulttext = self.my_verb_class.conj_display.display("TABLE",self.listetenses)
        return resulttext
        

    def get_verb_info(self, word, future_type="فتحة", transitive=True):
        """
        This function extract verb feaures:
        * length: 3,4,5,6 
        * weakness: weak, well
        * safety: hamza, shadda
        * kind of weakness: waw, yeh
        * category of weakness
        """
        try:
            future_form = mosaref.get_future_form(word, future_type)
        except:
            #print("qutrub_api: Error on future form ", word)
            future_form = word
        # strip haraka and keep shadda
        verb_nm = araby.strip_harakat(word)
        features = {"الفعل":word, "مضارعه": future_form}
        # length
        vlength = len(verb_nm)
        features["طول"]= self.tab_type.get(vlength, "")
        verb_normalized = araby.normalize_hamza(verb_nm)
        
        #التعدي
        if transitive :
            features["تعدي"] = "متعدي"
        else:
            features["تعدي"] = "لازم"        
        # سالم أو مهموز أو مضعف
        if araby.SHADDA in verb_nm and araby.HAMZA in verb_normalized:
            features["سالم"] = "مضعف مهموز"
        elif araby.SHADDA in  verb_nm:
            features["سالم"] = "مضعف"
        elif araby.HAMZA in verb_normalized:
            features["سالم"] = "مهموز"
        else:
            features["سالم"] = "" 
                
        # معتل
        features["علة"] = ""
        if vlength == 3:
            if verb_nm[0] == araby.WAW:
                # ~ if verb_nm[1] == araby.ALEF:
                    # ~ feature["علة"] = "لفيف مقرون"
                if verb_nm[2] in(araby.ALEF, araby.ALEF_MAKSURA, araby.YEH):
                    features["علة"] = "لفيف مفروق"
                else:
                    features["علة"] = "مثال واوي"
            elif verb_nm[1] == araby.WAW:
                if verb_nm[2] in(araby.ALEF_MAKSURA, araby.YEH):
                    features["علة"] = "لفيف مقرون"        
            elif verb_nm[1] == araby.ALEF:
                # ~ if verb_nm[2] in(araby.ALEF, araby.ALEF_MAKSURA, araby.YEH):
                    # ~ feature["علة"] = "لفيف مفروق"            
                if future_type == "ضمة":
                    features["علة"] = "أجوف واوي"
                elif future_type == "فتحة":
                    features["علة"] = "أجوف واوي"
                elif future_type == "كسرة":
                    features["علة"] = "أجوف يائي"
                else:
                    features["علة"] = "أجوف"
            elif verb_nm[2] == araby.ALEF or verb_nm[2] == araby.WAW:
                features["علة"] = "ناقص واوي"
            elif verb_nm[2] == araby.ALEF_MAKSURA or verb_nm[2] == araby.YEH:
                features["علة"] = "ناقص يائي"
            else:
                features["علة"] = "صحيح"
        else:
            if verb_nm[-2:-1] == araby.ALEF:
                features["علة"] = "أجوف"
            elif verb_nm[-1:] == araby.ALEF_MAKSURA:
                features["علة"] = "ناقص"
            else:
                features["علة"] = "صحيح"
        if not features["سالم"] and features["علة"] == "صحيح":
            features["سالم"]  = "سالم"
        return features
        
    def input(self,verb, future_type="فتحة", transitive= True):
        """
        prepare input
        """
        # ~ logging.debug("qutrub_api",future_type)
        self.my_verb_class = verbclass.VerbClass(verb, transitive, future_type);
        # init tenses list
        self.listetenses = verb_const.TABLE_TENSE
        
    def conjugate(word, future_type, alltense = True, past = False, future = False, 
passive = False, imperative = False, future_moode = False, confirmed = False,
 transitive = False):
        """
        conjugate verb
        """
        return conjugator.conjugate(word, future_type, 
            alltense, past, future, passive, imperative, future_moode, confirmed,
            transitive, 
            self.display_format,
            )
    def format_verb_info(self, features, exist_in_database=False):
        """
        Display verb info in proper way
        """
        if type(features) != dict:
            if type(features) != str:
                return features
            else:
                return ""
        text = """"الفعل 
        {verb} - {future_form} {length} {trans} {weak} {salim}""".format(
        verb=features.get("الفعل", ""),
        future_form =  features.get("مضارعه", ""),
        length=  features.get("طول", ""),
        trans =  features.get("تعدي", ""),
        weak =  features.get("علة", ""),
        salim =  features.get("سالم", ""),
        )
        if exist_in_database:
            text += " [في قاعدة البيانات]"
        return text
    def suggest_verb(self, word):
        """
        generate suggestion for incorrect verbs
        """
        return suggest_verb(word)
                
    def suggest_similar_verb_list(self, word, given_future_type):
        """
        Suggest a list of verbs if error or multiple entries
        """

        suggestions = []
  
        valid = is_valid_infinitive_verb(word)
        if valid:
            suggestions = self.find_tri_verb(word, given_future_type)
            suggestions.extend(self.find_nontri_verb(word))            
        else:
            sug_verb_list  =  list(set(suggest_verb(word)))
            suggestions = []
            logging.debug(repr(sug_verb_list))
            for sug in sug_verb_list:
                suggestions.extend(self.find_tri_verb(sug, given_future_type))
                suggestions.extend(self.find_nontri_verb(sug))
        # make suggestion unique
        list_of_data_uniq = []
        for data in suggestions:
            if data not in list_of_data_uniq:
                list_of_data_uniq.append(data)
        suggestions =  list_of_data_uniq
        # add future form
        for sug in suggestions:
            sug["future"] = mosaref.get_future_form(sug.get("verb", ""), sug.get("haraka", ""))
        if suggestions:
            # ~ print("suggest_verb_list",suggestions)
            return suggestions;
        else:
            return []   
    def verb_stamp(self, word):
        """
        generate a stamp for a verb,
        the verb stamp is different of word stamp, by hamza normalization
        remove all letters which can change form in the word :
            - ALEF,
            - YEH,
            - WAW,
            - ALEF_MAKSURA
            - SHADDA
        @return: stamped word
        """
        word = araby.strip_tashkeel(word)
        #The vowels are striped in stamp function
        word = araby.normalize_hamza(word)
        if word.startswith(araby.HAMZA):
            #strip The first hamza
            word = word[1:]
        # strip the last letter if is doubled
        if word[-1:] == word[-2:-1]:
            word = word[:-1]
        return self.verb_stamp_pat.sub('', word)
        
    def lookup_nontri_verb(self, verb):
        """
        Find the triliteral verb in the dictionary, 
        return a list of possible verb forms
        @param db_base_path: the database path
        @type db_base_path: path string.
        @param triliteralverb: given verb.
        @type triliteralverb: unicode.
        @param givenharaka: given haraka of tuture type of the verb.
        @type givenharaka: unicode.
        @return: list of triliteral verbs.
        @rtype: list of unicode.
        """
        # ~ liste = [{"verb":"استعجل", 
                    # ~ "haraka":"فتحة", "transitive":True}]
        # ~ return liste
        liste = []
        db_path = os.path.join(self.db_path, "data/verbdict.db")
        logging.debug("QAPI;%s", db_path)
        try:
            logging.debug("verb_db2:"+ db_path)        
            conn  =  sqlite.connect(db_path)
            cursor  =  conn.cursor()
            # strip harakat and keep shadda
            verb_nm = araby.strip_harakat(verb)
            verb_stamp = self.verb_stamp(verb)
            # ~ tup = (verb_nm, )
            # ~ cursor.execute("""select verb, transitive 
                        # ~ from verbmore
                        # ~ where unvocalized = ?""", tup)
            tup = (verb_stamp, )
            cursor.execute("""select verb, unmarked, transitive 
                        from verbmore
                        where stamp = ?""", tup)
            for row in cursor:
                verb_vocalised = row[0]
                # strip harakat and keep shadda
                verb_unmarked = row[1] 
                haraka = "فتحة"
                transitive = row[2]
                # Return the transitivity option
                #MEEM is transitive
                # KAF is commun ( transitive and intransitive)
                # LAM is intransitive
                if transitive in (araby.KAF, araby.MEEM):
                    transitive = True
                else:
                    transitive = False
    # if the given verb is the list, 
    #it will be inserted in the top of the list, 
    #to be treated in prior
                if verb_nm == verb_unmarked:
                    liste.insert(0, {"verb":verb_vocalised, 
                    "haraka":haraka, "transitive":transitive})
    # else the verb is appended in the liste
                else:
                    liste.append({"verb":verb_vocalised, 
                    "haraka":haraka, "transitive":transitive})
            cursor.close()
            return liste
        except IOError:
            return None
    def verb_exists_in_database(self, verb, given_future_type="فتحة"):
        """
        Test if a given verb exists on database,
        """
        # The  function find_verb return a list of similar verbs
        verb_list = self.find_verb(verb, given_future_type)
        if not verb_list:
            return False
        else:
            # test if the exact verb is in database
            verb_nm = araby.strip_harakat(verb)
            verb_nm_list = [araby.strip_harakat(v.get("verb","")) for v in verb_list]
            # ~ verb_nm_list = [v.get("verb","") for v in verb_list]
            return (verb_nm in verb_nm_list)
        return False
                
        

    def main(args):
        return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
