# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjä voi suorittaa CHIP8-järjestelmälle tehtyjä ohjelmia modernilla tietokoneella.


## Suunnitellut toiminnallisuudet

- ohjelma jäljittelee CHIP8-järjestelmän toimintaa tarpeeksi tarkasti, jotta suurin osa ohjelmista toimisi
  - ohjelma suorittaa CHIP8-ohjelman sisältämiä konekäskyjä [tehty]
  - ohjelma näyttää CHIP8-ohjelman tuottamaa grafiikkaa [tehty]
  - ohjelma toistaa CHIP8-ohjelman tuottamaa ääntä
- käyttäjä voi avata suoritettavan CHIP8-ohjelman tiedostosta graafisella käyttöliittymällä [tehty]
- käyttäjä voi muuttaa asetuksia (kuten mitä näppäimiä emulaattori käyttää) grafisella käyttöliittymällä [tehty]
  - asetukset tallennetaan koneelle tiedostoon, josta ohjelma voi lukea ne käynnistyessään [tehty]


## Jatkokehitysideoita

- graafinen käyttöliittymä, jolla käyttäjä voi tutkia ja muokata emuloidun järjestelmän muistia
- graafinen käyttöliittymä, joka näyttää emuloidun järjestelmän rekisterit ja mahdollistaa emuloidun koodin suorittamisen konekäsky kerrallaan
  - konekäskyt voitaisiin kääntää symboliseksi konekieleksi
- suoritettavia CHIP8 ohjelmia voitaisiin ladata netistä
