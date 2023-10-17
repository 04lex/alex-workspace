import unittest
from palindrom import este_palindrom

class TestPalindrom(unittest.TestCase):


    ## VERIFICAM POZITIV
    def test_palindrom(self):
        self.assertTrue(este_palindrom("asa"))
        self.assertTrue(este_palindrom("caiac"))
        self.assertTrue(este_palindrom("elefaccafele"))


    ## VERIFICAM NEGATIV
    def test_nu_este_palindrom(self):
        self.assertFalse(este_palindrom("teren"))

    ## FALS NEGATIV 
    def test_palindrom_capitalizat(self):
        # in cazul in care codul de dezvoltare nu contine cuvant.lower(), testarea va trimite mesajul
        self.assertTrue(este_palindrom("Asa"), "Cuvantul este palindrom chiar daca incepe cu litera mare")
        self.assertTrue(este_palindrom("Caiac"))

    ## FALS POZITIV
    def test_palindrom_fals(self):
        self.assertFalse(este_palindrom("a"))
        self.assertFalse(este_palindrom(""))

        # self.assertFalse(este_palindrom("arra"))
       

if __name__ == "__main__":
    unittest.main()