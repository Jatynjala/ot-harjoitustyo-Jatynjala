class Tiedostokasittelija:
    """
    Tätä luokkaa käytetään pelin tallentamiseen ja lataamiseen.
    """
    def tallenna_peli(self, lista_kysymyksista: list, kohta: int, nimi="pelitallennus.txt"):
        """
        Tallentaa pelin erilliseen tekstitiedostoon.
        Ottaa parametreina listan kysymyksistä ja kohdan, johon ollaan jääty.
        """
        tallennettava_lista = [str(alkio)+"\n" for alkio in lista_kysymyksista[kohta:]]
        with open(nimi, "w") as tiedosto:
            for rivi in tallennettava_lista:
                tiedosto.write(rivi)
    def lataa_peli(self, nimi="pelitallennus.txt"):
        """
        Lataa pelin erillisestä tekstitiedostosta.
        """
        with open(nimi) as tiedosto:
            palautettava_lista = []
            for rivi in tiedosto:
                kysymysnumerostr = rivi.replace("\n", "")
                kysymysnumero = int(kysymysnumerostr)
                palautettava_lista.append(kysymysnumero)
        return palautettava_lista
