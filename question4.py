import unittest

def somme_liste(liste):
    somme = 0
    for element in liste:
        somme += element
    return somme

class TestSommeListe(unittest.TestCase):

    def test_liste_vide(self):
        self.assertEqual(somme_liste([]), 0)

    def test_liste_un_element(self):
        self.assertEqual(somme_liste([5]), 5)

    def test_liste_plusieurs_elements(self):
        self.assertEqual(somme_liste([1, 2, 3, 4, 5]), 15)

    def test_liste_negatifs(self):
        self.assertEqual(somme_liste([-1, -2, -3, -4, -5]), -15)

    def test_melange_positifs_et_negatifs(self):
        self.assertEqual(somme_liste([1, -2, 3, -4, 5]), 3)

if __name__ == '__main__':
    unittest.main()
