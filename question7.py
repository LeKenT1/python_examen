import unittest

def calculer_moyenne(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)

class TestCalculerMoyenne(unittest.TestCase):

    def test_liste_non_vide(self):
        self.assertEqual(calculer_moyenne([1, 2, 3, 4, 5]), 3)

    def test_liste_vide(self):
        self.assertEqual(calculer_moyenne([]), 0)

    def test_liste_un_element(self):
        self.assertEqual(calculer_moyenne([5]), 5)

    def test_liste_negatifs(self):
        self.assertEqual(calculer_moyenne([-1, -2, -3, -4, -5]), -3)

    def test_liste_decimaux(self):
        self.assertAlmostEqual(calculer_moyenne([1.5, 2.5, 3.5, 4.5, 5.5]), 3.5)

if __name__ == '__main__':
    unittest.main()
