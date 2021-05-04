from random import choice, randint

class Sovelluslogiikka:
    """
    Tällä luokalla toteutetaan sovelluksen sisäinen logiikka.
    Metodit aseta_voitto, aseta_tappio ja aseta_todennakoisyys
    palauttavat vastaavasti voiton, tappion ja todennäköisyyden,
    joita käytetään tapahtuman arpomisessa.
    """
    def luo_lista(self, lkm: int, maximi: int):
        """
        Luo satunnaisen listan kysymyksiä annettujen parametrien mukaan.
        """
        tulos_lista=[]
        mahdolliset_kysymykset = [numero for numero in range(1, maximi+1)]
        for i in range(0, lkm):
            kysymys = choice(mahdolliset_kysymykset)
            tulos_lista.append(kysymys)
            mahdolliset_kysymykset.remove(kysymys)
        return tulos_lista
    def aseta_voitto(self, vastaus: str, tiedot: tuple):
        if vastaus == "1":
            return tiedot[3]
        if vastaus == "2":
            return tiedot[7]
        if vastaus == "3":
            return tiedot[11]
    def aseta_tappio(self, vastaus: str, tiedot: tuple):
        if vastaus == "1":
            return tiedot[4]
        if vastaus == "2":
            return tiedot[8]
        if vastaus == "3":
            return tiedot[12]
    def aseta_todennakoisyys(self, vastaus: str, tiedot: tuple):
        if vastaus == "1":
            return tiedot[5]
        if vastaus == "2":
            return tiedot[9]
        if vastaus == "3":
            return tiedot[13]
    def arvo_tapahtuma(self, voitto: str, tappio: str, todennakoisyys: int):
        """
        Arpoo annetun todennäköisyyden perusteella, tapahtuuko voitto vai tappio.
        """
        sattuma = randint(1, 100)
        if sattuma > todennakoisyys:
            return voitto
        return tappio
