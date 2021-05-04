from pelaajarajapinta import Pelaajarajapinta
from pelivalikko import Pelivalikko
from tietokannankasittely import Tietokantakasittelija
from tiedostonkasittely import Tiedostokasittelija

class Taistelusovellus:
    """Luokka, jolla käynnistetään sovellus, ladataan peli ja lisätään kysymyksiä.
    
    Atribuutit:
        pelivalikko: Tällä valmistellaan uuden pelin kysymykset.
        jatko: Tällä jatketaan tallennettua peliä.
        tietokanta: Muodostaa yhteyden tietokantaan ja suorittaa kysymyksen lisäämisen.
        tiedostokasittely: Lataa tallennetun pelin sen jatkamista varten.
    """
    def __init__(self):
        self.pelivalikko = Pelivalikko()
        self.tietokanta = Tietokantakasittelija()
        self.tiedostokasittely = Tiedostokasittelija()
        self.jatko = Pelaajarajapinta()
    def ohje(self):
        """
        Tulostaa alkuvalikon ohjeistuksen.
        """
        print("Anna komento. 0 lopettaa sovelluksen.")
        print("1 aloittaa uuden pelin.")
        print("2 lisää uuden kysymyksen.")
        print("3 lataa tallennetun pelin.")
    def kysymys_valmistelu(self):
        """
        Kysyy käyttäjältä itse kysymyksen, kolme vastausta ja jokaiselle
        vastaukselle voiton, tappion ja tappion todennäköisyyden ja
        lisää tiedot tietokantaan.
        """
        kys = input("Kysymys: ")
        vas1 = input("Vastaus 1: ")
        tod1 = int(input("Vastauksen 1 epäonnistumisen todennäköisyys (kokonaisluku 1-100): "))
        voit1 = input("Vastauksen 1 voittotapahtuma: ")
        tap1 = input("Vastauksen 1 tappiotapahtuma: ")
        vas2 = input("Vastaus 2: ")
        tod2 = int(input("Vastauksen 2 epäonnistumisen todennäköisyys (kokonaisluku 1-100): "))
        voit2 = input("Vastauksen 2 voittotapahtuma: ")
        tap2 = input("Vastauksen 2 tappiotapahtuma: ")
        vas3 = input("Vastaus 3: ")
        tod3 = int(input("Vastauksen 3 epäonnistumisen todennäköisyys (kokonaisluku 1-100): "))
        voit3 = input("Vastauksen 3 voittotapahtuma: ")
        tap3 = input("Vastauksen 3 tappiotapahtuma: ")
        tiedot = (kys, vas1, voit1, tap1, tod1, vas2, voit2, tap2, tod2, vas3, voit3, tap3, tod3)
        self.tietokanta.lisaa_kysymys(tiedot)
    def aloita(self):
        """
        Käynnistää sovelluksen.
        """
        while True:
            self.ohje()
            komento = input("Komento:")
            if komento == "1":
                self.pelivalikko.startti()
            elif komento == "2":
                self.kysymys_valmistelu()
            elif komento == "3":
                lista = self.tiedostokasittely.lataa_peli()
                if len(lista) < 1:
                    print("Ei tallennettua peliä.")
                else:
                    self.jatko.suorita(lista)
            elif komento not in ["0", "1", "2", "3"]:
                print("Tuntematon komento.")
            else:
                break

peli = Taistelusovellus()
peli.aloita()
