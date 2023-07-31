import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrenchTranslation(unittest.TestCase):
    def test_hello_translation(self):
        english_text = "Hello"
        expected_french_text = "Bonjour"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_bonjour_translation(self):
        english_text = "Bonjour"
        expected_french_text = "Hello"
        translated_text = english_to_french(english_text)
        self.assertNotEqual(translated_text, expected_french_text)

class TestFrenchToEnglishTranslation(unittest.TestCase):
    def test_bonjour_translation(self):
        french_text = "Bonjour"
        expected_english_text = "Hi"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

    def test_hello_translation(self):
        french_text = "Hi"
        expected_english_text = "Bonjour"
        translated_text = french_to_english(french_text)
        self.assertNotEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
