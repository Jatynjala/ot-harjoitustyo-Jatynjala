import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)
    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    def test_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)
    def test_saldo_kasvaa_oikein(self):
        plus=5
        self.maksukortti.lataa_rahaa(plus)
        self.assertEqual(self.maksukortti.saldo, 15)
    def test_saldo_vahenee_oikein(self):
        minus=5
        self.maksukortti.ota_rahaa(minus)
        self.assertEqual(self.maksukortti.saldo, 5)
    def test_saldo_ei_muutu(self):
        reduction=15
        self.maksukortti.ota_rahaa(reduction)
        self.assertEqual(self.maksukortti.saldo, 10)
    def test_ottaminen_palauttaa_True(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5), True)
    def test_ottaminen_palauttaa_False(self):
        self.assertEqual(self.maksukortti.ota_rahaa(15), False)
    def test_saldo_tulostuu_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
