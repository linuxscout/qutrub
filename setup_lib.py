#! /usr/bin/python
from setuptools  import setup
from io import open
# to install type:
# python setup.py install --root=/
def readme():
    with open('README.rst', encoding="utf8") as f:
        return f.read()
setup (name='libqutrub', version='1.2.5',
      description='libqutrub Arabic verb conjuagtion library',
      long_description = readme(),        
      author='Taha Zerrouki',
      author_email='taha.zerrouki@gmail.com',
      url='http://libqutrub.sourceforge.net/',
      license='GPL',
      platform="OS independent",
      package_dir={'libqutrub': 'libqutrub',},
      packages=['libqutrub'],
      install_requires=[ 'pyarabic>=0.6.2',
      ],         
      include_package_data=True,
      package_data = {
        'libqutrub': ['doc/*.*','doc/html/*'],
        },
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: End Users/Desktop',
          'Programming Language :: Python',
          ],
    );
