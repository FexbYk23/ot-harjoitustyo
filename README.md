# CHIP8-Emulaattori
Sovelluksen avulla käyttäjä voi suorittaa CHIP8-Järjestelmälle tehtyjä ohjelmia moderneilla tietokoneilla.  

## Dokumentaatio

[Määrittelydokumentti](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/m%C3%A4%C3%A4rittelydokumentti.md)  
[Työaikakirjanpito](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/ty%C3%B6aikakirjanpito.md)  
[Arkkitehtuuri](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)  
[Release 1](https://github.com/FexbYk23/ot-harjoitustyo/releases/tag/viikko5)  


## Asennus
1. Asenna riippuvuudet komennolla:   
`poetry install`  

2. Suorita sovellus komennolla:  
`poetry run invoke start`  


## Testaus
Testit voidaan suorittaa komennolla:  
`poetry run invoke test`

Testikattavuusraportin voi generoida komennolla:  
`poetry run invoke coverage-report`  

Pylintin tarkistus voidaan suorittaa komennolla:
`poetry run invoke lint`
