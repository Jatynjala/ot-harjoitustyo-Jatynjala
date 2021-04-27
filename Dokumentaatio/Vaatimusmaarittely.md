# Vaatimusmäärittely

### Tarkoitus
Tällä sovelluksella käyttäjä voi kokeilla, mitä voi seurata erilaisista päätöksistä kenraalina taistelukentällä.
Sovelluksella on tarkoitus olla vain yksi käyttäjärooli: *normaali käyttäjä*.

### Käyttöliittymä
Sovelluksen käyttöliitymä on tällä hetkellä tekstipohjainen.

### Toteutettu toiminnallisuus
Tällä hetkellä sovelluksessa on toteutettu seuraavat toiminnallisuudet:
* Aloitusvalikossa käyttäjä voi aloittaa uuden pelin, lisätä uuden kysymyksen, ladata tallennetun pelin tai lopettaa.
* Ennen uuden pelin aloittamista sovellus kertoo käyttäjälle, montako kysymystä on tarjolla. Käyttäjä joko keskeyttää uuden pelin aloittamisen ja palaa aloitusvalikkoon tai kertoo sovellukselle, moneenko kysymykseen hän aikoo vastata.
* Kerrotuaan sovellukselle, montako kysymystä hän aikoo ottaa, käyttäjä vastaa yksi kerrallaan esitettyihin kysymyksiin 1, 2 tai 3, jotka vastaavat vastausvaihtoehtoja.
* Kun käyttäjä on vastannut kysymykseen, sovellus arpoo onnistuuko käyttäjän vastaus ratkaisemaan tilannetta, tulostaa lopputuloksen ja siirtyy seuraavaan kysymykseen.
* Kun sovellukselle kerrottu määrä kysymyksiä on käyty läpi, sovellus palaa aloitusvalikkoon.
* Kysymystä lisätessä käyttäjältä kysytään itse kysymys, kolme vastausta ja jokaiseen vastaukseen voitto, tappio ja voiton todennäköisyys kokonaislukuna suljetulta väliltä 1-100. Tämän jälkeen sovellus lisää kysymyksen tietokantaan.
* Kysymykseen vastaamisen yhteydessä käyttäjä voi tallentaa pelin, minkä sovellus tekee erilliseen tekstitiedostoon 'pelitallennus.txt', tai lopettaa pelin kesken, jolloin hän palaa aloitusvalikkoon. Huom. lopettamisen yhteydessä peliä ei tallenneta.
* Jos käyttäjä lataa tallennetun pelin aloitusvalikosta, sovellus lataa tarvittavat tiedot edellä mainitusta tekstitiedostosta ja vie käyttäjän jatkamaan peliä.

### Jatkokehitysideoita
Sovellukseen saatetaan tulevaisuudessa toteuttaa seuraavat toiminnallisuudet:
* Alaiset suosittelevat kukin yhtä vaihtoehtoa kysymykseen vastattaessa.
