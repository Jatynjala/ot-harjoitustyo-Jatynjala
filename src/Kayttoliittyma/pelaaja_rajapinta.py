from logiikka import Sovelluslogiikka
from Tietokannan_kasittely import Tietokanta_kasittelija

class Pelaaja_rajapinta:
    def __init__(self):
        self.tietokanta = Tietokanta_kasittelija()
        self.logiikka = Sovelluslogiikka()
    def tulosta_kysymys(self, kysymys_tiedot: tuple):
        print(kysymys_tiedot[1])
        print("1: "+kysymys_tiedot[2]+",")
        print("2: "+kysymys_tiedot[6]+",")
        print("vai 3: "+kysymys_tiedot[10]+".")
    def suorita(self, maara: int, maksimi: int):
        kysymyslista = self.logiikka.luo_lista(maara, maksimi)
        for kysymys in range(0, len(kysymyslista)):
            kysymyksentiedot = self.tietokanta.hae_kysymys(kysymyslista[kysymys])
            self.tulosta_kysymys(kysymyksentiedot)
            vastaus = input("Vastaus:")
            while vastaus not in ["1", "2", "3"]:
                print("Vastaa 1, 2 tai 3.")
                vastaus = input("Vastaus:")
            voitto = self.logiikka.aseta_voitto(vastaus, kysymyksentiedot)
            tappio = self.logiikka.aseta_tappio(vastaus, kysymyksentiedot)
            todennakoisyys = self.logiikka.aseta_todennakoisyys(vastaus, kysymyksentiedot)
            print(self.logiikka.arvo_tapahtuma(voitto, tappio, todennakoisyys))
        print("Kysely päättyy.")
