"""Module for translating french text to english and vice versa
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    """Function for translating english text to french
    """
    translation = language_translator.translate(
            text=englishText,
            model_id='en-fr').get_result()
    frenchText = translation["translations"][0].get("translation")
    return frenchText

def frenchToEnglish(frenchText):
    """Function for translating french text to english
    """
    translation = language_translator.translate(
            text=frenchText,
            model_id='fr-en').get_result()
    englishText = translation["translations"][0].get("translation")
    return englishText
