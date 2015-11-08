#!/usr/bin/python
# -*- coding=utf-8 -*-
#************************************************************************
# $Id: conjugate.py,v 0.7 2009/06/02 01:10:00 Taha Zerrouki $
#
# ------------
# Description:
# ------------
#  Copyright (c) 2009, Arabtechies, Arabeyes Taha Zerrouki
#
#  This file is the main file to execute the application in the command line
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

##from verb_const import *
##from ar_ctype import *
##from classverb import *
import figleaf
figleaf.start()
from src.verb_const import *
from src.ar_verb import *
def main():
	word=u"تُيُسَّرَ";
	letters, marks=uniformate_verb(word);
	marks=DAMMA+DAMMA+SUKUN+KASRA+FATHA
	newword=standard2(letters, marks);
	print letters.encode('utf8');
	print write_harakat_in_full(marks).encode('utf8');
	print newword.encode('utf8');
	
if __name__ == "__main__":
	main();
	figleaf.stop()
	figleaf.write_coverage('performance.figleaf')







