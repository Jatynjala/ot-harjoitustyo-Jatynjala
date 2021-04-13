import sqlite3

class Tietokanta_kasittelija:
    def __init__(self):
        self.db = sqlite3.connect("kysymykset.db")
        self.db.isolation_level = None
    
    def kysymysten_maara(self):
        maara = self.db.execute("SELECT COUNT(*) FROM Kysymyksia").fetchone()
        return maara[0]
    
    def hae_kysymys(self, id: int):
        kysymys = self.db.execute("SELECT * FROM Kysymyksia WHERE id=?", [id]).fetchone()
        return kysymys
