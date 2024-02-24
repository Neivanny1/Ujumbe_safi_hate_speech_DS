#!/usr/bin/python3
"""
Function to translate kiswahili to english
"""
from googletrans import Translator

def swahili_to_english(tweet):
    translator = Translator()
    translation = translator.translate(tweet, dest='en')
    return translation.text

"""
Testing
"""
translation = swahili_to_english('Leo nimechoka sana')
print(f'Translated Text: {translation}')
