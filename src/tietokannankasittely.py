import sqlite3

class Tietokantakasittelija:
    def __init__(self):
        self.database = sqlite3.connect("kysymykset.db")
        self.database.isolation_level = None
    def kysymysten_maara(self):
        maara = self.database.execute("SELECT COUNT(*) FROM Kysymyksia").fetchone()
        return maara[0]
    def hae_kysymys(self, i: int):
        kysymys = self.database.execute("SELECT * FROM Kysymyksia WHERE id=?", [i]).fetchone()
        return kysymys
    def lisaa_kysymys(self, tiedot: tuple):
        sqlkomento_yksi = "INSERT INTO Kysymyksia "
        sqlkomento_kaksi = "(kysymys,ekavastaus,ekavoitto,ekatappio,ekatodennakoisyys,"
        sqlkomento_kolme = "tokavastaus,tokavoitto,tokatappio,tokatodennakoisyys,"
        sqlkomento_nelja = "kolmasvastaus,kolmasvoitto,kolmastappio,kolmastodennakoisyys)"
        sqlkomento_viisi = " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"
        sqlkomento = sqlkomento_yksi+sqlkomento_kaksi+sqlkomento_kolme+sqlkomento_nelja+sqlkomento_viisi
        self.database.execute(sqlkomento, [tiedot[0],tiedot[1],tiedot[2],tiedot[3],tiedot[4],tiedot[5],tiedot[6],tiedot[7],tiedot[8],tiedot[9],tiedot[10],tiedot[11],tiedot[12]])
