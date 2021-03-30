import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate=Kassapaate()
    #Luotu kassapaate
    def test_alkumaara_rahaa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_edullisten_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_maukkaiden_lounaiden_maara_alussa_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
    #kateismaksut raha riittaa
    def test_kateinen_riittaa_edulliseen_raha_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    def test_kateinen_riittaa_edulliseen_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)
    def test_kateinen_riittaa_edulliseen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)
    def test_kateinen_riittaa_maukkaaseen_raha_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
    def test_kateinen_riittaa_maukkaaseen_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    def test_kateinen_riittaa_maukkaaseen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(460), 60)
    #kateismaksut raha ei riita
    def test_kateinen_ei_riita_edulliseen_raha_kassassa(self):
        self.kassapaate.syo_edullisesti_kateisella(140)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_kateinen_ei_riita_edulliseen_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(140)
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_kateinen_ei_riita_edulliseen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(140), 140)
    def test_kateinen_ei_riita_maukkaaseen_raha_kassassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(140)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_kateinen_ei_riita_maukkaaseen_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(140)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    def test_kateinen_ei_riita_edulliseen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(140), 140)
    #korttimaksut raha riittaa
    def test_korttiraha_riittaa_edulliseen_True(self):
        kortti=Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), True)
    def test_korttiraha_riittaa_edulliseen_lounaat(self):
        kortti=Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
    def test_korttiraha_riittaa_edulliseen_raha_kassassa(self):
        kortti=Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_korttiraha_riittaa_edulliseen_saldo(self):
        kortti=Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 0)
    def test_korttiraha_riittaa_maukkaaseen_True(self):
        kortti=Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), True)
    def test_korttiraha_riittaa_maukkaaseen_lounaat(self):
        kortti=Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
    def test_korttiraha_riittaa_maukkaaseen_raha_kassassa(self):
        kortti=Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_korttiraha_riittaa_maukkaaseen_saldo(self):
        kortti=Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 0)
    #korttimaksut raha ei riita
    def test_korttiraha_ei_riita_edulliseen_False(self):
        kortti=Maksukortti(140)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)
    def test_korttiraha_ei_riita_edulliseen_lounaat(self):
        kortti=Maksukortti(140)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    def test_korttiraha_ei_riita_edulliseen_raha_kassassa(self):
        kortti=Maksukortti(140)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_korttiraha_riittaa_edulliseen_saldo(self):
        kortti=Maksukortti(140)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 140)
    def test_korttiraha_ei_riita_maukkaaseen_False(self):
        kortti=Maksukortti(140)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)
    def test_korttiraha_ei_riita_maukkaaseen_lounaat(self):
        kortti=Maksukortti(140)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    def test_korttiraha_ei_riita_maukkaaseen_raha_kassassa(self):
        kortti=Maksukortti(140)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    def test_korttiraha_riittaa_maukkaaseen_saldo(self):
        kortti=Maksukortti(140)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo, 140)
    #rahan lataaminen
    def test_saldo_muuttuu(self):
        kortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(kortti.saldo, 200)
    def test_raha_kassassa_kasvaa(self):
        kortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100200)
    def test_saldo_ei_muutu_negatiivinen_summa(self):
        kortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(kortti.saldo, 0)
    def test_raha_kassassa_ei_kasva_negatiivinen_summa(self):
        kortti=Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)