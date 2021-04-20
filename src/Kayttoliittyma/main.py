from pelivalikko import Pelivalikko
from Tietokannan_kasittely import Tietokanta_kasittelija

class Taistelusovellus:
    def __init__(self):
        self.pelivalikko = Pelivalikko()
        self.tietokanta = Tietokanta_kasittelija()
    def ohje(self):
        print("Anna komento. 0 lopettaa sovelluksen.")
        print("1 aloittaa uuden pelin.")
        print("2 lisää uuden kysymyksen.")
    def kysymys_valmistelu(self):
        kys = input("Kysymys: ")
        vas1 = input("Vastaus 1: ")
        tod1 = int(input("Vastauksen 1 todennäköisyys (kokonaisluku 1-100): "))
        voit1 = input("Vastauksen 1 voittotapahtuma: ")
        tap1 = input("Vastauksen 1 tappiotapahtuma: ")
        vas2 = input("Vastaus 2: ")
        tod2 = int(input("Vastauksen 2 todennäköisyys (kokonaisluku 1-100): "))
        voit2 = input("Vastauksen 2 voittotapahtuma: ")
        tap2 = input("Vastauksen 2 tappiotapahtuma: ")
        vas3 = input("Vastaus 3: ")
        tod3 = int(input("Vastauksen 3 todennäköisyys (kokonaisluku 1-100): "))
        voit3 = input("Vastauksen 3 voittotapahtuma: ")
        tap3 = input("Vastauksen 3 tappiotapahtuma: ")
        tiedot = (kys, vas1, voit1, tap1, tod1, vas2, voit2, tap2, tod2, vas3, voit3, tap3, tod3)
        self.tietokanta.lisaa_kysymys(tiedot)
    def aloita(self):
        while True:
            self.ohje()
            komento = input("Komento:")
            if komento == "1":
                self.pelivalikko.startti()
            elif komento == "2":
                self.kysymys_valmistelu()
            elif komento not in ["0", "1", "2"]:
                print("Tuntematon komento.")
            else:
                break

peli = Taistelusovellus()
peli.aloita()
