# Käyttöohje
Ohjelman käynnistyessä aukeaa musta ikkuna, jonka yläosassa on avattava File valikko.  
![](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/mainwindow.png)  

File valikossa on seuraavat vaihtoehdot:  

### Open Program
Avaa ikkunan, josta voit valita tietokoneeltasi suoritettavan chip8 tiedoston.  
Valittuasi tiedoston, se ladataan asetusten "entrypoint" kohdan osoittamaan kohtaan muistissa ja ohjelman suoritus alkaa.  

### Reset
Alustaa emuloidun järjestelmän rekisterit, mutta ei alusta muistia.  
Käytettävissä vain kun ohjelmaa suoritetaan.  

### Pause
Pysäyttää ohjelman suorituksen väliaikaisesti, suoritusta voi jatkaa tästä samasta vaihtoehdosta.  
Käytettävissä vain kun ohjelmaa suoritetaan.  

### Settings
Avaa ikkunan, jossa voit muuttaa emulaattorin asetuksia.

### Controls
Avaa ikkunan, jossa voit muuttaa emulaattorin käyttämiä näppäimiä.


## Settings-ikkuna
![](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/settings_dialog.png)  
Tässä ikkunassa voit muuttaa emulaattorin asetuksia. Asetukset tallennetaan settings.cfg nimiseen tiedostoon, josta ne myös luetaan ohjelman käynnistyessä.  
Voit tallentaa asetukset ja sulkea ikkunan painamalla OK-näppäintä. Ikkunan sulkeminen muuten ei tallenna asetuksia.
Vaihtoehdot:  
### Entrypoint
Ohjelmat kopioidaan tähän osoitteeseen ja suoritus alkaa tästä osoitteesta.  
Oletusarvo on 512 ja useimmat ohjelmat käyttävät kyseistä arvoa.

### Emulation speed
Tämä arvo määrittää kuinka nopeasti ohjelmaa suoritetaan.  
Konekäskyjen välillä odotetaan 1000/x millisekuntia, missä x on tämän kentän arvo. 
Oletusarvo on 300.

### Foreground color
Emulaattorin käyttämä edustaväri hex muodossa.  
Oletusarvo on #ffffff eli valkoinen.

### Background color
Emulaattorin käyttämä taustaväri hex muodossa.  
Oletusarvo on #000000 eli musta.

### Mute sound
Tämä vaihtoehto estää äänentoiston.  
Oletusarvona äänet ovat päällä.

## Controls-ikkuna
![](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/controls.png)  
Tässä ikkunassa voit vaihtaa emulaattorin käyttämiä näppäimiä.  
Näppäinten nimet ovat [tkinterin käyttämiä keysym](https://www.tcl.tk/man/tcl8.4/TkCmd/keysyms.htm) arvoja.

