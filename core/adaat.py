#!/usr/bin/python
# -*- coding=UTF-8 -*-
#------------------------------------------------------------------------
# Name:        adaat
# Purpose:    interface between library and the web interface for Adawat 
#
# Author:      Taha Zerrouki (taha.zerrouki[at]gmail.com)
#
# Created:     31-10-2011
# Copyright:   (c) Taha Zerrouki 2011
# Licence:     GPL
#-----------------------------------------------------------------------
"""
Adaat, arabic tools interface
"""
import sys,os
sys.path.append(os.path.join(os.path.dirname(__file__), '../support/'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../config/'))
import random
import pyarabic.araby  as araby # arabic words general functions
import re

import qutrub_config
#~import pyarabic.number
def DoAction(text, action, options = {}):
    """
    do action by name
    """
    if action == "DoNothing":
        return text
    elif action == "Conjugate":
        return conjugate(text, options)        
    elif action == "Suggest":
        return suggest_verb_list(text, options)        
    if action == "Contibute":
        return text
    else:
        return text


def conjugate(text, options):
    """
    Conjugate verb using qutrub
    
    """

    #extract first word if many words are given
    word = text.split(" ")[0]
    given_future_type = options.get("future_type",u"فتحة") 
    # find future haraka for a given verb
    import libqutrub.verb_db
    db_base_path = "."
    verb_list = libqutrub.verb_db.find_triliteral_verb(db_base_path, word, 
        given_future_type)
    # ~ print(verb_list)
    # get vocalized form of the verb
    if(verb_list):
        word = verb_list[0].get("verb",word)
        future_type = verb_list[0].get("haraka",word)
    else:
        future_type = given_future_type
    conjugate_result =  do_sarf(word, 
        future_type = future_type,
        all         = options.get("all", False),
        past        = options.get("past", False),
        future      = options.get("future", False),
        passive     = options.get("passive", False),
        imperative  = options.get("imperative", False),
        future_moode= options.get("future_moode", False),
        confirmed   = options.get("confirmed", False),
        transitive  = options.get("transitive", False),
        #~ display_format  =options.get("imperative", "HTML"),
        );
        
    conjugate_result_table = conjugate_result.get("table",{})
    conjugate_result_suggest = conjugate_result.get("suggest",{})
    conjugate_result_verb_info= format_verb_info(conjugate_result.get("verb_info",""), bool(verb_list))

    return {"table":conjugate_result_table,
    "suggest":conjugate_result_suggest,
    "verb_info":conjugate_result_verb_info}

def do_sarf(word,future_type,all=True,past=False,future=False,passive=False,imperative=False,future_moode=False,confirmed=False,transitive=False,display_format="HTML"):
    import libqutrub.mosaref_main as mosaref
    import libqutrub.ar_verb as ar_verb
    import libqutrub.classverb as verbclass
    import libqutrub.verb_const as verb_const
    import pyarabic.arabrepr as myrepr
    from libqutrub.verb_valid import is_valid_infinitive_verb, suggest_verb
    valid = is_valid_infinitive_verb(word)
    listetenses=[];
    if valid:
        future_type= ar_verb.get_future_type_by_name(future_type);
        bab_sarf=0;
        vb = verbclass.VerbClass(word,transitive,future_type);
        #vb.verb_class();
        vb.set_display(display_format);
    #test the uniformate function
        if all :
            if transitive :
##                  print("transitive")
                listetenses= verb_const.TABLE_TENSE
                result= vb.conjugate_all_tenses();
            else:
##                  print("intransitive");
                listetenses = verb_const.TableIndicativeTense;
##                  print(len(TableIndicativeTense))
                result= vb.conjugate_all_tenses(listetenses);
        else :
            listetenses=[];
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
            result =vb.conjugate_all_tenses(listetenses);
            #self.result["HTML"]=vb.conj_display.display("HTML",listetenses)
        #return result;
        # ~ print("Display text:", vb.conj_display.text)
        conjs_table = vb.conj_display.display("TABLE",listetenses)
        verb_info= get_verb_info(word,future_type,  transitive )
        # ~ return {"table":conjs_table,"suggest":[], "verb_info":repr(vb.conj_display.text)}
        return {"table":conjs_table,"suggest":[], "verb_info":verb_info}
        
    else:
        suggestions  =  suggest_verb(word)
        if suggestions:
            print("do-sarf",suggestions)
            return {"table":[], "verb_info":"","suggest":suggestions};
        else:
            return {"table":[], "verb_info":"","suggest":[]}
            
def suggest_verb_list(text, options):
    """
    Suggest a list of verbs if error or multiple entries
    """
    from libqutrub.verb_valid import is_valid_infinitive_verb, suggest_verb
    import libqutrub.verb_db
    import libqutrub.mosaref_main as mosaref
    suggestions = []
    word = text.split(" ")[0]
    given_future_type = options.get("future_mark",u"فتحة")    
    valid = is_valid_infinitive_verb(word)
    db_base_path = qutrub_config.db_base_path
    if valid:

        suggestions = libqutrub.verb_db.find_triliteral_verb(db_base_path, word, 
            given_future_type)
    else:
        sug_verb_list  =  list(set(suggest_verb(word)))
        suggestions = []
        for sug in sug_verb_list:
            suggestions.extend(libqutrub.verb_db.find_triliteral_verb(db_base_path, sug, 
            given_future_type))
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

def random_text():
    """
    get random text for tests
    """    
    from . import randtext
    
    return random.choice(randtext.textlist)

tab_type = {0: '', 1: '', 2: '', 
3: 'فعل ثلاثي', 
4: 'فعل رباعي', 
5: 'فعل خماسي', 
6: 'فعل سداسي', 
7: 'فعل سباعي', 
8: 'فعل ثماني', 
9: 'فعل تساعي'}

def get_verb_info(word, future_type="فتحة", transitive=True):
    """
    This function extract verb feaures:
    * length: 3,4,5,6 
    * weakness: weak, well
    * safety: hamza, shadda
    * kind of weakness: waw, yeh
    * category of weakness
    """
    import libqutrub.mosaref_main as mosaref
    future_form = mosaref.get_future_form(word, future_type)
    # strip haraka and keep shadda
    verb_nm = araby.strip_harakat(word)
    features = {"الفعل":word, "مضارعه": future_form}
    # length
    vlength = len(verb_nm)
    features["طول"]= tab_type.get(vlength, "")
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

def format_verb_info(features, exist_in_database=False):
    """
    Display verb info in proper way
    """
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
