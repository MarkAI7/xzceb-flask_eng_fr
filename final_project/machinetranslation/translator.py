"""
translator.py

This module provides functions for translating text between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French.

    Parameters:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated French text.
    """
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    french_text = translator.translate(english_text)
    print(french_text)	
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.

    Parameters:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated English text.
    """
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    english_text = translator.translate(french_text)
    print(english_text)
    return english_text
