import unittest
from logiikka import Sovelluslogiikka

class TestSovelluslogiikka(unittest.TestCase):
    def setUp(self):
        self.logiikkaa = Sovelluslogiikka()
    
    def test_luo_lista(self):
        testilista = self.logiikkaa.luo_lista(2, 5)
        self.assertEqual(len(testilista), 2)
