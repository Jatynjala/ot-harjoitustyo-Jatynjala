# Vaatimusmäärittely

### Tarkoitus
Tällä sovelluksella käyttäjä voi kokeilla, mitä voi seurata erilaisista päätöksistä kenraalina taistelukentällä.
Sovelluksella on tarkoitus olla vain yksi käyttäjärooli: *normaali käyttäjä*.

### Käyttöliittymä
Sovelluksen käyttöliitymä on tällä hetkellä tekstipohjainen

### Toteutettu toiminnallisuus
Tällä hetkellä sovelluksessa on toteutettu seuraavat toiminnallisuudet:
* Aloitusvalikossa käyttäjä voi aloittaa uuden pelin, lisätä uuden kysymyksen tai lopettaa.
* Ennen uuden pelin aloittamista sovellus kertoo käyttäjälle, montako kysymystä on tarjolla. Käyttäjä joko keskeyttää uuden pelin aloittamisen ja palaa aloitusvalikkoon tai kertoo sovellukselle, moneenko kysymykseen hän aikoo vastata.
* Kerrotuaan sovellukselle, montako kysymystä hän aikoo ottaa, käyttäjä vastaa yksi kerrallaan esitettyihin kysymyksiin 1, 2 tai 3, jotka vastaavat vastausvaihtoehtoja.
* Kun käyttäjä on vastannut kysymykseen, sovellus arpoo onnistuuko käyttäjän vastaus ratkaisemaan tilannetta, tulostaa lopputuloksen ja siirtyy seuraavaan kysymykseen.
* Kun sovellukselle kerrottu määrä kysymyksiä on käyty läpi, sovellus palaa aloitusvalikkoon.
* Kysymystä lisätessä käyttäjältä kysytään itse kysymys, kolme vastausta ja jokaiseen vastaukseen voitto, tappio ja voiton todennäköisyys kokonaislukuna suljetulta väliltä 1-100.
* Tämän jälkeen sovellus lisää kysymyksen tietokantaan.

### Jatkokehitysideat
Sovellukseen saatetaan tulevaisuudessa toteuttaa seuraavat toiminnallisuudet:
* Kesken olevan kyselyn tallentaminen myöhempää jatkamista varten.
* Tallennetun kyselyn jatkaminen aloitusvalikosta
