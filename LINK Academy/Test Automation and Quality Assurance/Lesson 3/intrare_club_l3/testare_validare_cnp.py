import unittest
from validare_cnp import are_voie_in_club, este_cnp_valid
import datetime

'''
Problemă: La intrarea în clubul de noapte local este instalat un
cititor de cărţi de identitate. Scopul unui astfel de dispozitiv este
de a verifica vârsta persoanei care doreşte să intre în club.
Persoanelor de sex masculin cu vârsta sub 18 ani şi femeilor sub
vârsta de 16 ani li se interzice intrarea în club, precum şi tuturor
persoanelor cu vârsta de peste 70 de ani (exemplul cu vârsta este
exclusiv ipotetic, folosit pentru scopurile acestui exerciţiu).
• Trebuie să se creeze un algoritm pe baza căruia cititorul cărţii de
identitate ar determina cine are voie să intre în club şi cine nu.
'''

class TestValidareCNP(unittest.TestCase):
    
    # def test_este_cnp_valid(self):
    #     self.assertTrue(are_voie_in_club("1234567890123"))

    ### Numar de cifre
    def test_are_13_cifre(self):
        self.assertTrue(este_cnp_valid("1640504290976"))

        self.assertFalse(este_cnp_valid("164050429097"))

        self.assertFalse(este_cnp_valid("164050429097698"))

    ### FARA alte caractere *&^%$@!

    def test_are_doar_cifre(self):
        self.assertTrue(este_cnp_valid("1640504290976"))

        self.assertFalse(este_cnp_valid("164050429097*"))

        self.assertFalse(este_cnp_valid("164050429097A"))

        self.assertFalse(este_cnp_valid("164050429097A "))

        self.assertFalse(este_cnp_valid("1640-50429097 "))

    ### (Prima) Cifra cu care incepe

    def test_prima_cifra(self):
        ## POZITIV
        self.assertTrue(este_cnp_valid("1640504290976"))
        self.assertTrue(este_cnp_valid("2640504290976"))
        self.assertTrue(este_cnp_valid("5040504290976"))
        self.assertTrue(este_cnp_valid("6040504290976"))


        ## NEGATIV
        self.assertFalse(este_cnp_valid("3640504290976"))
        self.assertFalse(este_cnp_valid("4640504290976"))
        self.assertFalse(este_cnp_valid("7040504290976"))
        self.assertFalse(este_cnp_valid("8040504290976"))
        self.assertFalse(este_cnp_valid("9040504290976"))
        self.assertFalse(este_cnp_valid("0040504290976"))


    ### An

    def test_are_minim_14_ani(self):
        self.assertFalse(este_cnp_valid("5340504290976"))
        self.assertFalse(este_cnp_valid("6340504290976"))

        self.assertFalse(este_cnp_valid("5190504290976"))
        self.assertFalse(este_cnp_valid("6190504290976"))


    ### Luna
    def test_luna_valida(self):
        self.assertFalse(este_cnp_valid("1641504290976"))
        self.assertFalse(este_cnp_valid("2640004290976"))
        self.assertFalse(este_cnp_valid("5041304290976"))
        self.assertFalse(este_cnp_valid("6049504290976"))


    ### Ziua

    def test_zi_valida(self):
        self.assertFalse(este_cnp_valid("1641534290976"))
        self.assertFalse(este_cnp_valid("2640000290976"))
        self.assertFalse(este_cnp_valid("5041332290976"))
        self.assertFalse(este_cnp_valid("6049590290976"))

    ### 31 Apr, Iunie, Sept, Noiembrie
    def test_zile_de_30(self):
        self.assertFalse(este_cnp_valid("2640431290976"))
        self.assertFalse(este_cnp_valid("2640631290976"))
        self.assertFalse(este_cnp_valid("2640931290976"))
        self.assertFalse(este_cnp_valid("2641131290976"))

    ### ULTIMA CIFRA - TEMA

class TestVerificareAcces(unittest.TestCase):
    def setUp(self):
        self.current_year = datetime.datetime.now().year


    def test_au_acces(self):
        self.assertTrue(are_voie_in_club("5001230290976"))
        self.assertTrue(are_voie_in_club("6000909029097"))


    def test_nu_au_acces(self):
        self.assertFalse(are_voie_in_club("5080331290976"))
        self.assertFalse(are_voie_in_club("6080509290976"))


    
    def test_baieti_sub_18(self):
        test_year = self.current_year - 17
        ### ACEST TEST VA MERGE TOT TIMPUL
        self.assertFalse(are_voie_in_club(f"5{test_year}0331290976"))
        ### ACEST TEST NU VA MAI MERGE IN 2024!!!!!!!!
        self.assertFalse(are_voie_in_club("5060331290976"))


if __name__ == "__main__":
    unittest.main()