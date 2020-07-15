#************************************************************************
# $Id: mosaref_main.py, v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
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
"""
Just a wraper for mosaref_main 
The main function to call qutrub conjugation from other programs.
"""
#
import libqutrub.mosaref_main
# rename the function
def conjugate(word, future_type, alltense = True, past = False, future = False, 
passive = False, imperative = False, future_moode = False, confirmed = False,
 transitive = False, display_format = "HTML"):
    """
    The main function to conjugate verbs.
    You must specify all parameters.
    Can be used as an example to call the conjugation class.
    @param word: the givern verb. the given word must be vocalized, 
    if it's 3 letters length only, else, the verb can be unvocalized, 
     but the Shadda must be given, it' considered as letter.
    @type word: unicode.
    @param future_type: For Triliteral verbs, 
    you must give the mark of Ain in the future, 
    كة عين الفعل في المضارع. it's given as a name of haraka (فتحة، ضمة، كسرة).
    @type future_type: unicode(فتحة، ضمة، كسرة).
    @param all: conjugate in all arabic tenses.
    @type all: Boolean, default(True)
    @param past: conjugate in past tense ألماضي
    @type past: Boolean, default(False)
    @param future: conjugate in arabic present and future tenses المضارع
    @type future: Boolean, default(False)
    @param passive: conjugate in passive voice  المبني للمجهول
    @type passive: Boolean, default(False)
    @param imperative: conjugate in imperative tense الأمر
    @type imperative: Boolean, default(False)
    @param future_moode: conjugate in future moode tenses المضارع المنصوب والمجزوم
    @type future_moode: Boolean, default(False)
    @param confirmed: conjugate in confirmed cases tense المؤكّد
    @type confirmed: Boolean, default(False)
    @param transitive: the verb transitivity التعدي واللزوم
    @type transitive: Boolean, default(False)
    @param display_format: Choose the display format:
        - 'Text':
        - 'HTML':
        - 'HTMLColoredDiacritics':
        - 'DICT':
        - 'CSV':
        - 'GUI':
        - 'TABLE':
        - 'XML':
        - 'TeX':
        - 'ROWS':
    @type display_format: string, default("HTML") 
    @return: The conjugation result
    @rtype: According to display_format.
    """
    return libqutrub.mosaref_main.do_sarf(word, future_type, alltense, past , future , 
passive , imperative , future_moode , confirmed ,
 transitive , display_format)
#~ conjugate = do_sarfco
