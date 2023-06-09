import unittest
from translator import english_to_french, french_to_english

class testingTexts(unittest.TestCase):
    def test_ef(self):
        self.assertEqual(english_to_french('hello'), 'bonjour')
        self.assertNotEqual(english_to_french('hello'), 'hello')

    def test_fe(self):
        self.assertEqual(french_to_english('bonjour'), 'hello')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')
unittest.main()
