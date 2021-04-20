import sqlite3

class Tietokanta_kasittelija:
    def __init__(self):
        self.db = sqlite3.connect("kysymykset.db")
        self.db.isolation_level = None
    def kysymysten_maara(self):
        maara = self.db.execute("SELECT COUNT(*) FROM Kysymyksia").fetchone()
        return maara[0]
    def hae_kysymys(self, i: int):
        kysymys = self.db.execute("SELECT * FROM Kysymyksia WHERE id=?", [i]).fetchone()
        return kysymys
    def lisaa_kysymys(self, tiedot: tuple):
        sqlkomento = "INSERT INTO Kysymyksia (kysymys,ekavastaus,ekavoitto,ekatappio,ekatodennakoisyys,tokavastaus,tokavoitto,tokatappio,tokatodennakoisyys,kolmasvastaus,kolmasvoitto,kolmastappio,kolmastodennakoisyys) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        self.db.execute(sqlkomento, [tiedot[0],tiedot[1],tiedot[2],tiedot[3],tiedot[4],tiedot[5],tiedot[6],tiedot[7],tiedot[8],tiedot[9],tiedot[10],tiedot[11],tiedot[12]])
