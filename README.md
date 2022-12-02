
Qutrub
=======
  Qutrub: Arabic verb conjugation software  قطرب: تصريف الأفعال العربية

[![downloads]( https://img.shields.io/sourceforge/dt/qutrub.svg)](http://sourceforge.org/projects/qutrub)
[![downloads]( https://img.shields.io/sourceforge/dm/qutrub.svg)](http://sourceforge.org/projects/qutrub)

  Developers: 	Taha Zerrouki: http://tahadz.com
	taha dot zerrouki at gmail dot com


Features |   value
---------|---------------------------------------------------------------------------------
Authors  | [Authors.md](https://github.com/linuxscout/qutrub/master/AUTHORS.md)
Release  | 1.5 (app), 1.2.4 (library)
License  |[GPL](https://github.com/linuxscout/qutrub/master/COPYING)
Tracker  |[linuxscout/qutrub/Issues](https://github.com/linuxscout/qutrub/issues)
Mailinglist  |[<qutrub@googlegroups.com>](http://groups.google.com/group/qutrub/)
Website  |[qutrub.arabeyes.org](http://qutrub.arabeyes.org)
Source  |[Github](http://github.com/linuxscout/qutrub)
Download  |[sourceforge](http://qutrub.sourceforge.net)
Feedbacks  |[Comments](http://tahadz.com/qutrub/contact)
Accounts  | [@Twitter](https://twitter.com/linuxscout)  [@Sourceforge](http://sourceforge.net/projectsqutrub/)


## Install

--------
### Requirements

pyarabic>=0.6.2

### Installation on Apache

enable mod_python in Apache
extract the qutrub package and run it from the web.
The program doesn't need a database.

### Installation as library 

```shell
pip install libqutrub
```
### Installation as an application

check that python is of version 2.5, it support python3 or higher is installed
extract the package
run the conjugate.py script 

``` Usage 

(C) CopyLeft 2009, Taha Zerrouki
Usage: conjugate -f filename [OPTIONS]
	[-h | --help]		outputs this usage message
	[-V | --version]	program version
	[-f | --file= filename]	input file to conjugate
	[-d | --display=  format]	display format as html,csv, tex, xml"
	[-a | --all ]		Conjugate in all tenses
	[-i | --imperative]	Conjugate in imperative
	[-F | --future]		conjugate in the present and the future
	[-p | --past]		conjugate in the past
	[-c | --confirmed]	conjugate in confirmed ( future or imperative) "
	[-m | --moode]		conjugate in future Subjunctive( mansoub) or Jussive (majzoom) "
	[-v | --passive]	passive form
	N.B. FILE FORMAT is descripted in README
	This program is licensed under the GPL License
```

#### Input file format   

-File encoding must be "utf8"
The input file  format is a text comma separeted  csv
Fields are separated by tabulation.
A line can be ignored, if it begin by '#'
The first field is the verb in vocalised form
The second field is the mark of the letter before last in the future tense, it used just for the verb Thulathi (with three letters).

```
	values 
		Fahta:
			1- fatha
			2-فتحة
			3-ف
			4-f
		DAMMA:
			1- damma
			2-ضمة
			3-ض
			4-d
		kasra:
			1- kasra
			2-كسرة
			3-ك
			4-k
	or values used as Conjugation mode ( Bab Tasrif باب التصريف)
		Bab		past	future
		1		FATHA	DAMMA
		2		FATHA	KASRA
		3		FATHA	FATHA
		4		KASRA	FATHA
		5		DAMMA	DAMMA
		6		KASRA	KASRA
```
The third field is :Transitive/intransitive
	values can be used in this field are:
```
		transitive :
				1-متعدي
				2-م
				3-مشترك
				4-ك
				5-t
				6-transitive
		intransitive:
				1-لازم
				2-ل
				3-i
				4-intransitive
```
Example 
#### commented line
```
كَتَبَ	ضمة	متعدي
ضَرَبَ	كسرة	متعدي
ذَكَرَ	ضمة	متعدي
سَكَتَ	ضمة	لازم
سَكَنَ	ضمة	متعدي
عَلَّمَ		متعدي
صَارَعَ	-	متعدي
أَكْرَمَ	-	متعدي
تَفَقَّدَ	-	متعدي
تَنَازَعَ	-	متعدي
اِدَّارَكَ	-	متعدي

```
This program is licensed under the GPL License

### Call from python
* Simple call
```python
import libqutrub.conjugator

verb=u"سعد"
future_type =u"كسرة"
table = libqutrub.conjugator.conjugate(verb,future_type, transitive= True);
print(table)

```
* display format
display format can be : 
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
```python
import libqutrub.conjugator

verb=u"سعد"
future_type =u"كسرة"
table = libqutrub.conjugator.conjugate(verb,future_type, transitive= True, display_format="DICT");
print(table)

```
* more options
```python
import libqutrub.conjugator

verb=u"سعد"
future_type =u"كسرة"
all = True # all tenses
past = True
future=True
passive =True
imperative=True
future_moode= True
confirmed=False
transitive =True
display_format="HTML"
table = libqutrub.conjugator.conjugate(verb,future_type,all,past,future,passive,imperative,future_moode,confirmed,transitive,display_format);
print(table)

```
### Web API
view [API doc](doc/api.md)
