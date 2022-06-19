from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_translation = translator.englishToFrench(textToTranslate)
    return french_translation

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_translation = translator.frenchToEnglish(textToTranslate)
    return english_translation

@app.route("/")
def renderIndexPage():
    pass
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

