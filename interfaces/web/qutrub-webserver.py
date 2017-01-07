#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os.path
import re
from glob import glob
#~ sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../support/'))
#sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../mishkal/lib/'))
#~ sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../mishkal'))
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), './lib'))
sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), '../../'))

import core.adaat
example_json = {"result": {"0": {"0": u"الضمائر", u"1": u"الماضي المعلوم", u"2": u"المضارع المعلوم", u"3": u"المضارع المجزوم", u"4": u"المضارع المنصوب", u"5": u"المضارع المؤكد الثقيل", u"6": u"الأمر", u"7": u"الأمر المؤكد", u"8": u"الماضي المجهول", u"9": u"المضارع المجهول", u"10": u"المضارع المجهول المجزوم", u"11": u"المضارع المجهول الم نصوب", u"12": u"المضارع المؤكد الثقيل المجهول u"}, u"1": {"0": u"أنا", u"1 u": u"قَاوَمْتُ", u"2": u"أُقَاوِمُ" , u"3": u"أُقَاوِمْ", u"4": u"أُقَاوِمَ", u"5": u"أُقَاوِمَنَّ", u"6": u"", u"7":"", u"8": u"قُووِمْتُ", u"9": u" أُقَاوَمُ", u"10": u"أُقَاوَمْ", u"11": u" أُقَاوَمَ", u"12": u"أُقَاوَمَنَّ"}, u"2": {"0": u"نحن", u"1": u"قَا وَمْنَا", u"2": u" نُقَاوِمُ", u"3": u"نُقَاوِمْ", u"4": u"نُقَاوِمَ", u"5": u"نُقَاوِمَنَّ", u"6": u"", u"7": u"" , u"8": u"قُووِمْنَا", u"9": u"نُقَاوَمُ", u"10": u"نُقَاوَمْ", u"11": u"نُقَاوَمَ", u"12": u"نُقَاوَمَنَّ"}, u"3" : {"0": u"أنت", u"1": u"قَاوَمْتَ", u"2": u"تُقَاوِمُ", u"3": u"تُقَاوِمْ", u"4": u"تُقَاوِمَ", u"5": u"تُقَاوِ مَنَّ", u"6": u"قَاوِمْ", u"7": u"قَاوِمَنَّ", u"8 u": u"قُووِمْتَ", u"9": u"تُقَاوَمُ", u"10": u"تُقَاوَمْ", u"11" : u"تُقَاوَمَ", u"12": u"تُقَاوَمَنَّ"}, u"4": {"0": u"أنتِ", u"1": u"قَاوَمْتِ", u"2": u"تُقَاوِمِينَ", u"3": u"تُقَاوِمِي", u"4": u"تُقَاوِمِي", u"5": u"تُقَاوِمِنَّ", u"6": u"قَاوِمِي", u"7": u"قَاوِمِنَّ", u"8": u"قُو وِمْتِ", u"9": u"تُقَاوَمِينَ", u"10": u"تُقَاوَمِي", u"11": u"تُقَاوَمِي", u"12": u" تُقَاوَمِنَّ"}, u"5": {"0" : u"أنتما", u"1": u"قَاوَمْتُمَا", u"2": u"تُقَاوِمَانِ", u"3": u"تُقَاوِمَا", u"4": u"تُقَاوِمَا", u"5": u"تُق َاوِمَانِّ", u"6": u"قَاوِمَا", u"7": u"قَاوِمَانِّ u", u"8": u"قُووِمْتُمَا", u"9": u"تُقَاوَمَانِ", u"10": u"ت ُقَاوَمَا", u"11": u"تُقَاوَمَا", u" 12": u"تُقَاوَمَانِّ"}, u"6": {"0": u"أنتما مؤ", u"1": u"قَاوَمْتُمَا", u"2" : u"تُقَاوِمَانِ", u"3": u"تُقَاوِمَا", u"4": u"تُقَاوِمَا", u"5": u"تُقَاوِمَانِّ", u"6": u"قَاوِمَا" , u"7": u" قَاوِمَانِّ", u"8": u"قُووِمْتُمَا", u"9": u"تُقَاوَمَانِ", u"10": u"تُقَاوَمَا", u" 11 u": u"تُقَاوَمَا", u"12" : u"تُقَاوَمَانِّ"}, u"7": {"0": u"أنتم", u"1": u"قَاوَمْتُم", u"2" : u"تُقَاوِمُونَ", u"3": u"تُقَاوِمُوا", u"4" : u"تُقَاوِمُوا", u"5": u"تُقَاوِمُنَّ", u"6": u"قَاوِمُوا", u"7": u"قَاوِمُنَّ", u"8": u"قُووِمْتُم", u"9": u" تُقَاوَمُونَ", u"10": u" تُقَاوَمُوا", u"11": u"تُقَاوَمُوا", u"12": u"تُقَاوَمُنَّ"}, u"8": {"0": u"أنتن", u"1" : u"قَاوَمْتُنَّ", u"2": u"تُقَاوِمْنَ", u"3": u"تُقَاوِمْنَ", u"4": u"تُقَاوِمْنَ", u"5": u"تُقَاوِمْنَانِّ" , u"6": u"قَاوِمْنَ", u"7": u"قَاوِمْنَانِّ", u"8": u"قُووِمْتُنَّ", u"9": u"تُقَاوَمْنَ", u"10": u"تُقَاوَمْن َ", u"11": u"تُقَاوَمْنَ", u"12": u"تُقَاوَمْنَانِّ"}, u"9": {" 0": u"هو", u"1": u"قَاوَمَ", u"2": u"يُقَاوِمُ" , u"3": u"يُقَاوِمْ", u"4": u"يُقَاوِمَ", u"5" : u"يُقَاوِمَنَّ", u"6": u"", u"7": u"", u"8": u"قُووِمَ", u"9": u"ي ُقَاوَمُ", u"10": u" يُقَاوَمْ", u"11": u"يُقَاوَمَ", u"12": u"يُقَاوَمَنَّ"}, u"10": {"0": u"هي", u"1": u"قَاو َمَتْ", u"2": u"تُقَاوِمُ", u"3": u"تُقَاوِمْ", u"4": u"تُقَاوِمَ", u"5": u"تُقَاوِمَنَّ", u"6 u": u"", u"7": u"", u"8": u"قُووِمَتْ", u"9": u"تُقَاوَمُ", u"10": u"تُقَاوَمْ", u"11": u"تُقَاوَمَ", u"12": u"تُقَاوَمَنَّ"}, u"11" : {"0": u"هما", u"1": u"قَاوَمَا", u"2": u"يُقَاوِمَانِ", u"3": u"يُقَاوِمَا", u"4": u"يُقَاوِمَا", u"5": u"يُق َاوِمَانِّ", u"6": u"", u"7 u": u"", u"8": u"قُووِمَا", u"9": u"يُقَاوَمَانِ", u"10": u"يُقَاوَمَا", u"11": u"يُقَ اوَمَا u", u"12": u"يُقَاوَمَانِّ"}, u"12": {"0": u"هما مؤ", u"1": u"قَاوَمَتَا", u"2": u" تُقَاوِمَانِ", u"3": u" تُقَاوِمَا", u"4": u"تُقَاوِمَا", u"5": u"تُقَاوِمَانِّ", u"6": u"", u"7 u": u"", u"8": u"قُووِمَتَا", u"9": u"تُق َاوَمَانِ", u"10": u"تُقَاوَمَا", u"11": u"تُقَاوَمَا u", u"12": u"تُقَاوَمَانِّ"}, u"13": {"0": u"هم", u"1": u" قَاوَمُوا", u"2": u"يُقَاوِمُونَ u", u"3": u"يُقَاوِمُوا", u"4": u"يُقَاوِمُوا", u"5": u"يُقَاوِمُنَّ", u"6": u"" , u"7": u"", u"8": u"قُووِمُوا", u"9": u"يُقَاوَمُونَ", u"10": u"يُقَاوَمُوا", u"11": u"يُقَاوَمُوا", u"12" : u"ي ُقَاوَمُنَّ"}, u"14": {"0": u"هن", u"1": u"قَاوَمْنَ", u"2": u"يُقَاوِمْنَ", u"3": u" يُقَاوِمْنَ", u"4": u"يُق َاوِمْنَ", u"5": u"يُقَاوِمْنَانِّ", u"6": u"", u"7": u"", u"8": u" قُووِمْنَ", u"9": u"يُقَاوَمْنَ", u"10": u"يُ قَاوَمْنَ", u"11": u"يُقَاوَمْنَ", u"12": u" يُقَاوَمْنَانِّ"}}, u"order": u"0"}


from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
def str2bool(strg):
    if strg == "false":
        return False;
    elif strg == "true":
        return True;
    else:
        return strg
@app.route('/doc/')
def doc():
    return render_template('doc.html')
@app.route('/contact/')
def contact():
    return render_template('contact.html')
@app.route('/download/')
def download():
    return render_template('download.html')
@app.route('/projects/')
def projects():
    return render_template('projects.html')
@app.route('/index/')
def index():
    return render_template('main.html')
@app.route('/')
def student():
    DefaultText = "Text"#core.adaat.random_text(),
    ResultText  = u"السلام عليكم"
    return render_template('main.html', DefaultText = DefaultText, ResultText=ResultText)
    
@app.route('/ajaxGet', methods = ['POST', 'GET'])
def ajax():
    default = core.adaat.random_text()
    resulttext = u"السلام عليكم"
    text = default
    action = ""
    options= {}    
    if request.method == 'GET':
        args = request.args
        print args
        text   = request.args.get('text', "")
        action = request.args.get('action', '')
        options['all'] = str2bool(request.args.get('all', False))
        options['past'] = str2bool(request.args.get('past', False))
        options['transitive'] = str2bool(request.args.get('transitive', False))
        options['future'] = str2bool(request.args.get('future', False))
        options['imperative'] = str2bool(request.args.get('imperative', False))
        options['future_moode'] = str2bool(request.args.get('future_moode', False))
        options['confirmed'] = str2bool(request.args.get('confirmed', False))

        options['passive'] = str2bool(request.args.get('passive', False))
        options['past'] = str2bool(request.args.get('past', False))
        options['future_type'] = request.args.get('future_type', u"فتحة")        
        options['display_format'] = request.args.get('display_format',"HTML")
        print options
        print request.form
        #~ resulttext = text + action
        resulttext=core.adaat.DoAction(text,action, options)
    return jsonify({'result':resulttext,})
    #~ return jsonify(example_json)

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run(debug = True)


