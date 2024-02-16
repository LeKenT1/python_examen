import unittest

def est_palindrome(chaine):
    chaine = chaine.lower().replace(" ", "")
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse

class TestEstPalindrome(unittest.TestCase):

    def test_palindrome_simple(self):
        self.assertTrue(est_palindrome("Engage le jeu que je le gagne"))

    def test_palindrome_avec_espaces(self):
        self.assertTrue(est_palindrome("Esope reste ici et se repose"))

    def test_non_palindrome(self):
        self.assertFalse(est_palindrome("python"))

    def test_palindrome_avec_majuscules(self):
        self.assertTrue(est_palindrome("Elu par cette crapule"))

    def test_palindrome_vide(self):
        self.assertTrue(est_palindrome(""))

if __name__ == '__main__':
    unittest.main()
