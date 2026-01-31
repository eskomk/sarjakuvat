# sarjakuvat

## Sovelluksen toiminnot
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan kuvauksia sarjakuvista.
- TODO: Käyttäjä pystyy lisäämään kuvia kuvaukseen sarjakuvasta.
- Käyttäjä näkee sovellukseen lisätyt sarjakuvien kuvaukset.
- Käyttäjä pystyy etsimään sarjakuvien kuvauksia hakusanalla.
- TODO: Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät sarjakuvien kuvaukset.
- TODO: Käyttäjä pystyy valitsemaan sarjakuvan kuvaukseen yhden tai useamman luokittelun (esim. sarjakuvan tyyppi, tähtimäärä).

## Sovelluksen asennus

Asenna flask-kirjasto:

<code>$ pip install flask</code>

Luo tietokannan taulut ja lisää alkutiedot:

<code>$ sqlite3 database.db < schema.sql</code>

Voit käynnistää sovelluksen näin:

<code>$ flask run</code>
