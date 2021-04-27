from logiikka import Sovelluslogiikka
from tietokannankasittely import Tietokantakasittelija
from tiedostonkasittely import Tiedostokasittelija

class Pelaajarajapinta:
    def __init__(self):
        self.tietokanta = Tietokantakasittelija()
        self.logiikka = Sovelluslogiikka()
        self.tiedostokasittely = Tiedostokasittelija()
    def tulosta_kysymys(self, kysymys_tiedot: tuple):
        print(kysymys_tiedot[1])
        print("1: "+kysymys_tiedot[2]+",")
        print("2: "+kysymys_tiedot[6]+",")
        print("vai 3: "+kysymys_tiedot[10]+".")
        print("save tallentaa pelin ja quit lopettaa pelin.")
    def tallennus(self, vastaus_tallenna, kysymyslista, kysymys):
        if vastaus_tallenna == "save":
            self.tiedostokasittely.tallenna_peli(kysymyslista, kysymys)
            print("Peli tallennettu.")
    def suorita(self, maara: int, maksimi: int):
        kysymyslista = self.logiikka.luo_lista(maara, maksimi)
        for kysymys in range(0, len(kysymyslista)):
            kysymyksentiedot = self.tietokanta.hae_kysymys(kysymyslista[kysymys])
            self.tulosta_kysymys(kysymyksentiedot)
            vastaus = input("Vastaus:")
            self.tallennus(vastaus, kysymyslista, kysymys)
            if vastaus == "quit":
                return
            while vastaus not in ["1", "2", "3"]:
                print("Vastaa 1, 2 tai 3, tallenna peli komennolla save tai lopeta peli komennolla quit.")
                vastaus = input("Vastaus:")
                self.tallennus(vastaus, kysymyslista, kysymys)
                if vastaus == "quit":
                    return
            voitto = self.logiikka.aseta_voitto(vastaus, kysymyksentiedot)
            tappio = self.logiikka.aseta_tappio(vastaus, kysymyksentiedot)
            todennakoisyys = self.logiikka.aseta_todennakoisyys(vastaus, kysymyksentiedot)
            print(self.logiikka.arvo_tapahtuma(voitto, tappio, todennakoisyys))
        print("Kysely päättyy.")
