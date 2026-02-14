# sarjakuvat

## Sovelluksen toiminnot
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan kuvauksia sarjakuvista.
- Käyttäjä näkee sovellukseen lisätyt sarjakuvien kuvaukset.
- Käyttäjä pystyy etsimään sarjakuvien kuvauksia hakusanalla.
- Käyttäjä pystyy valitsemaan sarjakuvan kuvaukseen "sarjakuvan tyyppi" -luokittelun.
- Sarjakuvaa arvosteleva käyttäjä pystyy antamaan sarjakuvalle tähtimäärän ja sanallisen arvostelun.

## Huomaa
- seed.py
- - Tiedosto ajamalla samassa hakmeistossa terminaalissa (komennolla <code>$ python3 seed.py</code>) lisää satunnaisesti tuotettua dataa tietokannan tauluihin.
- - Ajo kestää ainakin minulla yli tunnin tiedoston muuttujien oletuksilla. Säädä muuttujat mieleiseksisi.
- - Ei liity muuten sovelluksen toimintaan.

## TODO
- TODO: Käyttäjä pystyy lisäämään kuvia kuvaukseen sarjakuvasta.
- TODO: Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät sarjakuvat.
- - Tämä osittain olemassa.
- TODO: Etsintätoiminnon tulosten sivutus.
- TODO: Järkevämpi toiminto users.html -sivulla käyttäjän lisäämien sarjakuvien läpikäyntiin. Liittyy routeen userlist_paged.
- TODO: Tyylitiedostojen käyttö, kunhan olen päättänyt pitääkö sovelluksen ulkonäköä miten viilata.

## Sovelluksen asennus

Kloonaa repo halutussa kansiossa:
<code>git clone https://github.com/eskomk/sarjakuvat.git</code>

Käynnistä halutessasi python-virtuaaliympäristö:
<code>python3 -m venv venv</code> ja aktivoi virtuaaliympäristö: <code>source venv/bin/activate</code>

Asenna flask-kirjasto:

<code>$ pip install flask</code>

Luo tietokannan taulut ja lisää alkutiedot:

<code>$ sqlite3 database.db < schema.sql</code>
<code>$ sqlite3 database.db < init.sql</code>

Voit käynnistää sovelluksen näin:

<code>$ flask run</code>

Tai näin jos oletusportti 5000 varattuna:

<code>$ flask run --port 5001</code>
