import sys
import os.path
import re
import logging
import logging.config
from flask import Flask,request, jsonify, redirect
from flask_cors import CORS
import core.adaat
import qws_const

app = Flask(__name__)
CORS(app, resources={"*": {"origins": "*"}})
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

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

    app.logger.info('%s:%s:%s:%s', url, action, text, invalid_verb)
    logging.info('%s:%s:%s:%s',url, action, text, invalid_verb)

    app.logger.debug('%s:%s'%("Suggest", repr(suggestions)))
    return results

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
    response = jsonify(results)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response

@app.route("/projects/", methods=["GET"])
def projects():
    data = {
        'libraries': qws_const.libraries,
        'websites': qws_const.websites
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)
