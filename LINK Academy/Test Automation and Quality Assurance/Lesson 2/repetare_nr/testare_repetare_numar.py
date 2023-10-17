import unittest
from repetare_numar import cel_mai_des_numar


class TestExemplu(unittest.TestCase):
    def test_exemplu(self):
        assert True

    def test_exemplu_2(self):
        self.assertEqual(2, 2)

    def test_exemplu_3(self):
        self.assertTrue(9 == 9)
        self.assertTrue(100 == 100)



class TestRepetare(unittest.TestCase):
    
    def test_cel_mai_des(self):
        self.assertEqual(cel_mai_des_numar([1, 1, 1, 2, 2, 3]), 1)
        self.assertEqual(cel_mai_des_numar([1, 1, 2, 2, 2, 3]), 2)

        self.assertNotEqual(cel_mai_des_numar([1, 1, 2, 2, 2, 3]), 1)
        self.assertNotEqual(cel_mai_des_numar([1, 1, 2, 2, 2, 3]), 0)

    def test_doua_numere_dese(self):
        self.assertIn(2, cel_mai_des_numar([1, 1, 2, 2, 3]))
        self.assertIn(1, cel_mai_des_numar([1, 1, 2, 2, 3]))
        self.assertNotIn(3, cel_mai_des_numar([1, 1, 2, 2, 3]))

    def test_stringuri(self):
        self.assertNotEqual(cel_mai_des_numar(["1", "1", "1", "2", "2", "2", "3"]), 1)


if __name__ == "__main__":
    unittest.main()