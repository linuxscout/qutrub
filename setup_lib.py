#! /usr/bin/python
from distutils.core import setup
from glob import glob

# to install type:
# python setup.py install --root=/

setup (name='LibQutrub', version='1.0',
      description='libqutrub Arabic verb conjuagtion library',
      author='Taha Zerrouki',
      author_email='taha(dot) zerrouki (at) gmail.com',
      url='http://libqutrub.sourceforge.net/',
      license='GPL',
      #Description="Arabic Arabic text tools for Python",
      #platform="OS independent",
      package_dir={'libqutrub': 'libqutrub',},
      packages=['libqutrub'],
      # include_package_data=True,
      package_data = {
        'libqutrub': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS independent',
          'Programming Language :: Python',
          ],
    );
