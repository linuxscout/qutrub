#************************************************************************
# $Id: mosaref_main.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  This file is used by the web interface to execute verb conjugation
#
# -----------------
# Revision Details:    (Updated by Revision Control System)
# -----------------
#  $Date: 2009/06/02 01:10:00 $
#  $Author: Taha Zerrouki $
#  $Revision: 0.7 $
#  $Source: arabtechies.sourceforge.net
#
#***********************************************************************/
import sys,re,string
import sys, os
from classverb import *


def get_future_form(verb_vocalised,haraka):

    word=verb_vocalised
    transitive=True;
    future_type=haraka
    if future_type not in (FATHA,DAMMA,KASRA):
        future_type=get_future_type_by_name(future_type);
    vb=verbclass(word,transitive,future_type);
    #vb.verb_class();
    return vb.conjugate_tense_pronoun(TenseFuture,PronounHuwa);

def do_sarf(word,future_type,all=True,past=False,future=False,passive=False,imperative=False,future_moode=False,confirmed=False,transitive=False,display_format="HTML"):
	valid=is_valid_infinitive_verb(word)
	if valid:
		future_type=get_future_type_by_name(future_type);
		bab_sarf=0;
		vb=verbclass(word,transitive,future_type);
##		vb.verb_class();
		vb.set_display(display_format);
	#test the uniformate function
		if all :
			if transitive :
				result= vb.conjugate_all_tenses();
			else:
				listetenses=TableIndicativeTense;
				result= vb.conjugate_all_tenses(listetenses);
		else :
			listetenses=[];
			if past : listetenses.append(TensePast);
			if (past and passive and transitive) : listetenses.append(TensePassivePast)
			if future : listetenses.append(TenseFuture);
			if (future and passive and transitive) : listetenses.append(TensePassiveFuture)
			if (future_moode) :
				listetenses.append(TenseSubjunctiveFuture)
				listetenses.append(TenseJussiveFuture)
			if (confirmed) :
				if (future):listetenses.append(TenseConfirmedFuture);
				if (imperative):listetenses.append(TenseConfirmedImperative);
			if (future and passive and transitive and confirmed) :
				listetenses.append(TensePassiveConfirmedFuture);
			if (passive and transitive and future_moode) :
				listetenses.append(TensePassiveSubjunctiveFuture)
				listetenses.append(TensePassiveJussiveFuture)
##			if (future and passive and transitive) : listetenses.append(TensePassiveFuture)
			if imperative : listetenses.append(TenseImperative)
			result =vb.conjugate_all_tenses(listetenses);
		return result;

	else: return None;




