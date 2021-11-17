#! /usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import os.path
import re
from glob import glob
import logging
import logging.config
from datetime import datetime, timedelta
from flask import Flask, render_template, make_response, send_from_directory, request, jsonify, redirect
# ~ from flask_sitemap import Sitemap
from flask_minify import minify

# local libraries
sys.path.append(os.path.join(os.path.dirname(__file__), "./lib"))
sys.path.append(os.path.join(os.path.dirname(__file__), "../../"))
from config.qutrub_config import LOGGING_CFG_FILE
from config.qutrub_config import LOGGING_FILE
from config.qutrub_config import MODE_DEBUG
# ~ HOMEDOMAIN = "http://qutrub.arabeyes.org"
import qws_const
import core.adaat

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# set output logging in utf
import locale; 
if locale.getpreferredencoding().upper() != 'UTF-8': 
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8') 

# ~ logging.config.fileConfig(LOGGING_CFG_FILE,  disable_existing_loggers = False)
if MODE_DEBUG:
    logging.basicConfig(filename=LOGGING_FILE, level=logging.DEBUG)
else:
    logging.basicConfig(filename=LOGGING_FILE, level=logging.INFO) 

minify(app=app, html=True, js=True, cssless=True)



def str2bool(strg):
    if strg == "false":
        return False
    elif strg == "true":
        return True
    else:
        return strg
def prepare_result(resulttext, text, action, options, url="ajax"):
    """
    extract results from conjugator
    """
    
    if type(resulttext) == dict:
        suggestions = resulttext.get("suggest",[])
        results = {"result": resulttext.get("table",{}),
                "verb_info":resulttext.get("verb_info",""),
                 "suggest":suggestions}        
    else:
        app.logger.debug('No suggestion ', resulttext)
        suggestions = []
        results = {"result": {},
                "verb_info":"",
                 "suggest": []}  
    if not results.get("result",[]):
        invalid_verb = "invalid"
    else:
        invalid_verb = ""        
    # ~ suggestions = core.adaat.DoAction(text, "Suggest", options)
    app.logger.info('%s:%s:%s:%s', url, action, text, invalid_verb)
    logging.info('%s:%s:%s:%s',url, action, text, invalid_verb)
                     
    app.logger.debug('%s:%s'%("Suggest", repr(suggestions)))
    return results
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
    context = {
        'libraries':qws_const.libraries,
        'websites':qws_const.websites
    }
    return render_template("projects.html",current_page='projects',**context)


@app.route("/index/")
def index():
    return render_template("main.html",current_page='home')


@app.route("/")
def home():
    context = {}
    args = request.args
    context['verb']= args.get('verb', "")
    context['future_type']= args.get('haraka', "فتحة")
    context['transitive']= args.get('trans', False)

    return render_template("main.html",current_page='home',**context)

# ~ @app.route("/verb/<value>", methods=["POST", "GET"])

@app.route("/verb/<verb_value>/<haraka>/<trans>")
@app.route("/verb/<verb_value>/<haraka>")
@app.route("/verb/<verb_value>")
def verb(verb_value, haraka="فتحة", trans=False):
    context = {}
    context['verb']= verb_value
    context['future_type']= haraka
    context['transitive']= trans
    return redirect('/?verb=%s&haraka=%s&trans=%s'%(verb_value, haraka, trans))
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
    results = prepare_result(resulttext, text, action, options,"ajax")
    
    # ~ invalid_verb = ""
    # ~ if type(resulttext) == dict:
        # ~ suggestions = resulttext.get("suggest",[])
        # ~ results = {"result": resulttext.get("table",{}),
                # ~ "verb_info":resulttext.get("verb_info",""),
                 # ~ "suggest":suggestions}        
    # ~ else:
        # ~ app.logger.debug('No suggestion ', resulttext)
        # ~ suggestions = []
        # ~ results = {"result": {},
                # ~ "verb_info":"",
                 # ~ "suggest": []}  
    # ~ if not results.get("result",[]):
        # ~ invalid_verb = "invalid"
    #suggestions = core.adaat.DoAction(text, "Suggest", options)
    # ~ app.logger.info('%s:%s:%s', action, text, invalid_verb)
    # ~ logging.info('%s:%s:%s', action, text, invalid_verb)
    # ~ app.logger.debug('%s:%s',"Suggest", repr(suggestions))
    return jsonify(results)
    
    
@app.route("/api/<verb>/<haraka>", methods=["GET"])
@app.route("/api/<verb>", methods=["GET"])
@app.route("/api", methods=["GET"])
def api(text="", haraka=""):
    default = "استعمل"
    # ~ text = verb
    action = "Conjugate"
    options = {}
    if request.method == "GET":
        args = request.args
    else:
        return jsonify({"text": default})
    # Request a random text
    if args.get("response_type", "") == "get_random_text":
        return jsonify({"text": default})

    if not text : 
        text = args.get("verb", "")
        if not text:
            text = default
    if not haraka:
        haraka = args.get("haraka", u"فتحة")
        if haraka.lower() == "a":
            haraka = "فتحة"
        elif haraka.lower() == "u":
            haraka = "ضمة"
        elif haraka.lower() == "i":
            haraka = "كسرة"
        options["future_type"] = haraka
    
    trans = args.get("trans", True)
    if trans == "0":
        options["transitive"] = False
    else:
        options["transitive"] = True
    options["all"] = True    

    resulttext = core.adaat.DoAction(text, action, options)
    results = prepare_result(resulttext, text, action, options, url="api")
    # ~ if type(resulttext) == dict:
        # ~ suggestions = resulttext.get("suggest",[])
        # ~ results = {"result": resulttext.get("table",{}),
                # ~ "verb_info":resulttext.get("verb_info",""),
                 # ~ "suggest":suggestions}        
    # ~ else:
        # ~ app.logger.debug('No suggestion ', resulttext)
        # ~ suggestions = []
        # ~ results = {"result": {},
                # ~ "verb_info":"",
                 # ~ "suggest": []}  
    # ~ if not results.get("result",[]):
        # ~ invalid_verb = "invalid"
    # ~ else:
        # ~ invalid_verb = ""        
    ##suggestions = core.adaat.DoAction(text, "Suggest", options)
    # ~ app.logger.info('%s:%s:%s', action, text, invalid_verb)
    # ~ logging.info('%s:%s:%s', action, text, invalid_verb)
                     
    # ~ app.logger.debug('%s:%s'%("Suggest", repr(suggestions)))
    response = jsonify(results)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response
    


@app.route("/result", methods=["POST", "GET"])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("result.html", result=result)


@app.errorhandler(404)
def not_found(e):
    return render_template('404.shtml')


# ~ @app.route('/sitemap.xml', methods=['GET'])
# ~ def sitemap():
    # ~ try:
      # ~ """Generate sitemap.xml. Makes a list of urls and date modified."""
      # ~ ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # ~ verb_list = ["كتب",
      # ~ "سأل",
      # ~ "استعمل"]
      # ~ pages=[]
    
      # ~ ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # ~ # static pages
      # ~ for rule in app.url_map.iter_rules():
          # ~ if "GET" in rule.methods and len(rule.arguments)==0:
              # ~ pages.append(
                           # ~ {"loc":HOMEDOMAIN+str(rule.rule),
                           # ~ "lastmod":ten_days_ago,
                           # ~ }
                           # ~ )
      # ~ # dynamic pages
      # ~ for verb in verb_list:
          # ~ pages.append(
                        # ~ {"loc":HOMEDOMAIN+"/verb/"+verb,
                        # ~ "lastmod":ten_days_ago,
                        # ~ "prio":0.5,
                        # ~ "freq":"daily",
                          # ~ }
                       # ~ )

      # ~ sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      # ~ response= make_response(sitemap_xml)
      # ~ response.headers["Content-Type"] = "application/xml"    
    
      # ~ return response
    # ~ except Exception as e:
        # ~ return(str(e))  
@app.route('/sitemap.txt', methods=['GET'])
def sitemap_txt():
      return send_from_directory(app.static_folder, request.path[1:])

@app.route('/sitemap.xml', methods=['GET'])
def sitemap_xml():
      return send_from_directory(app.static_folder, request.path[1:])

# ~ @app.route('/sitemap.txt', methods=['GET'])
# ~ def sitemap_txt():
    # ~ try:
      # ~ """Generate sitemap.xml. Makes a list of urls and date modified."""
      # ~ verb_list = ["كتب",
      # ~ "سأل",
      # ~ "استعمل"]
      # ~ pages=[]
      # ~ # static pages
      # ~ for rule in app.url_map.iter_rules():
          # ~ if "GET" in rule.methods and len(rule.arguments)==0:
              # ~ pages.append(HOMEDOMAIN+str(rule.rule))
      # ~ # dynamic pages
      # ~ for verb in verb_list:
          # ~ pages.append(HOMEDOMAIN+"/verb/"+verb)

      # ~ sitemap_text = render_template('sitemap_template.txt', pages=pages)
      # ~ response= make_response(sitemap_text)
      # ~ response.headers["Content-Type"] = "text/text"    
    
      # ~ return response
    # ~ except Exception as e:
        # ~ return(str(e))  
        
if __name__ == "__main__":
    app.run(debug=True)
