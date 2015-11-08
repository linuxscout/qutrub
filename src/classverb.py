#!/usr/bin/python
# -*- coding=utf-8 -*-

#************************************************************************
# $Id: dclassverb.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  The Main class to do the conjugation
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
import copy
from ar_ctype import *
from ar_verb import *
from verb_const import *
from conjugatedisplay import *
import sys,re,string

# بنية جذع تصريف الجذع
#تتكون من الزمن، الحروف والحركات
# تستعمل لتخزين جذوع التصريف
class conjug_stem:
	tense=u"";
	letters=u"";
	marks=u"";
	def __init__(self,tense,letters,marks):
		self.tense=tense;
		self.letters=letters;
		self.marks=marks;

class verbclass :
	verb=u"";
#" internl verb : is the normalized form of the verb"
	internal_verb=u"";
	word_letters=u"";
	word_marks=u"";
	unvocalized=u"";
	vlength=0;
	vtype=u"";
	future_type=u'';
	transitive=u"";
	hamza_zaida=False;
	teh_zaida=False;
	future_form=u"";
	conj_display=None;
	tab_conjug_stem=None;

#---------------------------------------------------------------------------
	def __init__(self,verb,transitive, future_type=FATHA):
		self.verb=verb;
		self.internal_verb=normalize(verb);
		self.future_type=future_type;
		(self.word_letters,self.word_marks)=uniformate_verb(verb);
        #Before last haraka in the past
		self.past_haraka=ar_before_last_letter(self.word_marks);
		self.word_marks=uniformate_alef_origin(self.word_marks,self.internal_verb,self.future_type);

		self.transitive=transitive;
		self.hamza_zaida=False;
		self.teh_zaida=False;
		# display object
		self.conj_display=conjugatedisplay(self.verb);
		if self.transitive  :
		    self.conj_display.add_attribut(u"اللزوم/التعدي",u"متعدي");
		else :
		    self.conj_display.add_attribut(u"اللزوم/التعدي",u"لازم");

##		self.conj_display.add_attribut(u"الكتابة الداخلية للفعل",self.word_letters+" - "+self.word_marks);
		self.tab_conjug_stem={};
		verb=self.verb;
##		root=self.root;
		tab_type=[u"",u"",u"",u"فعل ثلاثي",u"فعل رباعي",u"فعل خماسي",u"فعل سداسي",u"فعل سباعي",u"فعل ثماني",u"فعل تساعي"];
		verb=normalize(verb);

		self.unvocalized=ar_strip_marks_keepshadda(verb);
		verb_nm=self.unvocalized;
		self.vlength=len(verb_nm);
		self.vtype=tab_type[self.vlength];
		self.conj_display.add_attribut(u"الفعل",self.verb);
		self.conj_display.add_attribut(u"نوع الفعل",self.vtype);#+str(self.vlength));

        # الهمزة زائدة
		self.hamza_zaida=is_hamza_zaida(verb_nm);
##		if self.hamza_zaida:
##			self.conj_display.add_attribut(u"خاصية",u"همزة زائدة");

        # التاء الزائدة
		self.teh_zaida=is_teh_zaida(verb_nm);
##		if self.teh_zaida:
##			self.conj_display.add_attribut(u"خاصية",u"تاء زائدة");
        # معالجة حالة الإعال الشاذة
        # إذا كان الفعل من الشواذ، استخرجنا جذوع التصريف من جدوله
        #وإلا ولّدنا جذوع تصريفه
        # في المضارع والأمر فقط
        # أما الماضي فليس فيه شذوذ
		self.prepare_past_stem();
		self.prepare_passive_past_stem();
		if self.is_irregular_verb():
		    self.prepare_irregular_future_and_imperative_stem();

		else:
		    self.prepare_future_and_imperative_stem();
		self.future_form=self.conjugate_tense_pronoun(TenseFuture,PronounHuwa);
		self.conj_display.set_future_form(self.future_form);
		if self.transitive : self.conj_display.settransitive();
		self.conj_display.setbab(self.future_type);


#-------------------------------------------------------------------------------------
	def set_display(self,mode='Text'):
		self.conj_display.setmode(mode)
#-------------------------------------------------------------------------------------
	def get_conj_display(self):
		return copy.copy(self.conj_display)

# التصريف
# التصريف في المضارع المعلوم
#---------------------------------------------------------------------------
	def prepare_future_and_imperative_stem(self):
		letters=self.word_letters;
		marks=self.word_marks;
		future_letters=letters;
        # حالة الفعل الثلاثي
		if self.vlength==3:
			first_future_mark=FATHA;
			first_passive_future_mark=DAMMA;
			future_marks=SUKUN+self.future_type+FATHA;
			passive_future_marks=SUKUN+FATHA+FATHA;
        # معالجة الفعل المثال الواوي
        #ToDO

        # الفعل الرباعي
		elif self.vlength==4:
			first_future_mark=DAMMA;
			first_passive_future_mark=DAMMA;
			future_marks=FATHA+SUKUN+KASRA+DAMMA;
			passive_future_marks=FATHA+SUKUN+FATHA+DAMMA;
		# الفعل الخماسي
		elif self.vlength==5:
			first_future_mark=FATHA;
			first_passive_future_mark=DAMMA;
			if letters.startswith(TEH):
				future_marks=FATHA+FATHA+SUKUN+FATHA+DAMMA;
				passive_future_marks=FATHA+FATHA+SUKUN+FATHA+DAMMA;
			else :
				future_marks=FATHA+SUKUN+FATHA+KASRA+DAMMA;
				passive_future_marks=FATHA+SUKUN+FATHA+FATHA+DAMMA;
        #الفعل السداسي
		elif self.vlength==6:
			first_future_mark=FATHA;
			first_passive_future_mark=DAMMA;
			future_marks=FATHA+SUKUN+FATHA+SUKUN+KASRA+DAMMA;
			passive_future_marks=FATHA+SUKUN+FATHA+SUKUN+FATHA+DAMMA;
		# معالجة الألفات في الفعل والحركات الطويلة
		#  إذا كان طول الحركات ألأصلية للفعل أقل من طول حركات الماضي المبني للمجهول
		# هذا يعني وجود حركة طويلة
		# نقوم بتحويل الحركة الطويلة إلى ما يوافقها
		if len(marks)<len(future_marks):
			future_marks=self.homogenize_harakat(marks,future_marks)
			passive_future_marks=self.homogenize_harakat(marks,passive_future_marks)
		imp_marks=future_marks;
		imp_letters=future_letters;
        # حالة الأفعال التي تبدأ بألف وصل
		if letters.startswith(ALEF) or self.hamza_zaida:
			future_letters=letters[1:];
			future_marks=future_marks[1:]
			passive_future_marks=passive_future_marks[1:];
			passive_letters=letters[1:];
        # حالة الفعل المثال
		elif self.vlength==3 and self.word_letters.startswith(WAW) and (self.future_type==KASRA or (self.future_type==FATHA and self.word_marks==FATHA+FATHA+FATHA)):
			future_letters=letters[1:];
			future_marks=future_marks[1:]
##			passive_future_marks=passive_future_marks[1:]
			passive_letters=letters;
		else:
			future_letters=letters;
			passive_letters=letters;
		new_marks=first_future_mark+future_marks;
		passive_marks=first_passive_future_mark+passive_future_marks;

        # حالة الأفعال التي تبدأ بألف وصل
		if imp_letters.startswith(ALEF):
			imp_letters=letters[1:];
			imp_marks=imp_marks[1:]
		elif self.vlength==3 and self.word_letters.startswith(WAW) and (self.future_type==KASRA or (self.future_type==FATHA and self.word_marks==FATHA+FATHA+FATHA)):
			imp_letters=letters[1:];
			imp_marks=imp_marks[1:]
		else:
			imp_letters=letters;

		# معالجة الفعل الناقص عند تصريفه في المجهول
		# تستبدل واو التاقص الذي حركة عين ماضيه فتحة بياء
##		passive_letters=future_letters;
		if self.vlength==3 and passive_letters.endswith(ALEF_MAMDUDA):
			passive_letters=passive_letters[:-1]+ALEF_MAKSURA;
		#  القعل الأمر يأخذ نفس حركات الفعل المضارع دون حركة حرف المضارعة
##		imp_marks=future_marks;
		### معلجة إضافة حرف ألف الوصل في الأفعال المسبوقة بالسكون
##		new_marks=first_future_mark+future_marks;
##		passive_marks=first_passive_future_mark+passive_future_marks;
		self.tab_conjug_stem[TenseFuture]=conjug_stem(TenseFuture,future_letters,new_marks);
		# تصريف الفعل المضارع المنصوب والمجزوم
		self.tab_conjug_stem[TenseJussiveFuture]=conjug_stem(TenseJussiveFuture,future_letters,new_marks);
		self.tab_conjug_stem[TenseSubjunctiveFuture]=conjug_stem(TenseSubjunctiveFuture,future_letters,new_marks);
		# المضارع المؤكد الثقيل
		self.tab_conjug_stem[TenseConfirmedFuture]=conjug_stem(TenseConfirmedFuture,future_letters,new_marks);

        # المبني للمجهول
  		self.tab_conjug_stem[TensePassiveFuture]=conjug_stem(TensePassiveFuture,passive_letters,passive_marks);
		# تصريف الفعل المضارع المنصوب والمجزوم المني للمجهول
		self.tab_conjug_stem[TensePassiveJussiveFuture]=conjug_stem(TensePassiveJussiveFuture,passive_letters,passive_marks);
		self.tab_conjug_stem[TensePassiveSubjunctiveFuture]=conjug_stem(TensePassiveSubjunctiveFuture,passive_letters,passive_marks);
		# المضارع المؤكد الثقيل المنبي للمجهول
		self.tab_conjug_stem[TensePassiveConfirmedFuture]=conjug_stem(TensePassiveConfirmedFuture,passive_letters,passive_marks);

		# الفعل الامر
		self.tab_conjug_stem[TenseImperative]=conjug_stem(TenseImperative,imp_letters,imp_marks);
		# الفعل الامر المؤكد
		self.tab_conjug_stem[TenseConfirmedImperative]=conjug_stem(TenseConfirmedImperative,imp_letters,imp_marks);

# التصريف
# التصريف في المضارع المعلوم
#---------------------------------------------------------------------------
	def prepare_future_and_imperative_stem2(self):
		verb=self.internal_verb;
		verb_nm=self.unvocalized;
		marks=self.word_marks;
		letters=self.word_letters;
		future_letter_mark=FATHA;
		passive_future_letter_mark=DAMMA;
		if not self.teh_zaida and len(verb_nm)==4:
			future_letter_mark=DAMMA;
		before_last_mark=ar_before_last_letter(marks);
		passive_before_last_mark=ar_before_last_letter(marks);
# if the verb is not vocalized
		if passive_before_last_mark==NOT_DEF_HARAKA:
			passive_before_last_mark=FATHA;
		if len(letters)==3 and before_last_mark==NOT_DEF_HARAKA:
			before_last_mark=self.future_type;

		if not self.teh_zaida and len(verb_nm)>=4:
			if before_last_mark in HARAKAT or before_last_mark==NOT_DEF_HARAKA:
				before_last_mark=KASRA;

			elif before_last_mark in LONG_HARAKAT:
			#  حالة انفال ينفال وافتال يفتال وافطال يفطال.
				if len(verb_nm)==5 :before_last_mark=ALEF_HARAKA;
				else: before_last_mark=YEH_HARAKA;
		if self.teh_zaida and len(verb_nm)>=4:
			if before_last_mark in HARAKAT:
				before_last_mark=FATHA;

			elif before_last_mark in LONG_HARAKAT:
				before_last_mark=ALEF_HARAKA;


		elif len(verb_nm)==3:
			if before_last_mark in HARAKAT :
				before_last_mark=self.future_type;
				passive_before_last_mark=FATHA;
			elif before_last_mark in LONG_HARAKAT:
				if self.future_type==FATHA :before_last_mark=ALEF_HARAKA;
				elif self.future_type==DAMMA:before_last_mark=WAW_HARAKA;
				elif self.future_type==KASRA :before_last_mark=YEH_HARAKA;
#معالجة حالة الفعل المبدوء بهمزة قطع المهموز الأول
#والفعل المبدوء بهمزة وصل
		if letters.startswith(ALEF) or (letters.startswith(HAMZA)  and  self.hamza_zaida):
			letters=letters[1:];
			marks=marks[1:];
# معالجة حالة الفعل المثال الواوي الذي عين مضارعه مكسورة
		first_mark=marks[0];
		if len(verb_nm)==3:

		    first_mark=SUKUN;
		if len(marks)==2:
#إذا كان الفعل الثلاثي أجوفا، كان عدد حركاته اثنين، ويكون عند البناء للمجهول ألفا على الدوام
			passive_marks=DAMMA+ALEF_HARAKA+marks[-1:];
			new_marks=future_letter_mark+before_last_mark+marks[-1:];
#حالة الفلع المثال الواوي، ذو حركة عين مضارعه كسرة
#وحركة واوه سكون
#من أجل منع حالة الواو ذو الحركة الطويلة
		elif len(letters)==3 and  first_mark==SUKUN and letters.startswith(WAW) and (self.future_type==KASRA or (self.future_type==FATHA and marks[1]==FATHA)):
#  يحذف الواو في كلتا الحالتين وتصبح حركة طويلة في المبني للمجهول
			letters=letters[1:];

# يحذف الواو في أول المضارع المعلوم
			new_marks=future_letter_mark+before_last_mark+marks[-1:];
# يحذف الواو في أول المضارع المجهول، ويصبح حركة طويلة لحرف المضارعة
			passive_marks=WAW_HARAKA+passive_before_last_mark+marks[-1:];
		else:
			passive_marks=DAMMA+first_mark+marks[1:-2]+passive_before_last_mark+marks[-1:];
			new_marks=future_letter_mark+first_mark+marks[1:-2]+before_last_mark+marks[-1:];

# تحضير جذع الأمر
		imp_letters=self.word_letters;
#حالة الفعل الثلاثي المثال الواوي، الذي حركته ساكنة في المضارع، وحركة  عينه كسرة
#تحذف الواو
		if len(self.word_letters)==3 and  first_mark==SUKUN and self.word_letters.startswith(WAW) and (self.future_type==KASRA or (self.future_type==FATHA and marks[1]==FATHA)):
			imp_letters=self.word_letters[1:];
			imp_marks=KASRA+marks[-1:];
		elif len(letters)!=len(self.word_letters):
		    imp_marks=self.word_marks;
		else:
		    imp_marks=new_marks[1:];
# معالجة الفعل الناقص عند تصريفه في المجهول
# تستبدل واو التاقص الذي حركة عين ماضيه فتحة بياء
		passive_letters=letters;
		if len(self.word_letters)==3 and self.word_letters.endswith(ALEF_MAMDUDA) and marks[1]==FATHA:
		  passive_letters=passive_letters[:-1]+ALEF_MAKSURA;
#  القعل الأمر يأخذ نفس حركات الفعل المضارع دون حركة حرف المضارعة
		imp_marks=imp_marks[:-2]+before_last_mark+imp_marks[-1:];
# معلجة إضافة حرف ألف الوصل في الأفعال المسبوقة بالسكون

		self.tab_conjug_stem[TenseFuture]=conjug_stem(TenseFuture,letters,new_marks);
# تصريف الفعل المضارع المنصوب والمجزوم
		self.tab_conjug_stem[TenseJussiveFuture]=conjug_stem(TenseJussiveFuture,letters,new_marks);
		self.tab_conjug_stem[TenseSubjunctiveFuture]=conjug_stem(TenseSubjunctiveFuture,letters,new_marks);
# المضارع المؤكد الثقيل
		self.tab_conjug_stem[TenseConfirmedFuture]=conjug_stem(TenseConfirmedFuture,letters,new_marks);


# المبني للمجهول
  		self.tab_conjug_stem[TensePassiveFuture]=conjug_stem(TensePassiveFuture,passive_letters,passive_marks);
# تصريف الفعل المضارع المنصوب والمجزوم المني للمجهول
		self.tab_conjug_stem[TensePassiveJussiveFuture]=conjug_stem(TensePassiveJussiveFuture,passive_letters,passive_marks);
		self.tab_conjug_stem[TensePassiveSubjunctiveFuture]=conjug_stem(TensePassiveSubjunctiveFuture,passive_letters,passive_marks);
# المضارع المؤكد الثقيل المنبي للمجهول
		self.tab_conjug_stem[TensePassiveConfirmedFuture]=conjug_stem(TensePassiveConfirmedFuture,passive_letters,passive_marks);

# الفعل الامر
		self.tab_conjug_stem[TenseImperative]=conjug_stem(TenseImperative,imp_letters,imp_marks);
# الفعل الامر المؤكد
		self.tab_conjug_stem[TenseConfirmedImperative]=conjug_stem(TenseConfirmedImperative,imp_letters,imp_marks);

#	--------------------------------------------------------------------------
	def prepare_past_stem(self):
		self.past_stem=self.internal_verb;
		self.tab_conjug_stem[TensePast]=conjug_stem(TensePast,self.word_letters,self.word_marks);

	def homogenize_harakat(self,original_harakat,applied_harakat):
		marks=original_harakat;
		new_marks=applied_harakat;
#  إذا كان طول الحركات ألأصلية للفعل أقل من طول حركات الماضي المبني للمجهول
# هذا يعني وجود حركة طويلة
# نقوم بتحويل الحركة الطويلة إلى ما يوافقها
		if len(marks)<len(new_marks):
			alef_haraka_pos=marks.find(ALEF_HARAKA);
			if alef_haraka_pos<0:
				alef_haraka_pos=marks.find(ALEF_WAW_HARAKA);
			if alef_haraka_pos<0:
				alef_haraka_pos=marks.find(ALEF_YEH_HARAKA);
			if alef_haraka_pos>=0 and alef_haraka_pos+1<len(new_marks):
				first=new_marks[alef_haraka_pos];
				second=new_marks[alef_haraka_pos+1];
				changed_haraka=tab_homogenize_alef_haraka[first][second];
				new_marks=new_marks[:alef_haraka_pos]+changed_haraka+new_marks[alef_haraka_pos+2:]
		return new_marks;

	def prepare_passive_past_stem(self):
##		verb=self.internal_verb;
		letters=self.word_letters;
		marks=self.word_marks;

		if len(letters)==3 and letters.endswith(ALEF_MAMDUDA) and marks[1]==FATHA:
			letters=letters[:-1]+ALEF_MAKSURA;
		if self.vlength==3:
			passive_marks=DAMMA+KASRA+FATHA;
		elif self.vlength==4:
			passive_marks=DAMMA+SUKUN+KASRA+FATHA;
		elif self.vlength==5:
			if letters.startswith(TEH):
				passive_marks=DAMMA+DAMMA+SUKUN+KASRA+FATHA;
			else :
				passive_marks=DAMMA+SUKUN+DAMMA+KASRA+FATHA;
		elif self.vlength==6:
			passive_marks=DAMMA+SUKUN+DAMMA+SUKUN+KASRA+FATHA;
#  إذا كان طول الحركات ألأصلية للفعل أقل من طول حركات الماضي المبني للمجهول
# هذا يعني وجود حركة طويلة
# نقوم بتحويل الحركة الطويلة إلى ما يوافقها
		if len(marks)<len(passive_marks):
			passive_marks=self.homogenize_harakat(marks,passive_marks)

# -	حالة الفعل الأجوف الذي حركة مضارعه فتحة أو كسرة،
#-	فيصبح في الماضي عند التقاء الساكنين كسرة، لذا يجب تعديل ذلك في الماضي المجهول، بجعلها تتحول إلى ضمة عند التقاء الساكنين.
		if len(passive_marks)==2 and passive_marks[0]==YEH_HARAKA and  self.future_type in(FATHA,KASRA):
			passive_marks=ALTERNATIVE_YEH_HARAKA+FATHA;
		self.tab_conjug_stem[TensePassivePast]=conjug_stem(TensePassivePast,letters,passive_marks);

	def conjugate_tense_pronoun(self,tense,pronoun):

        #prefix
		pre_val=TableTensePronoun[tense][pronoun][0];
        #suffix
		suf_val=TableTensePronoun[tense][pronoun][1];
		stem_l=self.tab_conjug_stem[tense].letters;
		stem_m=self.tab_conjug_stem[tense].marks;
#deprecated
##		return self.join(stem_l,stem_m,prefix,suffix);
        # _m : marks
        #_l :letters
		if pre_val!=u"":
			pre_val_l=pre_val;
			pre_val_m=stem_m[0];
			stem_m=stem_m[1:];
		else:
			pre_val_l=u"";
			pre_val_m=u"";

        # the suffix already start by a HARAKA,
        # we add Taweel to ensure valid word in the uniformate function
		suf_val=TATWEEL+suf_val;
        #uniformate suffix
		(suf_val_l,suf_val_m)=uniformate_suffix(suf_val);
        # add affix to the stem
		conj_l=pre_val_l+stem_l+suf_val_l;
		#The end of the stem marks takes the begining of the suffix marks
		conj_m=pre_val_m+stem_m[:-1]+suf_val_m;
        # the begining of suffix letters is Tatweel, it will be striped
		conj_l=pre_val_l+stem_l+suf_val_l[1:];

        # Treat sukun
		conj_m=treat_sukun2(conj_l,conj_m,self.future_type);
        # standard orthographic form
		conj=standard2(conj_l,conj_m);
		return conj;



#--------------------------------------------------------------------------------
# التصريف في الأزمنة المختلفة،
# عند وضع قائمة خاصة بالأزمنة المختارة،
# تلقائيا كافة الأزمنة
#--------------------------------------------------------------------------------
	def conjugate_all_tenses2(self,listtense=TableTense):
#		if listtense==None: listtense=TableTense;
		for tense in listtense:
			if tense not in (TenseImperative,TenseConfirmedImperative):
				for pron in PronounsTable:
					conj=self.conjugate_tense_pronoun(tense,pron);
					self.conj_display.add(tense,pron,conj);
			else:
				for pron in  ImperativePronouns:
					conj=self.conjugate_tense_pronoun(TenseImperative,pron);
					self.conj_display.add(tense,pron,conj);
		self.conj_display.display(listtense);


#-
#--------------------------------------------------------------------------------
# التصريف في الأزمنة المختلفة،
# عند وضع قائمة خاصة بالأزمنة المختارة،
# تلقائيا كافة الأزمنة
#--------------------------------------------------------------------------------
	def conjugate_all_tenses(self,listtense=TableTense):
		for tense in listtense:
			if tense==TensePast:
					conj_ana=self.conjugate_tense_pronoun(tense,PronounAna);
					self.conj_display.add(tense,PronounAna,conj_ana);
					conj_ana_without_last_mark=conj_ana[:-1];
					self.conj_display.add(tense,PronounAnta,conj_ana_without_last_mark+FATHA);
					self.conj_display.add(tense,PronounAnti,conj_ana_without_last_mark+KASRA);
					self.conj_display.add(tense,PronounAntuma,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntuma_f,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntum,conj_ana+MEEM);
					self.conj_display.add(tense,PronounAntunna,conj_ana+NOON+SHADDA+FATHA)
					self.conj_display.add(tense,PronounAna,conj_ana);

					conj_nahnu=self.conjugate_tense_pronoun(tense,PronounNahnu);
					self.conj_display.add(tense,PronounNahnu,conj_nahnu);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huma=self.conjugate_tense_pronoun(tense,PronounHuma);
					self.conj_display.add(tense,PronounHuma,conj_huma);

					conj_hum=self.conjugate_tense_pronoun(tense,PronounHum);
					self.conj_display.add(tense,PronounHum,conj_hum);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huwa=self.conjugate_tense_pronoun(tense,PronounHuwa);
					self.conj_display.add(tense,PronounHuwa,conj_huwa);
					conj_hya=self.conjugate_tense_pronoun(tense,PronounHya);
					self.conj_display.add(tense,PronounHya,conj_hya);
					self.conj_display.add(tense,PronounHuma_f,conj_hya[:-1]+FATHA+ALEF);
			elif tense ==TensePassivePast:
					conj_ana=self.conjugate_tense_pronoun(tense,PronounAna);
					self.conj_display.add(tense,PronounAna,conj_ana);
					conj_ana_without_last_mark=conj_ana[:-1];
					self.conj_display.add(tense,PronounAnta,conj_ana_without_last_mark+FATHA);
					self.conj_display.add(tense,PronounAnti,conj_ana_without_last_mark+KASRA);
					self.conj_display.add(tense,PronounAntuma,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntuma_f,conj_ana+MEEM+FATHA+ALEF);
					self.conj_display.add(tense,PronounAntum,conj_ana+MEEM);
					self.conj_display.add(tense,PronounAntunna,conj_ana+NOON+SHADDA+FATHA)
					self.conj_display.add(tense,PronounAna,conj_ana);

					conj_nahnu=self.conjugate_tense_pronoun(tense,PronounNahnu);
					self.conj_display.add(tense,PronounNahnu,conj_nahnu);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_hunna=self.conjugate_tense_pronoun(tense,PronounHunna);
					self.conj_display.add(tense,PronounHunna,conj_hunna);

					conj_huwa=self.conjugate_tense_pronoun(tense,PronounHuwa);
					self.conj_display.add(tense,PronounHuwa,conj_huwa);
# حالة الفعل مهموز الآخر
					if conj_huwa.endswith(YEH+HAMZA+FATHA) :
					   self.conj_display.add(tense,PronounHya,conj_huwa[:-2]+YEH_HAMZA+FATHA+TEH+SUKUN);
					   self.conj_display.add(tense,PronounHuma_f,conj_huwa[:-2]+YEH_HAMZA+FATHA+TEH+FATHA+ALEF);
##					   conj_huma=self.conjugate_tense_pronoun(tense,PronounHuma);
					   self.conj_display.add(tense,PronounHuma,conj_huwa[:-2]+YEH_HAMZA+FATHA+ALEF);

##					   conj_hum=self.conjugate_tense_pronoun(tense,PronounHum);
					   self.conj_display.add(tense,PronounHum,conj_huwa[:-2]+YEH_HAMZA+DAMMA+WAW+ALEF);

					else :
					   self.conj_display.add(tense,PronounHya,conj_huwa+TEH+SUKUN);
					   self.conj_display.add(tense,PronounHuma_f,conj_huwa+TEH+FATHA+ALEF);
					   self.conj_display.add(tense,PronounHuma,conj_huwa+ALEF);
					   if conj_huwa.endswith(KASRA+YEH+FATHA):
					       self.conj_display.add(tense,PronounHum,conj_huwa[:-3]+DAMMA+WAW+ALEF);
					   else:
					       self.conj_display.add(tense,PronounHum,conj_huwa[:-1]+DAMMA+WAW+ALEF);
			elif tense in (TenseFuture,TensePassiveFuture,TenseJussiveFuture,TenseSubjunctiveFuture,TenseConfirmedFuture,TensePassiveJussiveFuture,TensePassiveSubjunctiveFuture,TensePassiveConfirmedFuture):
					conj_ana=self.conjugate_tense_pronoun(tense,PronounAna);
					self.conj_display.add(tense,PronounAna,conj_ana);

					conj_anta=self.conjugate_tense_pronoun(tense,PronounAnta);
					self.conj_display.add(tense,PronounAnta,conj_anta);
					conj_anta_without_future_letter=conj_anta[1:];
##					self.conj_display.add(tense,PronounAnta,TEH+conj_ana_without_future_letter);
					self.conj_display.add(tense,PronounNahnu,NOON+conj_anta_without_future_letter);
					self.conj_display.add(tense,PronounHuwa,YEH+conj_anta_without_future_letter);
					self.conj_display.add(tense,PronounHya,TEH+conj_anta_without_future_letter);

					conj_anti=self.conjugate_tense_pronoun(tense,PronounAnti);
					self.conj_display.add(tense,PronounAnti,conj_anti);

					conj_antuma=self.conjugate_tense_pronoun(tense,PronounAntuma);
					self.conj_display.add(tense,PronounAntuma,conj_antuma);
					self.conj_display.add(tense,PronounAntuma_f,conj_antuma);
					self.conj_display.add(tense,PronounHuma_f,conj_antuma);
					self.conj_display.add(tense,PronounHuma,YEH+conj_antuma[1:]);

					conj_antum=self.conjugate_tense_pronoun(tense,PronounAntum);
					self.conj_display.add(tense,PronounAntum,conj_antum);
					self.conj_display.add(tense,PronounHum,YEH+conj_antum[1:]);

					conj_antunna=self.conjugate_tense_pronoun(tense,PronounAntunna);
					self.conj_display.add(tense,PronounAntunna,conj_antunna);
					self.conj_display.add(tense,PronounHunna,YEH+conj_antunna[1:]);
			elif tense ==TenseImperative or  tense ==TenseConfirmedImperative:
				for pron in  ImperativePronouns:
					conj=self.conjugate_tense_pronoun(tense,pron);
					self.conj_display.add(tense,pron,conj);
##		self.conj_display.display_html(listtense);
# if the result is not diplyed directely on the screen, we return it
		result=self.conj_display.display(self.conj_display.mode,listtense);
		if result: return result;
#--------------------------------------------------------
# return True if the verb is irregular, founded in the irregular verb table
# إرجاع إّذا كان الفعل ضاذا
#
#--------------------------------------------------------
	def is_irregular_verb(self):
	    if len(self.word_letters)!=3: return False;
	    else:
	        # the key is composed from the letters and past and future marks, to identify irregular verb
	        key=self.word_letters+self.past_haraka+self.future_type
	        if IrregularVerbsConjug.has_key(key ):
	            return True;
##	            if self.past_haraka== IrregularVerbsConjug[self.word_letters][ConjugBab][0] and self.future_type== IrregularVerbsConjug[self.word_letters][ConjugBab][1]:
##	                return True;
	    return False;
#--------------------------------------------------------
# return True if the verb is irregular, founded in the irregular verb table
# إرجاع إّذا كان الفعل ضاذا
#
#--------------------------------------------------------
	def get_irregular_future_stem(self):
      # the key is composed from the letters and past and future marks, to identify irregular verb
	   key=self.word_letters+self.past_haraka+self.future_type
	   if  IrregularVerbsConjug.has_key(key):
	     return IrregularVerbsConjug[key][TenseFuture];
	   else:
	       self.word_letters
#--------------------------------------------------------
	def get_irregular_passivefuture_stem(self):
      # the key is composed from the letters and past and future marks, to identify irregular verb
	   key=self.word_letters+self.past_haraka+self.future_type
	   if IrregularVerbsConjug.has_key(key):
	     return IrregularVerbsConjug[key][TensePassiveFuture];
	   else:
	       self.word_letters
#--------------------------------------------------------
	def get_irregular_imperative_stem(self):
      # the key is composed from the letters and past and future marks, to identify irregular verb
	   key=self.word_letters+self.past_haraka+self.future_type
	   if  IrregularVerbsConjug.has_key(key):
	     return IrregularVerbsConjug[key][TenseImperative];
	   else:
	       self.word_letters

#--------------------------------------------------------
# prepare the irregular conjug for future and imperative
# تحضير جذوع التصريف في المضارع والأمر للأفعال الضاذة
#
#--------------------------------------------------------
	def prepare_irregular_future_and_imperative_stem(self):
##	   if self.word_letters in IrregularVerbsConjug.keys():
	   if self.is_irregular_verb():
	       (l,m)=self.get_irregular_future_stem();
	       #IrregularVerbsConjug[self.word_letters][TenseFuture];
#تمت إضافة حركة حرف المضارعة إلى الجذع المستعمل في الفعل الشاذ
	       self.tab_conjug_stem[TenseFuture]=conjug_stem(TenseFuture,l,m);
	       self.tab_conjug_stem[TenseJussiveFuture]=conjug_stem(TenseJussiveFuture,l,m);
	       self.tab_conjug_stem[TenseSubjunctiveFuture]=conjug_stem(TenseSubjunctiveFuture,l,m);
	       self.tab_conjug_stem[TenseConfirmedFuture]=conjug_stem(TenseConfirmedFuture,l,m);


	       (l1,m1)=self.get_irregular_passivefuture_stem();
#تمت إضافة حركة حرف المضارعة إلى الجذع المستعمل في الفعل الشاذ
	       self.tab_conjug_stem[TensePassiveFuture]=conjug_stem(TensePassiveFuture,l1,m1);
	       self.tab_conjug_stem[TensePassiveJussiveFuture]=conjug_stem(TensePassiveJussiveFuture,l1,m1);
	       self.tab_conjug_stem[TensePassiveSubjunctiveFuture]=conjug_stem(TensePassiveSubjunctiveFuture,l1,m1);
	       self.tab_conjug_stem[TensePassiveConfirmedFuture]=conjug_stem(TensePassiveConfirmedFuture,l1,m1);


	       (l2,m2)=self.get_irregular_imperative_stem();
	       self.tab_conjug_stem[TenseImperative]=conjug_stem(TenseImperative,l2,m2);
	       self.tab_conjug_stem[TenseConfirmedImperative]=conjug_stem(TenseConfirmedImperative,l2,m2);
##	       print l.encode("utf"),m.encode("utf");
	   return False;
