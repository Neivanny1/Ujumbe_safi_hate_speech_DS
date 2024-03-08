#!/usr/bin/python3
"""
Function to translate kiswahili to english
"""
from googletrans import Translator

def swahili_to_english(tweet):
    translator = Translator()
    translation = translator.translate(tweet, dest='en')
    print(type(translation.text))
    return translation.text

"""
Testing
"""
translation = swahili_to_english('uyu mtoto ni malaya')
print(f'Translated Text: {translation}')
print(type(translation))