#/usr/bin/sh
# Build  Qutrub: Arabic verb conjugation software  

default: all
# Clean build files
clean:
	
backup: 
	
#create all files 
all: install install3 wheel wheel3  doc sdist 
install:
	sudo python setup_lib.py install
install3:
	sudo python3 setup_lib.py install
# Publish to github
publish:
	git push origin master 

md2rst:
	pandoc -s -r markdown -w rst README.md -o README.rst
md2html:
	pandoc -s -r markdown -w html README.md -o README.html
	
wheel:
	sudo python setup_lib.py bdist_wheel
wheel3:
	sudo python3 setup_lib.py bdist_wheel
sdist:
	sudo python setup_lib.py sdist
upload:
	echo "use twine upload dist/libqutrub-0.1.tar.gz"
	
test:
	python -m unittest discover tests
test3:
	python3 -m unittest discover tests
doc:
	epydoc -v --config epydoc.conf

test4:
	cd tests;python3 treat_reverso.py -f samples/reverso/original/تصريف-العربية-الفعل-وَدَى.html -o out.txt
reverso:
	cd tests;python3 scrap_reverso.py -c generate -f samples/verbsmodels.csv -o output/text.html
eval:
	cd tests;python3 evalconjugate-2.py  -f samples/verbsmodels.csv  > output/eval.csv
eval2:
	cd tests;python2 evalconjugate-2.py  -f samples/verbsmodels.csv  > output/eval.csv
scrap_dal:
	cd tests;python3 scrap_reverso.py -c scrap-dal -f samples/verbsmodels.csv >  output/text.dal.html
	
