def compter_mots(phrase):
    if not phrase:
        return 0
    mots = phrase.split()
    return len(mots)

import unittest

class TestCompterMots(unittest.TestCase):

    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)

    def test_une_seule_mot(self):
        self.assertEqual(compter_mots("Bonjour"), 1)

    def test_plusieurs_mots(self):
        self.assertEqual(compter_mots("Ceci est un test"), 4)

    def test_espaces_supplementaires(self):
        self.assertEqual(compter_mots("   Ceci   est   un   test   "), 4)

if __name__ == '__main__':
    unittest.main()
