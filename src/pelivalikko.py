import sqlite3
from Tietokannan_kasittely import Tietokanta_kasittelija
from pelaaja_rajapinta import Pelaaja_rajapinta

class Pelivalikko:
    def __init__(self):
        self.tietokanta = Tietokanta_kasittelija()
        self.pelaamis_rajapinta = Pelaaja_rajapinta()
    
    def ohjeistus(self):
        print("Syötä haluamasi kysymysten määrä tai keskeytä syöttämällä cancel.")
    
    def startti(self):
        maksimi = self.tietokanta.kysymysten_maara()
        if maksimi < 1:
                print("Kysymyksiä ei ole tällä hetkellä tarjolla.")
                return False
        else:
            while True:
                print("Kysymyksiä tarjolla "+maksimi)
                self.ohjeistus()
                komento = input("Komento:")
                if komento == "cancel":
                    print("Keskeytetty")
                    break
                elif int(komento) in range(1, maksimi+1):
                    self.pelaamis_rajapinta.suorita(int(komento), maksimi)
                    break
                else:
                    print("Seuraathan ohjeita.")
        return True
