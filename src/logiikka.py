from random import choice, randint

class Sovelluslogiikka:
    def luo_lista(self, lkm: int, maximi: int):
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
        elif vastaus == "2":
            return tiedot[7]
        elif vastaus == "3":
            return tiedot[11]
    def aseta_tappio(self, vastaus: str, tiedot: tuple):
        if vastaus == "1":
            return tiedot[4]
        elif vastaus == "2":
            return tiedot[8]
        elif vastaus == "3":
            return tiedot[12]
    def aseta_todennakoisyys(self, vastaus: str, tiedot: tuple):
        if vastaus == "1":
            return tiedot[5]
        elif vastaus == "2":
            return tiedot[9]
        elif vastaus == "3":
            return tiedot[13]
    def arvo_tapahtuma(self, voitto: str, tappio: str, todennakoisyys: int):
        sattuma = randint(1, 100)
        if sattuma > todennakoisyys:
            return voitto
        return tappio
