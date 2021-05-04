# Käyttöohje
Mikäli sovellus on asennettu siihen liittyvien ohjeiden mukaisesti, käynnistämisen pitäisi onnistua komentoriviltä sovelluksen hakemistossa komennolla 'poetry run invoke start'.
## Uusi peli
Sovelluksen käynnistämisen jälkeen käyttäjältä kysytään aloitusvalikossa jotain komennoista 0, 1, 2 tai 3. Uuden pelin aloittamiseksi syötetään 1. Komento 0 sulkee sovelluksen.

Tämän jälkeen sovellus menee uuden pelin valmisteluun ja hakee tietokannasta kysymysten lukumäärän. Mikäli tietokannassa ei ole kysymyksiä, käyttäjä palautetaan aloitusvalikkoon. Muussa tapauksessa käyttäjältä kysytään joko syötettä 'cancel' tai kokonaislukua väliltä 1-X, missä X on aiemmin saatu kysymysten lukumäärä. Syöte 'cancel' palauttaa käyttäjän aloitusvalikkoon. Kokonaisluku aloittaa pelin ja siirtyy pelinäkymään.

## Pelin lataaminen
Jos aloitusvalikossa antaa komennon 3, tallennettu peli ladataan, ja sovellus siirtyy pelinäkymään.

## Pelinäkymä
Pelinäkymässä käyttäjälle on luotu satunnainen lista kysymyksiä, jonka sovellus käy läpi kysymys kerrallaan. Jokaiseen kysymykseen on kolme vastausta, joista jokainen voi jollakin todennäköisyydellä onnistua tai epäonnistua.

Käyttäjä antaa jonkun syötteistä 'save', 'quit', 1, 2 tai 3. Syöte 'save' tallentaa pelin ja palaa takaisin kysymykseen, kun taas 'quit' keskeyttää pelin ja palaa aloitusvalikkoon. Syöttämällä 1, 2 tai 3 käyttäjä antaa vastaukseksi vastaavan vastauksen, minkä jälkeen sovellus arpoo vastaukseen liityvän todennäköisyyden perusteella, onnistuuko vastaus vai ei.

## Kysymysten lisääminen
Kun aloitusvalikossa annetaan komento 2, käyttäjältä kysytään ensin itse kysymys ja sitten kolme kertaa vastaus, siihen liittyvä epäonnistumisen todennäkösyys, voitto ja tappio kyseisessä järjestyksessä. Tämän jälkeen tiedot lisätään tietokantaan, ja sovellus palaa aloitusvalikkoon.
