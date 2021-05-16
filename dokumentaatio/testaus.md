# Testaus
Ohjelmaa on testattu automaattisilla yksikkö- ja integraatiotesteillä sekä manuaalisesti ohjelmaa käyttämällä.  

## Yksikkö- ja Integraatiotestaus
Emulaation testaamiseen on kolme luokkaa:  
TestInstruction, joka testaa Instruction olioiden luomista eri konekäskyillä.  
TestInstructionExec, joka testaa konekäskyjen suorittamista Chip8 oliolla.  
TestChip8, joka testaa Chip8 luokan toimintaa

Näiden lisäksi on vielä TestSettings, joka testaa asetuksista vastaavaa Settings luokkaa.


## Testikattavuus
Käyttöliittymää ja testejä huomioimatta ohjelman testikattavuus on 85%
![](https://github.com/FexbYk23/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/coverage.png)  

Testejen ulkopuolelle jäi muutamien konekäskyjen suorittaminen, virheellisten asetusten lukeminen ja chip8 ohjelmien lukeminen tiedostosta, sekä koko SoundPlayer luokka, koska en keksinyt siinä mitään testattavaa.


