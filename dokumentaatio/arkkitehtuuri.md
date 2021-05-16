# Arkkitehtuuri

## Rakenne
Ohjelman lähdekoodi on jaettu kansioihin seuraavasti:  
Käyttöliittymään liittyvä koodi on src/ui/ kansiossa.  
Testien koodi on src/tests/ kansiossa.  
Ohjelman ydintoiminnallisuuteen liittyvä koodi on src/ kansiossa.

## Käyttöliittymä
Ohjelman käyttöliittymä koostuu kolmesta ikkunasta: Ohjelman pääikkunasta, asetusikkunasta ja näppäinasetusikkunasta. 
Ohjelman pääikkunasta voidaan avata muut ikkunat. Jokaista erityyppistä ikkunaa voi olla avattuna vain yksi kerrallaan.

## Tietojen tallennus
Ohjelma tallentaa käyttäjän antamat asetukset "settings.cfg" nimiseen tiedostoon pythonin [configparser](https://docs.python.org/3/library/configparser.html) kirjaston käyttämässä formaatissa.

# Päätoiminnallisuuksien sekvenssikaaviot

## Chip8 ohjelmien suoritus
![](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/ohjelman_suoritus.png)

## Asetusten muuttaminen
![](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/settings.png)  


# Ohjelman rakenteeseen jääneet heikkoudet
Settings luokan olisi voinut jakaa asetukset sisältävään ja tiedostoja käsittelevään osaan eri luokiksi.
Asetusten validointia tapahtuu myös sekä käyttöliittymän että Settings luokan sisällä.
