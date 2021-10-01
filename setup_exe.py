#! /usr/bin/python
from distutils.core import setup
from glob import glob
import py2exe

# to install type:
# python setup.py install --root=/

setup (name='Qutrub', version='1.0',
      description='Qutrub Arabic verb conjugator',
      author='Taha Zerrouki',
      author_email='taha dot zerrouki at gmail.com',
      url='http://qutrub.org/',
      license='GPL',
	 console = [
        {
            "script": "main_gui.py",
            "icon_resources": [(1, "images/qutrub.ico")]
        }
    ],
	 windows = [
        {
            "script": "main_gui.py",
            "icon_resources": [(1, "images/qutrub.ico")]
        }
    ],

      #scripts=['Qutrub'],
      classifiers=[
          'Development Status ::  5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
      data_files=[
	  #('images',['f:\gui/qutrub/libqutrub/images/save.png']),
	  ('images',['./images/logo.jpg','./images/qutrub.ico','./images/qutrub2.ico','./images/qaf.png']),
	  ('resources',
	   ['./resources/style.css',
	   './resources/qutrub_body.html',
       './resources/about.html',
       './resources/help_body.html']
       ),
	  ('resources/images',
	  [	  './resources/images/print.png',
	  './resources/images/save.png',
	  './resources/images/preview.png',
	  './resources/images/copy.png',
	  './resources/images/cut.png',
	  './resources/images/font.png',
	  './resources/images/help.jpg',
	  './resources/images/new.png',
	  './resources/images/exit.png',
	  './resources/images/zoomin.png',
	  './resources/images/zoomout.png',
	  './resources/images/logo.png' ])
,
	  ('resources/languages',
	  [	  './resources/languages/en.qm',
	  './resources/languages/de.qm',
	  './resources/languages/fr.qm',
	  './resources/languages/ur.qm',
	  './resources/languages/fa.qm',
	  './resources/languages/ms.qm',
	  './resources/languages/jp.qm']),

	  ('resources/languages/ar',
	   ['./resources/languages/ar/qutrub_body.html',
       './resources/languages/ar/about.html',
       './resources/languages/ar/help_body.html']
       ),
	   
	  ('resources/languages/en',
	   ['./resources/languages/en/qutrub_body.html',
       './resources/languages/en/about.html',
       './resources/languages/en/help_body.html']
       ),

	  ('resources/languages/fr',
	   ['./resources/languages/fr/qutrub_body.html',
       './resources/languages/fr/about.html',
       './resources/languages/fr/help_body.html']
       ),

	  ('resources/languages/de',
	   ['./resources/languages/de/qutrub_body.html',
       './resources/languages/de/about.html',
       './resources/languages/de/help_body.html']
       ),
	  ('resources/languages/jp',
	   ['./resources/languages/jp/qutrub_body.html',
       './resources/languages/jp/about.html',
       './resources/languages/jp/help_body.html']
       ),
	  ('resources/languages/fa',
	   ['./resources/languages/fa/qutrub_body.html',
       './resources/languages/fa/about.html',
       './resources/languages/fa/help_body.html']
       ),
	  ('resources/languages/ur',
	   [  './resources/languages/ur/qutrub_body.html',
       './resources/languages/ur/about.html',
       './resources/languages/ur/help_body.html']
       ),	
	  
	  ]);

