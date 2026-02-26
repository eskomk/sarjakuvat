# sarjakuvat

## Sovelluksen toiminnot
- Käyttäjä pystyy luomaan tunnuksen ja kirjautumaan sisään sovellukseen.
- Käyttäjä pystyy lisäämään, muokkaamaan ja poistamaan kuvauksia sarjakuvista.
- Käyttäjä näkee sovellukseen lisätyt sarjakuvien kuvaukset.
- Käyttäjä pystyy etsimään sarjakuvien kuvauksia hakusanalla.
- Käyttäjä pystyy valitsemaan sarjakuvan kuvaukseen "sarjakuvan tyyppi" -luokittelun.
- Käyttäjä näkee mitä sarjakuvia kukin käyttäjä on lisännyt.
- Sarjakuvaa arvosteleva käyttäjä pystyy antamaan sarjakuvalle tähtimäärän ja sanallisen arvostelun.

## Huomaa
- seed.py
  - Tiedosto ajamalla samassa hakemistossa terminaalissa (komennolla <code>$ python3 seed.py</code>) tyhjentää tietokannan päätaulut ja lisää satunnaisesti tuotettua dataa näihin tauluihin.
  - Ajo kestää ainakin minulla yli tunnin tiedoston muuttujien oletuksilla. Säädä muuttujat mieleiseksisi.
  - Ei liity muuten sovelluksen toimintaan.

## TODO
- TODO: Käyttäjä pystyy lisäämään kuvia kuvaukseen sarjakuvasta.
- TODO: Sovelluksessa on käyttäjäsivut, jotka näyttävät tilastoja ja käyttäjän lisäämät sarjakuvat.
  - Tämä osittain olemassa.
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

Luo tietokannan taulut;

<code>$ sqlite3 database.db < schema.sql</code>

Ja lisää alkutiedot:

<code>$ sqlite3 database.db < init.sql</code>

Voit käynnistää sovelluksen näin:

<code>$ flask run</code>

Tai näin jos oletusportti 5000 varattuna:

<code>$ flask run --port 5001</code>

## pylint report

<code>
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:11:0: C0410: Multiple imports on one line (forum, users, config) (multiple-imports)
app.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:36:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:57:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:89:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:108:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:115:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:151:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:151:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:182:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:183:4: R1731: Consider using 'page = max(page, 1)' instead of unnecessary if block (consider-using-max-builtin)
app.py:213:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:220:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:221:4: R1731: Consider using 'page = max(page, 1)' instead of unnecessary if block (consider-using-max-builtin)
app.py:244:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:245:4: R1731: Consider using 'page = max(page, 1)' instead of unnecessary if block (consider-using-max-builtin)
app.py:267:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:267:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:308:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:308:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:337:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:353:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:353:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:353:0: R0911: Too many return statements (7/6) (too-many-return-statements)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:25:0: C0305: Trailing newlines (trailing-newlines)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:14:4: E0237: Assigning to attribute 'last_insert_id' not defined in class slots (assigning-non-slot)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module forum
forum.py:1:0: C0114: Missing module docstring (missing-module-docstring)
forum.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:7:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:48:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:70:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:97:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:108:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:112:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:116:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:120:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:129:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:133:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
forum.py:133:0: C0116: Missing function or method docstring (missing-function-docstring)
forum.py:137:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
forum.py:137:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module seed
seed.py:1:0: C0114: Missing module docstring (missing-module-docstring)
seed.py:11:0: C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:12:0: C0103: Constant name "comic_count" doesn't conform to UPPER_CASE naming style (invalid-name)
seed.py:13:0: C0103: Constant name "star_count" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:25:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:32:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:37:0: C0116: Missing function or method docstring (missing-function-docstring)

------------------------------------------------------------------
Your code has been rated at 8.22/10 (previous run: 8.22/10, +0.00)
</code>

### C0114: Missing module docstring (missing-module-docstring)
Ei tarvita tällä kurssilla.

### C0410: Multiple imports on one line (forum, users, config) (multiple-imports)
On näköjään kurssin käytäntönä sallia useampia importteja rivillä.

### C0116: Missing function or method docstring (missing-function-docstring)
Kurssi ei vaadi docstringejä.

### R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
En ymmärrä miten voisi paremmin tämän tehdä.

### R1731: Consider using 'page = max(page, 1)' instead of unnecessary if block (consider-using-max-builtin)
Käsittääkseni logiikka menisi pieleen tällä suosituksella.

### R0911: Too many return statements (7/6) (too-many-return-statements)
Suositus ei taida ymmärtää funktion GET / POST -logiikkaa.

### C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
Kurssin käytäntö.

### C0305: Trailing newlines (trailing-newlines)
Joku suositus valitti aiemmin että ei ole rivinvaihtoa tiedoston lopussa. Kumpi parempi.

### W0102: Dangerous default value [] as argument (dangerous-default-value)
Kurssin käytäntö.

### E0237: Assigning to attribute 'last_insert_id' not defined in class slots (assigning-non-slot)
Kurssin käytäntö.

### C0103: Constant name "user_count" doesn't conform to UPPER_CASE naming style (invalid-name)
Kurssin käytäntö
