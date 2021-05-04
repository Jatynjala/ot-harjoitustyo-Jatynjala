from logiikka import Sovelluslogiikka
from pelaajarajapinta import Pelaajarajapinta
from tietokannankasittely import Tietokantakasittelija

class Pelivalikko:
    """
    Tätä luokkaa käytetään valmistellaan kysymykset uutta peliä varten.
    
    Atribuutit:
        tietokanta: Käytetään kysymysten hakemiseen.
        logiikka: Käytetään kysymyslistan luomiseen.
        pelaamis_rajapinta: Käytetään pelin aloittamiseen.
    """
    def __init__(self):
        self.tietokanta = Tietokantakasittelija()
        self.logiikka = Sovelluslogiikka()
        self.pelaamis_rajapinta = Pelaajarajapinta()
    def ohjeistus(self):
        """
        Tulostaa ohjeistuksen.
        """
        print("Syötä haluamasi kysymysten määrä kokonaislukuna tai keskeytä syöttämällä cancel.")
    def startti(self):
        """
        Hakee kysymysten määrän ja kysyy läpikäytävien kysymysten määrän.
        """
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
                    lista_kysymyksia = self.logiikka.luo_lista(int(komento), maksimi)
                    self.pelaamis_rajapinta.suorita(lista_kysymyksia)
                    break
                else:
                    print("Seuraathan ohjeita.")
