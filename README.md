# sarjakuvat

## Sovelluksen toiminnot
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan kuvauksia sarjakuvista.
- Käyttäjä pystyy lisäämään kuvia kuvaukseen sarjakuvasta.
- Käyttäjä näkee sovellukseen lisätyt sarjakuvien kuvaukset.
- Käyttäjä pystyy etsimään sarjakuvien kuvauksia hakusanalla.
- Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät sarjakuvien kuvaukset.
- Käyttäjä pystyy valitsemaan sarjakuvan kuvaukseen yhden tai useamman luokittelun (esim. sarjakuvan tyyppi, tähtimäärä).

## Sovelluksen asennus

Asenna flask-kirjasto:

<code>$ pip install flask</code>

Luo tietokannan taulut ja lisää alkutiedot:

<code>$ sqlite3 database.db < schema.sql</code>
<code>$ sqlite3 database.db < init.sql</code>

Voit käynnistää sovelluksen näin:

<code>$ flask run</code>
