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
import pyarabic.araby as araby
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


    def find_tri_verb(self, word, given_future_type):
        """
        lookup for tri verb from database
        """
        verb_list = libqutrub.verb_db.find_triliteral_verb(self.db_path, 
                word,    given_future_type)        
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

        future_form = mosaref.get_future_form(word, future_type)
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
            elif verb_nm[2] == araby.ALEF:
                features["علة"] = "ناقص واوي"
            elif verb_nm[2] == araby.ALEF_MAKSURA:
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
                
    def suggest_verb_list(self, text, options):
        """
        Suggest a list of verbs if error or multiple entries
        """

        suggestions = []
        word = text.split(" ")[0]
        given_future_type = options.get("future_mark",u"فتحة")    
        valid = is_valid_infinitive_verb(word)
        db_base_path = self.db_path
        if valid:

            suggestions = self.find_tri_verb(word, given_future_type)
        else:
            sug_verb_list  =  list(set(suggest_verb(word)))
            suggestions = []
            for sug in sug_verb_list:
                suggestions.extend(self.find_tri_verb(sug, given_future_type))
            # ~ suggestions = list(set(suggestions)) 
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
            print("suggest_verb_list",suggestions)
            return suggestions;
        else:
            return []        
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
