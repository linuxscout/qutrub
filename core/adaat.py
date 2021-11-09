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
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
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
    from . import qutrub_api
    db_base_path = "."
    myconjugator = qutrub_api.QutrubApi(db_path = db_base_path)
    #extract first word if many words are given
    word = text.split(" ")[0]
    given_future_type = options.get("future_type",u"فتحة") 
    # find future haraka for a given verb
    import libqutrub.verb_db

    verb_list = myconjugator.find_tri_verb(word, given_future_type)
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
    conjugate_result_verb_info= myconjugator.format_verb_info(conjugate_result.get("verb_info",""), bool(verb_list))

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
    
    from . import qutrub_api
    db_base_path = "."
    myconjugator = qutrub_api.QutrubApi(db_path = db_base_path)
        
    valid = myconjugator.is_valid_infinitive(word)
    listetenses=[];
    if valid:
        future_type= myconjugator.get_future_type_by_name(future_type);
        bab_sarf=0;
        myconjugator.input(word,transitive,future_type);
        #vb.verb_class();
        myconjugator.set_display_format(display_format);
    #test the uniformate function
        listetenses= myconjugator.manage_tenses(all, past,future,passive,imperative,future_moode,confirmed,transitive)    
        # ~ if all :
            # ~ if transitive :
# ~ ##                  print("transitive")
                # ~ listetenses= verb_const.TABLE_TENSE
                # ~ result= vb.conjugate_all_tenses();
            # ~ else:
# ~ ##                  print("intransitive");
                # ~ listetenses = verb_const.TableIndicativeTense;
# ~ ##                  print(len(TableIndicativeTense))
                # ~ result= vb.conjugate_all_tenses(listetenses);
        # ~ else :
            # ~ listetenses= myconjugator.manage_tenses(past,future,passive,imperative,future_moode,confirmed,transitive)
            # ~ if past : listetenses.append(verb_const.TensePast);
            # ~ if (past and passive and transitive) : listetenses.append(verb_const.TensePassivePast)
            # ~ if future : listetenses.append(verb_const.TenseFuture);
            # ~ if (future and passive and transitive) : listetenses.append(verb_const.TensePassiveFuture)
            # ~ if (future_moode) :
                # ~ listetenses.append(verb_const.TenseSubjunctiveFuture)
                # ~ listetenses.append(verb_const.TenseJussiveFuture)
            # ~ if (confirmed) :
                # ~ if (future):listetenses.append(verb_const.TenseConfirmedFuture);
                # ~ if (imperative):listetenses.append(verb_const.TenseConfirmedImperative);
            # ~ if (future and passive and transitive and confirmed) :
                # ~ listetenses.append(verb_const.TensePassiveConfirmedFuture);
            # ~ if (passive and transitive and future_moode) :
                # ~ listetenses.append(verb_const.TensePassiveSubjunctiveFuture)
                # ~ listetenses.append(verb_const.TensePassiveJussiveFuture)
            # ~ if imperative : listetenses.append(verb_const.TenseImperative)
        result =  myconjugator.conjugate_all_tenses(listetenses);
            #self.result["HTML"]=vb.conj_display.display("HTML",listetenses)
        #return result;
        # ~ print("Display text:", vb.conj_display.text)
        conjs_table = myconjugator.display()
        verb_info= myconjugator.get_verb_info(word,future_type,  transitive )
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
    from . import qutrub_api
    db_base_path = "."
    myconjugator = qutrub_api.QutrubApi(db_path = db_base_path)
    return myconjugator.suggest_verb_list(text, options)
    


def random_text():
    """
    get random text for tests
    """    
    from . import randtext
    
    return random.choice(randtext.textlist)
