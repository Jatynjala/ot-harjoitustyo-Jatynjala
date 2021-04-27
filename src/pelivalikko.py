from pelaajarajapinta import Pelaajarajapinta
from tietokannankasittely import Tietokantakasittelija

class Pelivalikko:
    def __init__(self):
        self.tietokanta = Tietokantakasittelija()
        self.pelaamis_rajapinta = Pelaajarajapinta()
    def ohjeistus(self):
        print("Syötä haluamasi kysymysten määrä kokonaislukuna tai keskeytä syöttämällä cancel.")
    def startti(self):
        maksimi = self.tietokanta.kysymysten_maara()
        if maksimi < 1:
            print("Kysymyksiä ei ole tällä hetkellä tarjolla.")
        else:
            while True:
                print("Kysymyksiä tarjolla "+str(maksimi))
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
