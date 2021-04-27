import unittest
from logiikka import Sovelluslogiikka

class TestSovelluslogiikka(unittest.TestCase):
    def setUp(self):
        self.logiikkaa = Sovelluslogiikka()
        self.tiedot = (1, "Mitä?", "A", "Oh yeah!", "Hmph!", 10, "B", "Jes!", "Äh!", 50, "C", "Hahaa", "GRRR!", 75)
    def test_luo_lista(self):
        testilista = self.logiikkaa.luo_lista(2, 5)
        self.assertEqual(len(testilista), 2)
    def test_aseta_voitto_eka(self):
        tulos = self.logiikkaa.aseta_voitto("1", self.tiedot)
        self.assertEqual(tulos, "Oh yeah!")
    def test_aseta_voitto_toka(self):
        tulos = self.logiikkaa.aseta_voitto("2", self.tiedot)
        self.assertEqual(tulos, "Jes!")
    def test_aseta_voitto_kolmas(self):
        tulos = self.logiikkaa.aseta_voitto("3", self.tiedot)
        self.assertEqual(tulos, "Hahaa")
    def test_aseta_tappio_eka(self):
        tulos = self.logiikkaa.aseta_tappio("1", self.tiedot)
        self.assertEqual(tulos, "Hmph!")
    def test_aseta_tappio_toka(self):
        tulos = self.logiikkaa.aseta_tappio("2", self.tiedot)
        self.assertEqual(tulos, "Äh!")
    def test_aseta_tappio_kolmas(self):
        tulos = self.logiikkaa.aseta_tappio("3", self.tiedot)
        self.assertEqual(tulos, "GRRR!")
    def test_aseta_todennakoisyys_eka(self):
        tulos = self.logiikkaa.aseta_todennakoisyys("1", self.tiedot)
        self.assertEqual(tulos, 10)
    def test_aseta_todennakoisyys_toka(self):
        tulos = self.logiikkaa.aseta_todennakoisyys("2", self.tiedot)
        self.assertEqual(tulos, 50)
    def test_aseta_todennakoisyys_kolmas(self):
        tulos = self.logiikkaa.aseta_todennakoisyys("3", self.tiedot)
        self.assertEqual(tulos, 75)
