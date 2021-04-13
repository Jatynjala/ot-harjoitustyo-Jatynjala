from pelivalikko import Pelivalikko
import sqlite3

class Taistelusovellus:
    def __init__(self):
        self.pelivalikko = Pelivalikko()
    def ohje(self):
        print("Anna komento. 0 lopettaa sovelluksen.")
        print("1 aloittaa uuden pelin.")
    def aloita(self):
        while True:
            self.ohje()
            komento = input("Komento:")
            if komento == "0":
                break
            elif komento == "1":
                self.pelivalikko.startti()
            else:
                print("Tuntematon komento.")

peli = Taistelusovellus()
peli.aloita()
