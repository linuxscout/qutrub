#!/usr/bin/python
# -*- coding=utf-8 -*-

#************************************************************************
# $Id: classnoun.py, v 0.1 2016/04/01 12:14:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  The Main class to do the Noun derivation 
#
# -----------------
# Revision Details:    (Updated by Revision Control System)
# -----------------
#  $Date: 2016/04/01 12:14:00 $
#  $Author: Taha Zerrouki $
#  $Revision: 0.1 $
#  $Source: qutrub.sourceforge.net
#
#***********************************************************************/
"""
Noun Class for derivation
@author: Taha Zerrouki
@contact: taha dot zerrouki at gmail dot com
@copyright: Arabtechies, Arabeyes, Taha Zerrouki
@license: GPL
@date:2016/04/01
@version: 0.1
"""
import pyarabic.araby as araby
from pyarabic.araby import FATHA, DAMMA, KASRA, SHADDA, SUKUN, HAMZA, ALEF, \
 NOON,  YEH_HAMZA, WAW, TATWEEL, MEEM, MEEM, YEH, TEH, ALEF_MAKSURA, DAMMATAN
import libqutrub.classverb as classverb
import  libqutrub.verb_const as vconst
import libqutrub.ar_verb as ar_verb 

#~ class ConjugStem:
# Noun derivation 
class NounClass(classverb.VerbClass):
    """
    Noun Class: represent a derived noun from a verb or a root
    """
    def __init__(self, verb, transitive, future_type=FATHA):
        """ 
        init method
        @param verb: the given verb
        @type verb: unicode.
        @param transitive: the verb is transitive or not
        @type transitive: Boolean.        
        @param future_type: The mark of the third radical letter in the verb, 
        used for triletiral verb only. Default value is Fatha; 
        @type future_type: unicode; one arabic letter (Fatha, Damma, Kasra).        
        """    
        # we make transitive as True, to force the cverb conjugator
        # to generate passive voices
        classverb.VerbClass.__init__(self, verb, True, future_type)
        self._prepare_subject_stem()
        self._prepare_object_stem()


#####################################
#{ Attributes functions
#####################################
#####################################
#{ Extract information from verb functions
#####################################

    def _prepare_subject_stem(self):
        """
        Prepare the derivation stems 
         Those stems will be concatenated with conjugation affixes.
          This function store results in self.tab_conjug_stem. 
          This function prepare conjugation stems for the following nouns type:
          - اسم الفاعل
        """
        #~ """
        #~ اسم الفاعل /تعريفـه :
#~ اسم مشتق من الفعل المبني للمعلوم للدلالة على وصف من فعل الفعل على وجه الحدوث .
#~ مثل : كتب – كاتب ، جلس – جالس ، اجتهد – مُجتهد ، استمع – مُستمع .
#~ صوغه : يصاغ اسم الفاعل على النحو التالي :
#~ 1 ـ من الفعل الثلاثي على وزن فاعل :
#~ نحو : ضرب - ضارب ، وقف - واقف ، أخذ - آخذ ، قال - قائل ، بغى - باغ ، أتى - آت ، رمى - رام ، وقى - واق .
#~ فإن كان الفعل معتل الوسط بالألف " أجوف " تقلب ألفه همزة مثل : قال – قائل ، نام – نائم .
#~ ومنه قوله تعالى : { وفي أموالهم حق للسائل والمحروم } 19 الذاريات .
#~ أما إذا كان معتل الوسط بالواو أو بالياء فلا تتغير عينه في اسم الفاعل .
#~ مثل : حول – حاول ، حيد – حايد .
#~ وإن كان الفعل معتل الآخر " ناقصاً " فإن اسم الفاعل ينطبق عليه ما ينطبق على الاسم المنقوص . أي تحذف ياؤه الأخيرة في حالتي الرفع والجر ، وتبقى في حالة النصب .
#~ 2 ـ من الفعل المزيد :
#~ يصاغ اسم الفاعل من الفعل غير الثلاثي " المزيد " على وزن الفعل المضارع مع إبدال حرف المضارعة ميماً مضمومة وكسر ما قبل الآخر .
#~ مثل : طمأن – مُطمئِن ، انكسر - مُنكسِر ، استعمل – مُستعمِل .
#~ – الفعل المزيد الخماسي على وزن تفاعل هو ما تكون عينه مفتوحة في المضارع، لكنها تكون مكسورة في اسم الفاعل
#~ 
#~ 
#~ الخوارزمية:
#~ 1- إن كان ثلاثيا:
    #~ - إن كان  أجوفا، نغير حرفه الأوسط إلى همزة، 
#~ - نشتقه على وزن فاعل
#~ 2- إن كان غير ثلاثي
    #~ - إن كان خماسيا مبدوءا بتاء نأخذ مضارعه ونكسر ما قبل آخره
    #~ - وإلا نأخذ مضارعه كما هو
    #~ """
    #~ 
        letters = self.word_letters
        marks = self.word_marks
        # حركات مشتق اسم الفاعل
        derivation_subject_marks = marks
        derivation_subject_letters = letters
        # حالة الفعل الثلاثي
        if self.vlength == 3:
            # الفعل الأجوف ممثل بحرفين باعتبار أنّ الألف هو حركة طويلة
            # لذا نضع وسطه همزة
            if len(letters) == 2:
                # اسم الفاعل
                derivation_subject_letters = letters[0] + HAMZA + letters[1]
            elif letters.endswith(ALEF_MAKSURA) or letters.endswith(vconst.ALEF_MAMDUDA):
                derivation_subject_letters = letters[0] + letters[1] + YEH


            # اسم افاعل من الثلاثي جميعا
            # حركاته
            derivation_subject_marks = vconst.ALEF_HARAKA + KASRA + DAMMA 

        # الفعل غير الثلاثي
        else:
        # الفعل الخماسي المبدوء بتاء
        # هذا مضارعه عينه مفتوحة
        # لذا نحتاج إلى عين مكسورة
            if self.vlength == 5 and letters.startswith(TEH):
                #~ if len(letters) == 4: # تفاعل 
                    #~ # الألف تعتبر مدة وليست حرفا 
                    #~ # لذا يظهر الاختلاف بين طول الطلمة وعدد الحروف الفعلي
                    #~ # الفعل الخماسي المبدوء بتاء يختلف في حركة عين اسم الفاعل عن مضارعه
                    #~ derivation_subject_marks = FATHA + vconst.ALEF_HARAKA + KASRA + DAMMA                    
                #~ else:
                    #~ # الفعل الخماسي المبدوء بتاء يختلف في حركة عين اسم الفاعل عن مضارعه
                    #~ derivation_subject_marks = FATHA + FATHA + SUKUN + KASRA + DAMMA
                derivation_subject_marks = FATHA + FATHA + SUKUN + KASRA + DAMMA

                # add Damma for MEEM
                #~ derivation_subject_marks = DAMMA + derivation_subject_marks
            else :
                # الفعل غير الثلاثي يصاغ على منوال مضارعه
                derivation_subject_marks = self.tab_conjug_stem[vconst.TenseFuture].marks
                #~ if derivation_subject_marks.startswith(FATHA):
                   #~ derivation_subject_marks = DAMMA + derivation_subject_marks[1:] 
                #~ derivation_subject_marks = DAMMA + derivation_subject_marks 
                derivation_subject_letters = self.tab_conjug_stem[vconst.TenseFuture].letters

    # معالجة الألفات في الفعل والحركات الطويلة
        #  إذا كان طول الحركات ألأصلية للفعل 
        # أقل من طول حركات الماضي المبني للمجهول
        # هذا يعني وجود حركة طويلة
        # نقوم بتحويل الحركة الطويلة إلى ما يوافقها
        if len(marks) < len(derivation_subject_marks):
            derivation_subject_marks = self._homogenize_harakat(marks, derivation_subject_marks)
        # Add Meem Haraka
        if self.vlength != 3:
            if self.vlength == 5 and letters.startswith(TEH):
                # add Damma for MEEM
                derivation_subject_marks = DAMMA + derivation_subject_marks
            else :
                # الفعل غير الثلاثي يصاغ على منوال مضارعه
                if derivation_subject_marks.startswith(FATHA):
                   derivation_subject_marks = DAMMA + derivation_subject_marks[1:] 
        ### اشتقاق اسم الفاعل 
        self.tab_conjug_stem[vconst.SubjectNoun] = classverb.ConjugStem(
        vconst.SubjectNoun, derivation_subject_letters, derivation_subject_marks)

    def _prepare_object_stem(self):
        """
        Prepare the derivation stems 
         Those stems will be concatenated with conjugation affixes.
          This function store results in self.tab_conjug_stem. 
          This function prepare conjugation stems for the following nouns type:
          - اسم المفعول
          
        """
        letters = self.word_letters
        marks = self.word_marks
        # حركات مشتق اسم المفعول
        derivation_object_marks = marks
        derivation_object_letters = letters
        # حالة الفعل الثلاثي
    #~ """
    #~ اسم المفعول تعريفـه :
#~ اسم يشتق من الفعل المبني للمجهول للدلالة على وصف من يقع عليه الفعل .
#~ مثل : ضُرب مضروب ، أُكل مأكول ، شُرب مشروب ، بُث مبثوث ، وُعد موعود ، أُتى مأتي ، رُجي مرجي ، مُلئ مملوء .
#~ صوغـه :
#~ لا يصاغ إلا من الأفعال المتعدية المتصرفة على النحو التالي :
#~ 1 ـ من الثلاثي على وزن مفعول .
#~ كما في الأمثلة السابقة . ومنه : الحق صوته مسموع .
#~ والشاي مشروب لذيذ الطعم .
#~ فإن كان الفعل معتل الوسط بالألف فإنه يحدث فيه إعلال تقتضيه القواعد الصرفية ، فيكون اسم المفعول من الفعل قال : مقول ، وباع : مبيع .
#~ ومما سبق يتبع في أخذ اسم المفعول من الأفعال المعتلة الوسط الآتي :
#~ نأخذ الفعل المضارع من الفعل المراد اشتقاق اسم المفعول منه ثم نحذف حرف المضارعة ونستبدلها بالميم .
#~ مثل : قال يقول مقول ، باع يبيع مبيع .
#~ فإن كان وسط المضارع ألفاً ترد في اسم المفعول إلى أصلها الواو أو الياء .
#~ مثل : خاف يخاف مخوف ، فالألف أصلها الواو لأن مصدرها " الخوف " .
#~ وهاب يهاب مهيب ، فالألف أصلها الياء لأن مصدرها " الهيبة " .
#~ وإن كان الفعل معتل الآخر " ناقصاً " نأتي بالمضارع منه ثم نحذف حرف المضارعة ونضع مكانها ميماً مفتوحة ونضعف الحرف الأخير الذي هو حرف العلة سواء أكان أصله واواً أو ياءً أو ألفاً .
#~ مثل : دعا يدعو مدعوّ ، رجا يرجو مرجوّ ، رمى يرمي مرميّ ، سعى يسعى مسعيّ .
#~ 2 ـ ويصاغ من غير الثلاثي " المزيد " على وزن الفعل المضارع مع إبدال حرف المضارعة ميماً مضمومة وفتح ما قبل الآخر .
#~ مثل : أنزل ينزل مُنزَل ، انطلق ينطلق مُنطلَق ، انحاز ينحاز مُنحاز ، استعمل يستعمل مُستعمَل .
#~ ـ إذا كان الفعل لازماً يصح اشتقاق اسم المفعول منه حسب القواعد السابقة بشرط استعمال شبه الجملة " الجار والمجرور أو الظرف " مع الفعل ، وقد يصح المصدر أيضاً .
#~ مثال : ذهب به – مذهوب به ، سافر يوم الخميس – ما مُسافَرٌ يوم الخميس .
#~ ومثال استعمال المصدر مع اسم مفعول الفعل اللازم : العلم مُنتفَع انتفاع عظيم به .
#~ 
#~ 1- إن كان  ثلاثيا
        #~ - غير معتل: على وزن مفعول
#~ - معتل : 1- فعل مثال => كغير المعتل
               #~ 2- الأجوف : من مضارعه      يقول => مقول
                    #~ يسير => مسير
                    #~ يخاف => مخوف
                    #~ يهاب => يهيب
    #~ 3- الناقص : من مضارعه مع تضعيف الحرف الأخير
#~ 2- غير ثلاثي
    #~ - على غرار المضارع المبني للمجهول
#~ ل
    #~ """
        if self.vlength == 3:
            # اسم المفعول
            # حالة المعتل
            # الأجوف
            if len(letters) == 2:            
                # اسم المفعول من الأجوف
                # يشتق من المضارع المعلوم
                derivation_object_marks = self.tab_conjug_stem[vconst.TenseFuture].marks
                derivation_object_letters = self.tab_conjug_stem[vconst.TenseFuture].letters

            elif (self.word_letters.endswith(ALEF_MAKSURA) or
             self.word_letters.endswith(ALEF) or self.word_letters.endswith(YEH)):            
                # والناقص
                # يشتق من المضارع المعلوم
                # يضاف إليه شدة في آخره 
                derivation_object_marks = self.tab_conjug_stem[vconst.TenseFuture].marks
                derivation_object_letters = self.tab_conjug_stem[vconst.TenseFuture].letters
            else: # السالم والمضعف والمثال
                if self.word_letters.endswith(SHADDA):
                    # strip last letters which is Shadda, duplicate the second letters
                    derivation_object_letters =  letters[0]+ letters[1]*2
                else:
                    derivation_object_letters =  letters
                # الحروف
                derivation_object_marks  = FATHA + SUKUN + vconst.WAW_HARAKA + DAMMA 
        # الفعل غير الثلاثي
        else:
            # اسم المفعول من غير الثلاثي
            derivation_object_marks = self.tab_conjug_stem[vconst.TensePassiveFuture].marks
            derivation_object_letters = self.tab_conjug_stem[vconst.TensePassiveFuture].letters

    # معالجة الألفات في الفعل والحركات الطويلة
        #  إذا كان طول الحركات ألأصلية للفعل 
        # أقل من طول حركات الماضي المبني للمجهول
        # هذا يعني وجود حركة طويلة
        # نقوم بتحويل الحركة الطويلة إلى ما يوافقها
        #~ if len(marks) < len(derivation_object_marks):
            #~ derivation_object_marks = self._homogenize_harakat(marks, 
                     #~ derivation_object_marks)
        ### اشتقاق اسم الفاعل والمفعول
        self.tab_conjug_stem[vconst.ObjectNoun] = classverb.ConjugStem(
        vconst.ObjectNoun, derivation_object_letters, derivation_object_marks)

    def conjugate_noun(self, noun_type):
        """
        Conjugate a verb in a given tense with a pronoun.
        @param tense: given tense
        @type tense: unicode name of the tense
        @param pronoun: given pronoun
        @type pronoun: unicode name of the pronoun
        @return: conjugated verb
        @rtype: unicode;        
        """

        if noun_type == vconst.SubjectNoun :
            if self.vlength == 3 :            
                #prefix
                pre_val = u""
            else:
                pre_val = MEEM                
            #suffix
            suf_val = DAMMA           
        elif noun_type == vconst.ObjectNoun:
            #prefix
            pre_val = MEEM 
            #suffix
            suf_val = DAMMA 
        else:
            #prefix
            pre_val = "" 
            #suffix
            suf_val = ""
            
        stem_l = self.tab_conjug_stem[noun_type].letters
        stem_m = self.tab_conjug_stem[noun_type].marks
        # _m : marks
        #_l :letters
        if pre_val != u"":
            pre_val_l = pre_val
            pre_val_m = stem_m[0]
            stem_m = stem_m[1:]
        else:
            pre_val_l = u""
            pre_val_m = u""

        # the suffix already start by a HARAKA, 
        # we add Taweel to ensure valid word in the uniformate function
        suf_val = TATWEEL + suf_val
        #uniformate suffix
        # the case is used to avoid duplicated staddization
        if self.cache_standard['suffix'].has_key( suf_val): 
            (suf_val_l, suf_val_m) = self.cache_standard['suffix'][suf_val]
        else:
            (suf_val_l, suf_val_m) = ar_verb.uniformate_suffix(suf_val)
            self.cache_standard['suffix'][suf_val] = (suf_val_l, suf_val_m)
        # add affix to the stem
        conj_l = pre_val_l + stem_l + suf_val_l
        #The end of the stem marks takes the begining of the suffix marks
        conj_m = pre_val_m + stem_m[:-1] + suf_val_m
        # the begining of suffix letters is Tatweel, it will be striped
        conj_l = pre_val_l + stem_l + suf_val_l[1:]

        # Treat sukun
        # the case is used to avoid duplicated staddization
        key_cache = u'-'.join([conj_l, conj_m])
        if self.cache_standard['sukun'].has_key(key_cache):
            conj_m = self.cache_standard['sukun'][key_cache]
        else:
            #~ conj_m = ar_verb.treat_sukun2(conj_l, conj_m, self.future_type)
            conj_m = ar_verb.treat_sukun2(conj_l, conj_m)
            self.cache_standard['sukun'][key_cache] = conj_m
        # standard orthographic form
        # the case is used to avoid duplicated staddization
        key_cache = u'-'.join([conj_l, conj_m])
        if self.cache_standard['standard'].has_key(key_cache):
            conj = self.cache_standard['standard'][key_cache]
        else:    
            conj = ar_verb.standard2(conj_l, conj_m)
            self.cache_standard['standard'][key_cache] = conj
        return conj

    def derivate(self):
        """
        Derivate a subject and object nouns from a verb
        @param tense: given tense
        @type tense: unicode name of the tense
        @param pronoun: given pronoun
        @type pronoun: unicode name of the pronoun
        @return: conjugated verb
        @rtype: unicode;        
        """
        subj = self.conjugate_noun(vconst.SubjectNoun)
        obj  = self.conjugate_noun(vconst.ObjectNoun)

        if subj.endswith(araby.DAMMA):
            subj = subj[:-1]+araby.DAMMATAN
        if self.vlength == 3 and obj.endswith(araby.YEH):
            obj+= SHADDA + DAMMATAN 
        #~ if self.verb == u"مَحَا":
            #~ print self.verb.encode('utf8'), len(self.word_letters), obj.endswith(WAW*2+
             #~ DAMMA)
        if self.vlength == 3  and obj.endswith(WAW*2+DAMMA):
            obj = obj[:-2] +SHADDA + DAMMATAN                        
        if obj.endswith(araby.DAMMA):
            obj = obj[:-1]+araby.DAMMATAN
            
        return u"\t".join([subj,obj])
