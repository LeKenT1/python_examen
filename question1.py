import unittest

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

class TestEstPremier(unittest.TestCase):

    def test_nombres_premiers(self):
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertTrue(est_premier(5))
        self.assertTrue(est_premier(7))
        self.assertTrue(est_premier(11))

    def test_nombres_non_premiers(self):
        self.assertFalse(est_premier(1))
        self.assertFalse(est_premier(4))
        self.assertFalse(est_premier(6))
        self.assertFalse(est_premier(8))
        self.assertFalse(est_premier(9))
        self.assertFalse(est_premier(10))

    def test_nombre_grand(self):
        self.assertTrue(est_premier(9999991))

    def test_nombre_negatif(self):
        self.assertFalse(est_premier(-7))

if __name__ == '__main__':
    unittest.main()
