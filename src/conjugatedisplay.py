#!/usr/bin/python
# -*- coding=utf-8 -*-
#************************************************************************
# $Id: conjugateddisplay.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  The Class used to display information after conjugated
#   All print and views and display are redirected to this class
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

from verb_const import *
from ar_ctype import *
import sys,re,string
##import simplejson as json
# صف عرض التصريفات حسب الضمائر
# جدول عرض التصريفات حسب الأزمنة
# تعيينه متغيرا شاملا من أجل تقليل بناء جدول عرض التصريفات في كل عرض.
OneTensePronoun={u"أنا":"" ,u"أنت":"" ,u"أنتِ":"" ,u"هو":"" ,u"هي":"" ,u"أنتما":"" ,u"أنتما مؤ":"" ,u"هما":"" ,u"هما مؤ":"" ,u"نحن":"" ,u"أنتم":"" ,u"أنتن":"" ,u"هم":"" ,u"هن":""}
TableConjug={TensePast:OneTensePronoun.copy(),
	TensePassivePast:OneTensePronoun.copy(),
	TenseFuture:OneTensePronoun.copy(),
	TensePassiveFuture:OneTensePronoun.copy(),
	TenseJussiveFuture:OneTensePronoun.copy(),
	TensePassiveJussiveFuture:OneTensePronoun.copy(),
	TenseSubjunctiveFuture:OneTensePronoun.copy(),
	TensePassiveSubjunctiveFuture:OneTensePronoun.copy(),
	TenseImperative:OneTensePronoun.copy(),
	TenseConfirmedFuture:OneTensePronoun.copy(),
	TenseConfirmedImperative:OneTensePronoun.copy()
	}


TabDisplay={
PronounAna:u"1",
PronounNahnu:u"2",
PronounAnta:u"3",
PronounAnti:u"4ِ",
PronounAntuma:u"5",
PronounAntuma_f:u"6",
PronounAntum:u"7",
PronounAntunna:u"8",
PronounHuwa:u"9",
PronounHya:u"10",
PronounHuma:u"11",
PronounHuma_f:u"12",
PronounHum:u"13",
PronounHunna:u"14",


# const for Tense Name
TensePast:u"20",
TenseFuture:u"21",
TenseImperative:u"22",
TenseConfirmedImperative:u"23",
TenseJussiveFuture:u"24",
TenseSubjunctiveFuture:u"25",
TenseConfirmedFuture:u"26",


TensePassivePast:u"27",
TensePassiveFuture:u"28",
TensePassiveJussiveFuture:u"29",
TensePassiveSubjunctiveFuture:u"30",
TensePassiveConfirmedFuture:u"31",
}
class conjugatedisplay:
	tab_conjug={}
	pronouns={}
	verb=u""
	mode='Text'
	future_form=u""
	text={}
	transitive=False;
	def __init__(self,verb):
# بناء جدول عرض التصريفات
		self.tab_conjug=TableConjug.copy()
		self.verb=verb
		self.text={}
		self.mode='Text'
		self.future_form=u"";
		self.transitive=False;
		self.bab="0";
#------------------------------------------------------------------
	def setmode(self,mode):
		self.mode=mode
	def settransitive(self):
		self.transitive
	def setbab(self,bab):
		self.bab=bab
#------------------------------------------------------------------
	def set_future_form(self,future_form):
		self.future_form=future_form
#------------------------------------------------------------------
# add a new conjugation to display
#a conjugation contains
#a tense, a pronoun, a verbconjugated
#------------------------------------------------------------------
	def add(self,tense,pronoun,verbconjugated):
		if tense not in self.tab_conjug.keys():
			self.tab_conjug[tense]={}
		self.tab_conjug[tense][pronoun]=verbconjugated
#------------------------------------------------------------------
# Add a new attribut to display
#a attribut contains
#a title, an a value
#------------------------------------------------------------------
	def add_attribut(self,title,value):
		if title!='' :
			self.text[title]=value
	def get_verb_attributs(self):
	    return self.text;
#------------------------------------------------------------------
	def display(self,listtense=TableTense):
		return self.display(self.mode,listtense);
	def display(self,mode, listtense=TableTense):
		if mode=='Text':
		    return self.display_text(listtense)
		elif mode=='HTML':
		    return self.display_html(listtense)
		elif mode=='HTMLColoredDiacritics':
		    return self.display_html_colored_diacritics(listtense)
		elif mode=='DICT':
		    return self.display_dict(listtense)
		elif mode=='CSV':
		    return self.display_csv(listtense)
		elif mode=='GUI':
		    return self.display_table(listtense)
		elif mode=='TABLE':
		    return self.display_table(listtense)
		elif mode=='XML':
		    return self.display_xml(listtense)
		elif mode.upper()=='TeX'.upper():
		    return self.display_tex(listtense)
		elif mode=='ROWS'.upper():
		    return self.display_rows(listtense)
		else:
		    return self.display_text(listtense)
#-------------------------------------------------
#
#
#-------------------------------------------------
	def display_text(self,listtense=TableTense):
		text = u""
		for title in self.text.keys():
			text+= u"%s: %s\n" %(title, self.text[title])
		text+= u"\t"
		text+=u"\t".join(listtense);
		for pronoun in PronounsTable:
			text+= u"\n%s" %(pronoun)
			for tense in listtense:
				if pronoun in self.tab_conjug[tense].keys():
					text+= u"\t%s" %(self.tab_conjug[tense][pronoun])
		return text
#-------------------------------------------------
#
#
#-------------------------------------------------
	def display_csv(self,listtense=TableTense):
		text = u""
		for title in self.text.keys():
			text+= u"%s: %s\n" %(title,self.text[title])
		text+= u";".join(listtense);
		text+=u"\n";
		for pronoun in PronounsTable:
			text+= u"%s" %(pronoun)
			for tense in listtense:
#				print (self.verb).encode("utf-8"),
				if pronoun in self.tab_conjug[tense].keys():
					text+= u";%s" %(self.tab_conjug[tense][pronoun])
			text+= u"\n"
		return text

#-------------------------------------------------
#
#
#-------------------------------------------------


	def display_rows(self,listtense=TableTense):
		text = u""
##		for title in self.text.keys():
##			text+= u"%s: %s\n" %(title,self.text[title])
##		text+= u";".join(listtense);
##		text+=u"\n";
		transitive="0";
		if self.transitive:transitive='1';
		for pronoun in PronounsTable:
##			text+= u"%s" %(pronoun)
			for tense in listtense:
#				print (self.verb).encode("utf-8"),
				if  self.tab_conjug[tense][pronoun]!="":#pronoun  in self.tab_conjug[tense].keys():
					text+= "\t".join([
						ar_strip_marks_keepshadda(self.tab_conjug[tense][pronoun]),
						self.tab_conjug[tense][pronoun],
						TabDisplay[pronoun],
						TabDisplay[tense],
						transitive,
						self.verb,
						self.bab,
						]);
					text+= u"\n"
		return text


#----------------------------------------------------------
# display_gui
# return a HTML formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_html(self,listtense=TableTense):
		indicativeTenses=[];
		passiveTenses=[];
		for t in listtense:
			if t in TableIndicativeTense:
				indicativeTenses.append(t);
			else:
				passiveTenses.append(t);
		text = u""
		text+= u"<h3>%s : %s - %s</h3>\n" %(self.verb,self.verb,self.future_form)
#		text+= u"<h3>%s - %s</h3>\n\n" %(self.verb,self.future_form)
		# print spelcial attribut of the verb
		text+= u"<ul>\n"
		for title in self.text.keys():
			text+= u"<li><b>%s:</b> %s</li>\n" %(title,self.text[title])
		text+= u"</ul>\n\n"

		for  mode in("indicative","passive"):
			if mode=="indicative":
				listtenseToDisplay=indicativeTenses;

			else:
				listtenseToDisplay=passiveTenses;
				text+="<br/>"
			if len(listtenseToDisplay) >0:
				text+= u"<table class='resultarea' border=1 cellspacing=0>\n"
				text+= u"<tr><th>&nbsp;</th>"
				for tense in listtenseToDisplay:
					text+= u"<th>%s</th>" %(tense)
				text+= u"</tr>\n"
				for pronoun in PronounsTable:
					text+= u"<tr>"
					text+= u"<th>%s</th>" %(pronoun)
					for tense in listtenseToDisplay:
						text+= u"<td>&nbsp;%s</td>" %(self.tab_conjug[tense][pronoun])
					text+=u"</tr>\n"
				text+=u"</table>\n"
		return text
###----------------------------------------------------------
### display_gui
### return a HTML formatted text with tenses and conjugated verb
###
###
###-----------------------------------------------------------
##
##	def display_html2(self,listtense=TableTense):
##		indicativeTenses=[];
##		passiveTenses=[];
##		for t in listtense:
##			if t in TableIndicativeTense:
##				indicativeTenses.append(t);
##			else:
##				passiveTenses.append(t);
##		text = u""
##		text+= u"<h3>%s : %s - %s</h3>\n" %(self.verb,self.verb,self.future_form)
###		text+= u"<h3>%s - %s</h3>\n\n" %(self.verb,self.future_form)
##        # print spelcial attribut of the verb
##		text+= u"<ul>\n"
##		for title in self.text.keys():
##			text+= u"<li><b>%s:</b> %s</li>\n" %(title,self.text[title])
##		text+= u"</ul>\n\n"
##		# Ad mechanisme to set font size
##		text+=u"<span id='holder1'></span>"
##		#tabs for conjugation mood
##		text+="""<div id="tabs">"""
##		text+=u"<ul>"
##
##		if len(indicativeTenses)>0 :
##			text+=u"""<li><a href="#tabs-1">المبني للمعلوم</a></li>"""
##		if len(passiveTenses)>0:
##			text+=u"""<li><a href="#tabs-2">المبني للمجهول</a></li>"""
###		text+=u"<li><a href="#tabs-3"><span id='holder1'></span></a></li>"
##		text+=u"</ul>";
##		# print conjugation
##		text+=u"""<div id='resultat'>"""
##		# tabs-1 : for indicative
##		#tabs-2 : for passive
##		for  mode in("indicative","passive"):
##			if mode=="indicative":
##				listtenseToDisplay=indicativeTenses;
##				classid='tabs-1';
##			else:
##				listtenseToDisplay=passiveTenses;
##				classid='tabs-2';
##			if len(listtenseToDisplay) >0:
##				text+= u"<div id='%s' class='result'>\n"%classid;
##				text+= u"<table border=1 cellspacing=0 id='result' class='result' >\n"
##				text+= u"<tr><th>&nbsp;</th>"
##				for tense in listtenseToDisplay:
##					text+= u"<th>%s</th>" %(tense)
##				text+= u"</tr>\n"
##				for pronoun in PronounsTable:
##					text+= u"<tr>"
##					text+= u"<th>%s</th>" %(pronoun)
##					for tense in listtenseToDisplay:
##						text+= u"<td>&nbsp;%s</td>" %(self.tab_conjug[tense][pronoun])
##					text+=u"</tr>\n"
##				text+=u"</table>\n"
##				text+=u"</div><br/>\n"
##		text+=u"</div></div>"
##		return text
#----------------------------------------------------------
# display_gui
# return a HTML formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_html_colored_diacritics(self,listtense=TableTense):
		text = self.display_html(listtense)
##		text="<div style='color:red'>"+text+"</div>"
		text=self.highlight_diacritics_html(text);
		return text;

	def highlight_diacritics_html(self,text):
		hight_text=u"";
		lefttag=u"<span class='tashkeel'>"
#		lefttag=u"<span style='color:red;'>"
		righttag=u"</span>"
		for i in range(len(text)):
		    if text[i] in (FATHA,DAMMA, KASRA, SUKUN):
		        if (i>0 and text[i-1] not in (ALEF,ALEF_HAMZA_ABOVE,WAW_HAMZA,ALEF_MADDA, DAL,THAL,WAW,REH,ZAIN,SHADDA)) and (i+1<len(text) and text[i+1] not in (" ","<")):
		           hight_text+=u"".join([lefttag,TATWEEL, text[i],righttag]);
		        else :
##               hight_text+=u"<span style='color:red'>%s</span>"%text[i];
		           hight_text+=u"".join([lefttag," ", text[i],righttag]);
		    else:
		        hight_text+=text[i];
		return hight_text;
#----------------------------------------------------------
# display_table
# return a table with tenses and conjugated verb
#
#
#-----------------------------------------------------------
	def display_table(self,listtense=TableTense):
		table={}

		j=0;
		table[0]={0:u"الضمائر"}
		for j in range(len(listtense)):
		  table[0][j+1]=listtense[j];
		i=1;
		for pronoun in PronounsTable:
		  table[i]={}
		  table[i][0]=pronoun;
		  j=1
		  for tense in listtense:
		      table[i][j]=self.tab_conjug[tense][pronoun]
		      j=j+1
		  i=i+1
		return table
#----------------------------------------------------------
# display_table
# return a table with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_dict(self,listtense=TableTense):
		table={}
		for tense in listtense:
			table[tense]=self.tab_conjug[tense];
		#text=json.dumps(table,ensure_ascii=False);
		return table;
#----------------------------------------------------------
# display_gui
# return a HTML formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_xml(self,listtense=TableTense):
		text = u""
		text+= u"<verb_conjugation>\n"
		text+= u"\t<proprety name='verb' value='%s'/>\n" %(self.verb)
		for title in self.text.keys():
			text+= u"\t<proprety name='%s' value='%s'/>\n" %(title,self.text[title])
		for tense in listtense:
			text+= u"\t<tense name='%s'>\n" %(tense)
			for pronoun in PronounsTable:
			 if self.tab_conjug[tense][pronoun]!="":
			     text+= u"\t\t<conjugation pronoun='%s' value='%s'/>\n" %(pronoun,self.tab_conjug[tense][pronoun])
			text+= u"\t</tense>\n"
		text+= u"</verb_conjugation>"
		return text
#----------------------------------------------------------
# display_tex
# return a TeX formatted text with tenses and conjugated verb
#
#
#-----------------------------------------------------------

	def display_tex(self,listtense=TableTense):
		text = u""
		text+= u"\\environment qutrub-layout\n"
		text+= u"\\starttext\n"

		text+= u"\\Title{%s}\n" %(self.verb)

		text+= u"\\startitemize\n"
		for title in self.text.keys():
			if title == u" الكتابة الداخلية للفعل ":
				text+= u"\\item {\\bf %s} \\DeShape{%s}\n" %(title,self.text[title])
			else:
				text+= u"\\item {\\bf %s} %s\n" %(title,self.text[title])
		text+= u"\\stopitemize\n"

		text+= u"\\starttable[|lB|l|l|l|l|l|]\n"
		text+= u"\\HL[3]\n\\NC"
		for tense in listtense:
			text+= u"\\NC {\\bf %s}" %(tense)
		text+= u"\\SR\n\\HL\n"
		for pronoun in PronounsTable:
			text+= u"\\NC %s" %(pronoun)
			for tense in listtense:
				text+= u"\\NC %s" %(self.tab_conjug[tense][pronoun])
			text+= u"\\AR\n"
		text+= u"\\LR\\HL[3]\n"
		text+= u"\\stoptable\n"

		text+= u"\\stoptext"
		return text
