#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os.path
import re
from glob import glob
import logging.config
from datetime import datetime, timedelta
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))

import core.adaat
from config.qutrub_config import LOGGING_CFG_FILE
from config.qutrub_config import LOGGING_FILE
HOMEDOMAIN = "http://qutrub.arabeyes.org"
example_json = {
    "result": {
        "0": {
            "0": u"الضمائر",
            u"1": u"الماضي المعلوم",
            u"2": u"المضارع المعلوم",
            u"3": u"المضارع المجزوم",
            u"4": u"المضارع المنصوب",
            u"5": u"المضارع المؤكد الثقيل",
            u"6": u"الأمر",
            u"7": u"الأمر المؤكد",
            u"8": u"الماضي المجهول",
            u"9": u"المضارع المجهول",
            u"10": u"المضارع المجهول المجزوم",
            u"11": u"المضارع المجهول الم نصوب",
            u"12": u"المضارع المؤكد الثقيل المجهول",
        },
        u"1": {
            "0": u"أنا",
            u"1 u": u"قَاوَمْتُ",
            u"2": u"أُقَاوِمُ",
            u"3": u"أُقَاوِمْ",
            u"4": u"أُقَاوِمَ",
            u"5": u"أُقَاوِمَنَّ",
            u"6": u"",
            u"7": "",
            u"8": u"قُووِمْتُ",
            u"9": u" أُقَاوَمُ",
            u"10": u"أُقَاوَمْ",
            u"11": u" أُقَاوَمَ",
            u"12": u"أُقَاوَمَنَّ",
        },
        u"2": {
            "0": u"نحن",
            u"1": u"قَا وَمْنَا",
            u"2": u" نُقَاوِمُ",
            u"3": u"نُقَاوِمْ",
            u"4": u"نُقَاوِمَ",
            u"5": u"نُقَاوِمَنَّ",
            u"6": u"",
            u"7": u"",
            u"8": u"قُووِمْنَا",
            u"9": u"نُقَاوَمُ",
            u"10": u"نُقَاوَمْ",
            u"11": u"نُقَاوَمَ",
            u"12": u"نُقَاوَمَنَّ",
        },
        u"3": {
            "0": u"أنت",
            u"1": u"قَاوَمْتَ",
            u"2": u"تُقَاوِمُ",
            u"3": u"تُقَاوِمْ",
            u"4": u"تُقَاوِمَ",
            u"5": u"تُقَاوِ مَنَّ",
            u"6": u"قَاوِمْ",
            u"7": u"قَاوِمَنَّ",
            u"8": u"قُووِمْتَ",
            u"9": u"تُقَاوَمُ",
            u"10": u"تُقَاوَمْ",
            u"11": u"تُقَاوَمَ",
            u"12": u"تُقَاوَمَنَّ",
        },
        u"4": {
            u"0": u"أنتِ",
            u"1": u"قَاوَمْتِ",
            u"2": u"تُقَاوِمِينَ",
            u"3": u"تُقَاوِمِي",
            u"4": u"تُقَاوِمِي",
            u"5": u"تُقَاوِمِنَّ",
            u"6": u"قَاوِمِي",
            u"7": u"قَاوِمِنَّ",
            u"8": u"قُو وِمْتِ",
            u"9": u"تُقَاوَمِينَ",
            u"10": u"تُقَاوَمِي",
            u"11": u"تُقَاوَمِي",
            u"12": u" تُقَاوَمِنَّ",
        },
        u"5": {
            u"0": u"أنتما",
            u"1": u"قَاوَمْتُمَا",
            u"2": u"تُقَاوِمَانِ",
            u"3": u"تُقَاوِمَا",
            u"4": u"تُقَاوِمَا",
            u"5": u"تُق َاوِمَانِّ",
            u"6": u"قَاوِمَا",
            u"7": u"قَاوِمَانِّ u",
            u"8": u"قُووِمْتُمَا",
            u"9": u"تُقَاوَمَانِ",
            u"10": u"ت ُقَاوَمَا",
            u"11": u"تُقَاوَمَا",
            u"12": u"تُقَاوَمَانِّ",
        },
        u"6": {
            "0": u"أنتما مؤ",
            u"1": u"قَاوَمْتُمَا",
            u"2": u"تُقَاوِمَانِ",
            u"3": u"تُقَاوِمَا",
            u"4": u"تُقَاوِمَا",
            u"5": u"تُقَاوِمَانِّ",
            u"6": u"قَاوِمَا",
            u"7": u" قَاوِمَانِّ",
            u"8": u"قُووِمْتُمَا",
            u"9": u"تُقَاوَمَانِ",
            u"10": u"تُقَاوَمَا",
            u"11": u"تُقَاوَمَا",
            u"12": u"تُقَاوَمَانِّ",
        },
        u"7": {
            u"0": u"أنتم",
            u"1": u"قَاوَمْتُم",
            u"2": u"تُقَاوِمُونَ",
            u"3": u"تُقَاوِمُوا",
            u"4": u"تُقَاوِمُوا",
            u"5": u"تُقَاوِمُنَّ",
            u"6": u"قَاوِمُوا",
            u"7": u"قَاوِمُنَّ",
            u"8": u"قُووِمْتُم",
            u"9": u" تُقَاوَمُونَ",
            u"10": u" تُقَاوَمُوا",
            u"11": u"تُقَاوَمُوا",
            u"12": u"تُقَاوَمُنَّ",
        },
        u"8": {
            u"0": u"أنتن",
            u"1": u"قَاوَمْتُنَّ",
            u"2": u"تُقَاوِمْنَ",
            u"3": u"تُقَاوِمْنَ",
            u"4": u"تُقَاوِمْنَ",
            u"5": u"تُقَاوِمْنَانِّ",
            u"6": u"قَاوِمْنَ",
            u"7": u"قَاوِمْنَانِّ",
            u"8": u"قُووِمْتُنَّ",
            u"9": u"تُقَاوَمْنَ",
            u"10": u"تُقَاوَمْن َ",
            u"11": u"تُقَاوَمْنَ",
            u"12": u"تُقَاوَمْنَانِّ",
        },
        u"9": {
            u"0": u"هو",
            u"1": u"قَاوَمَ",
            u"2": u"يُقَاوِمُ",
            u"3": u"يُقَاوِمْ",
            u"4": u"يُقَاوِمَ",
            u"5": u"يُقَاوِمَنَّ",
            u"6": u"",
            u"7": u"",
            u"8": u"قُووِمَ",
            u"9": u"ي ُقَاوَمُ",
            u"10": u" يُقَاوَمْ",
            u"11": u"يُقَاوَمَ",
            u"12": u"يُقَاوَمَنَّ",
        },
        u"10": {
            u"0": u"هي",
            u"1": u"قَاو َمَتْ",
            u"2": u"تُقَاوِمُ",
            u"3": u"تُقَاوِمْ",
            u"4": u"تُقَاوِمَ",
            u"5": u"تُقَاوِمَنَّ",
            u"6": u"",
            u"7": u"",
            u"8": u"قُووِمَتْ",
            u"9": u"تُقَاوَمُ",
            u"10": u"تُقَاوَمْ",
            u"11": u"تُقَاوَمَ",
            u"12": u"تُقَاوَمَنَّ",
        },
        u"11": {
            u"0": u"هما",
            u"1": u"قَاوَمَا",
            u"2": u"يُقَاوِمَانِ",
            u"3": u"يُقَاوِمَا",
            u"4": u"يُقَاوِمَا",
            u"5": u"يُق َاوِمَانِّ",
            u"6": u"",
            u"7 u": u"",
            u"8": u"قُووِمَا",
            u"9": u"يُقَاوَمَانِ",
            u"10": u"يُقَاوَمَا",
            u"11": u"يُقَ اوَمَا u",
            u"12": u"يُقَاوَمَانِّ",
        },
        u"12": {
            u"0": u"هما مؤ",
            u"1": u"قَاوَمَتَا",
            u"2": u" تُقَاوِمَانِ",
            u"3": u" تُقَاوِمَا",
            u"4": u"تُقَاوِمَا",
            u"5": u"تُقَاوِمَانِّ",
            u"6": u"",
            u"7 u": u"",
            u"8": u"قُووِمَتَا",
            u"9": u"تُق َاوَمَانِ",
            u"10": u"تُقَاوَمَا",
            u"11": u"تُقَاوَمَا u",
            u"12": u"تُقَاوَمَانِّ",
        },
        u"13": {
            u"0": u"هم",
            u"1": u" قَاوَمُوا",
            u"2": u"يُقَاوِمُونَ u",
            u"3": u"يُقَاوِمُوا",
            u"4": u"يُقَاوِمُوا",
            u"5": u"يُقَاوِمُنَّ",
            u"6": u"",
            u"7": u"",
            u"8": u"قُووِمُوا",
            u"9": u"يُقَاوَمُونَ",
            u"10": u"يُقَاوَمُوا",
            u"11": u"يُقَاوَمُوا",
            u"12": u"ي ُقَاوَمُنَّ",
        },
        u"14": {
            u"0": u"هن",
            u"1": u"قَاوَمْنَ",
            u"2": u"يُقَاوِمْنَ",
            u"3": u" يُقَاوِمْنَ",
            u"4": u"يُق َاوِمْنَ",
            u"5": u"يُقَاوِمْنَانِّ",
            u"6": u"",
            u"7": u"",
            u"8": u" قُووِمْنَ",
            u"9": u"يُقَاوَمْنَ",
            u"10": u"يُ قَاوَمْنَ",
            u"11": u"يُقَاوَمْنَ",
            u"12": u" يُقَاوَمْنَانِّ",
        },
    },
    u"order": u"0",
}


from flask import Flask, render_template, make_response, request, jsonify, redirect
from flask_sitemap import Sitemap
from flask_minify import minify


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# ~ ext = Sitemap(app=app)

# ~ logging.config.fileConfig(LOGGING_CFG_FILE,  disable_existing_loggers = False)
logging.basicConfig(filename=LOGGING_FILE, level=logging.DEBUG)

minify(app=app, html=True, js=True, cssless=True)


def str2bool(strg):
    if strg == "false":
        return False
    elif strg == "true":
        return True
    else:
        return strg


@app.route("/doc/")
def doc():
    return render_template("doc.html",current_page='doc')


@app.route("/contact/")
def contact():
    return render_template("contact.html",current_page='contact')


@app.route("/download/")
def download():
    return render_template("download.html",current_page='download')


@app.route("/projects/")
def projects():
    return render_template("projects.html",current_page='projects')


@app.route("/index/")
def index():
    return render_template("main.html",current_page='home')


@app.route("/")
def home():
    context = {}
    args = request.args
    if args.get('verb'):
        context['verb']= args.get('verb')

    return render_template("main.html",current_page='home',**context)

# ~ @app.route("/verb/<value>", methods=["POST", "GET"])

@app.route("/verb/<verb_value>")
def verb(verb_value):
    context = {}
    context['verb']= verb_value
    return redirect('/?verb=%s'%verb_value)
    # ~ return render_template("main.html",current_page='verb',**context)


@app.route("/ajaxGet", methods=["POST", "GET"])
def ajax():
    default = core.adaat.random_text()
    resulttext = u"السلام عليكم"
    text = default
    action = ""
    options = {}
    if request.method == "GET":
        args = request.args
    elif request.method == "POST":
        args = request.get_json(silent=True)["data"]
    else:
        return jsonify({"text": default})
    # Request a random text
    if args.get("response_type", "") == "get_random_text":
        return jsonify({"text": default})

    text = args.get("text", "")
    action = args.get("action", "")
    options["all"] = args.get("all", False)
    options["transitive"] = args.get("transitive", False)

    options["past"] = args.get("past", False)
    options["future"] = args.get("future", False)
    options["imperative"] = args.get("imperative", False)
    options["future_moode"] = args.get("future_moode", False)
    options["confirmed"] = args.get("confirmed", False)

    options["passive"] = args.get("passive", False)
    options["past"] = args.get("past", False)
    options["future_type"] = args.get("future_type", u"فتحة")

    options["display_format"] = args.get("display_format", "HTML")

    resulttext = core.adaat.DoAction(text, action, options)
        
    suggestions = resulttext.get("suggest","")
    # ~ suggestions = core.adaat.DoAction(text, "Suggest", options)
    app.logger.info('%s:%s'%(action, text))
    app.logger.info('%s:%s'%("Suggest", repr(suggestions)))
    return jsonify({"result": resulttext.get("table",{}),"verb_info":resulttext.get("verb_info",""), "suggest":suggestions})
    # ~ return jsonify({"result": resulttext.get("table",{}),"verb_info":resulttext.get("verb_info",""), "suggest":resulttext.get("suggest","")})


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result=result)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.shtml')


@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      verb_list = ["كتب",
      "سأل",
      "استعمل"]
      pages=[]
    
      ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # static pages
      for rule in app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(
                           {"loc":HOMEDOMAIN+str(rule.rule),
                           "lastmod":ten_days_ago,
                           }
                           )
      # dynamic pages
      for verb in verb_list:
          pages.append(
                        {"loc":HOMEDOMAIN+"/verb/"+verb,
                        "lastmod":ten_days_ago,
                        "prio":0.5,
                        "freq":"daily",
                          }
                       )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"    
    
      return response
    except Exception as e:
        return(str(e))  
@app.route('/sitemap.txt', methods=['GET'])
def sitemap_txt():
    try:
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      verb_list = ["كتب",
      "سأل",
      "استعمل"]
      pages=[]
      # static pages
      for rule in app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(HOMEDOMAIN+str(rule.rule))
      # dynamic pages
      for verb in verb_list:
          pages.append(HOMEDOMAIN+"/verb/"+verb)

      sitemap_text = render_template('sitemap_template.txt', pages=pages)
      response= make_response(sitemap_text)
      response.headers["Content-Type"] = "text/text"    
    
      return response
    except Exception as e:
        return(str(e))  
        
if __name__ == "__main__":
    app.run(debug=True)
