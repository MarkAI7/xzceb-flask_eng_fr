from flask import jsonify

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = english_to_french(textToTranslate)
    return jsonify({"translatedText": translated_text})

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    translated_text = french_to_english(textToTranslate)
    return jsonify({"translatedText": translated_text})
