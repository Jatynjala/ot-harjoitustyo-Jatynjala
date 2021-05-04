from logiikka import Sovelluslogiikka
from tietokannankasittely import Tietokantakasittelija
from tiedostonkasittely import Tiedostokasittelija
from random import randint

class Pelaajarajapinta:
    """
    Tällä luokalla suoritetaan itse pelin pelaaminen.
    
    Atribuutit:
        tietokanta: Käytetään kysymysten tietojen hakemiseen.
        logiikka: Käytetään tapahtuman arpomiseen.
        tiedotokasittely: Käytetään pelin tallentamiseen.
    """
    def __init__(self):
        self.tietokanta = Tietokantakasittelija()
        self.logiikka = Sovelluslogiikka()
        self.tiedostokasittely = Tiedostokasittelija()
    def tulosta_kysymys(self, kysymys_tiedot: tuple):
        """
        Ottaa parametrina kysymyksen tiedot ja tulostaa ne.
        """
        print(kysymys_tiedot[1])
        print("1: "+kysymys_tiedot[2]+",")
        print("2: "+kysymys_tiedot[6]+",")
        print("vai 3: "+kysymys_tiedot[10]+".")
        print("save tallentaa pelin ja quit lopettaa pelin.")
    def alaiset(self):
        """
        Kertoo käyttäjälle kuinka moni alainen kannattaa mitäkin
        vaihtoehtoa.
        """
        alaisia = 8
        ykkonen = alaisia-randint(0, alaisia)
        alaisia -= ykkonen
        kakkonen = alaisia-randint(0, alaisia)
        alaisia -= kakkonen
        kolmonen = alaisia-randint(0, alaisia)
        print("Alaiset: vaihtoehto 1:"+str(ykkonen)+" vaihtoehto 2:"+str(kakkonen)+" vaihtoehto 3:"+str(kolmonen))
    def tallennus(self, vastaus_tallenna, kysymyslista, kysymys):
        """
        Tallentaa pelin. Ottaa parametreina komennon ja tiedot siitä,
        mitkä kysymykset ovat käymättä.
        """
        if vastaus_tallenna == "save":
            self.tiedostokasittely.tallenna_peli(kysymyslista, kysymys)
            print("Peli tallennettu.")
    def suorita(self, kysymyslista: list):
        """
        Käy parametrina annetun listan kysymykset läpi yksi kerrallaan,
        tulostaen ne ja kysyen käyttäjän vastausta.
        """
        for kysymys in range(0, len(kysymyslista)):
            kysymyksentiedot = self.tietokanta.hae_kysymys(kysymyslista[kysymys])
            self.tulosta_kysymys(kysymyksentiedot)
            self.alaiset()
            vastaus = input("Vastaus:")
            self.tallennus(vastaus, kysymyslista, kysymys)
            if vastaus == "quit":
                return
            while vastaus not in ["1", "2", "3"]:
                self.tulosta_kysymys(kysymyksentiedot)
                self.alaiset()
                vastaus = input("Vastaus:")
                self.tallennus(vastaus, kysymyslista, kysymys)
                if vastaus == "quit":
                    return
            voitto = self.logiikka.aseta_voitto(vastaus, kysymyksentiedot)
            tappio = self.logiikka.aseta_tappio(vastaus, kysymyksentiedot)
            todennakoisyys = self.logiikka.aseta_todennakoisyys(vastaus, kysymyksentiedot)
            print(self.logiikka.arvo_tapahtuma(voitto, tappio, todennakoisyys))
        print("Kysely päättyy.")
