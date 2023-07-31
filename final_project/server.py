from flask import Flask, render_template, request, jsonify
from translator import english_to_french, french_to_english

app = Flask("Web Translator")

@app.route("/englishToFrench")
def translate_to_french():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = english_to_french(text_to_translate)
    return jsonify({"translatedText": translated_text})

@app.route("/frenchToEnglish")
def translate_to_english():
    text_to_translate = request.args.get('textToTranslate')
    translated_text = french_to_english(text_to_translate)
    return jsonify({"translatedText": translated_text})

@app.route("/")
def render_index_page():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
