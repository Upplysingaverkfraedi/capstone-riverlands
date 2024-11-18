# Verkefnalýsing
Verkefnið fól í sér að útbúa og hanna mælaborð sem lýsti mismunandi þáttum evrópsku söngvakeppninnar Eurovision líkt og tóntegundum og takti (bpm) laga, lengd atriða og velgengni landa. Þá var kafað dýpra í velgengni Svíþjóðar annars vegar og Íslands hins vegar yfir 20 ára tímabil (árunum 2004-2024) og borið þau saman þar sem þau taka keppninni hvað alvarlegast. 
Leitað var að gagnagrunnum með nytsamlegum upplýsingum á netinu sem voru síðan skrapaðar og parse-aðar með gerð reglulegra segða (regex), breyttar í CSV skrár en einnig var unnið gagnagrunna í Postgres sem notaðir voru við gerð mælaborðsins í Power BI. 

# Niðurstöður
Ýmsar áhugaverðar niðurstöður komu í ljós við gerð mælaborðsins. Þar má meðal annars sjá hvernig uppröðun atriða getur haft áhrif á velgengni landa í keppninni; best er að vera sautjándi í röðinni eða seinna. Svíþjóð og Írland hafa unnið oftast eða sjö sinnum hvor, flest lög eru í dúr og eru 120-130 bpm sem gefur til kynna að flest lög eru hress og flokkast sem popp-tónlist eða diskó lög. Stig Íslands voru einnig borin saman við stig Svíþjóðar, og kom í ljós að Ísland veitir Svíþjóð flest sín stig. Hins vegar er Ísland aðeins í 10. sæti hjá Svíþjóð. Annars eiga Ísland og Svíþjóð það sameiginlegt að gefa og fá flest sín stig frá Norðurlöndunum. 

# Möppustrúktúr
```bash
.
├── config/
│   └── __init__.py
├── data/
│   ├── __init.py
│   ├── keppnir.py
│   └── lengdKeppna.py
├── logic/
│   ├── __init.py
│   ├── keppnir.py
│   └── lengdKeppna.py
├── models/
│   ├── __init__.py
│   ├── keppnir.py
│   └── lengdKeppna.py
├── myndir /
│   ├── graf1.png
│   ├── graf10.png
│   ├── graf2.png
│   ├── graf3.png
│   ├── graf4.png
│   ├── graf5.png
│   ├── graf6.png
│   ├── graf7.png
│   ├── graf8.png
│   ├── graf9.png
│   ├── tengsl1.png
│   └── tengsl2.png
├── .env
├── .gitignore
├── Capstone.pbix
├── Capstone2.pbix
├── FogSF.csv
├── fromISL.csv
├── FromSE.csv
├── ISLpoints.csv
├── lengdogvote.csv
├── LICENSE
├── losers.csv
├── main.py
├── main3.py
├── main4.py
├── main5.py
├── main6.py
├── main7.py
├── main8.py
├── main9.py
├── main10.py
├── main11.py
├── README.md
├── SEpoints.csv
├── skyrsla.md
├── start.sh
├── TeleVsJury.csv
├── TontegundOgBPM.csv
├── winners
└── winners.csv
```

# Nauðsynleg forrit og uppsetning
## Sækja PowerBI 
- Fyrir **mac:** 
1. Einfaldasta leiðin er að nota vefútgáfuna sem má finna hér: https://app.powerbi.com/home?experience=power-bi.
Þar sem Power BI er Microsoft forrit þá er ekki hægt að nota það á sama máta og með windows stýrikerfi. 

- Fyrir **Windows:**
1. Hægt er að downloada forritinu Power BI með því að fara inná Microsoft Store. 
2. Fyrst þarf að download SQLite ODBC 64 bits (ekki 32 bits) inn á tölvuna
3. Opna ODBC, smella á *Add…*
4. Velja SQlite3 ODBC Driver
5. Velja CSV skrána sem þú vilt nota
6. Opna Power BI
7. Búa til nýtt report
8. Ýta á Get data → more → ODBC
9. Þá ætti skráin að birtast, ýta á Windows (ekki vera inná Database) og ýta á að halda áfram
10. Þá opnast Navigator og hakað í þær töflur sem á að nota við gerð grafa

## Sækja **Python**
1. Hægt er að sækja Python á þessari slóð https://www.python.org/downloads/
2. Ýtir á *Download Python 3.13.0* fyrir gerð tölvunnar sem verið er að nota

## Sækja **Datagrip**
- Fyrir **mac:** 
Þarf að fara inn á þessa slóð: https://www.jetbrains.com/datagrip/download/#section=mac
- Fyrir **Windows:** 
Þarf að fara inn á þessa slóð: https://www.jetbrains.com/datagrip/download/#section=windows

## Sækja **Docker**
1. Hægt að downloada forritinu með þessari slóð: https://www.docker.com/
2. Ýta á `Download Docker Desktop` og velja þar gerð tölvu sem verið er að nota
3. Skrifa í Terminal: `docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -p 5432:5432 -d postgres`

Setja upp env skrá með neðantöldum breytum:
```bash
DB_NAME = 
DB_USER = 
DB_PASSWORD = 
DB_HOST = 
DB_PORT = 
```
## Hlaða niður pakkanum “pandas”
Skrifa í Terminal til að hlaða niður: `Pip install pandas`.
Efst uppi á að standa: `Import pandas as pd`

## Opna .pbic skrána til að skoða mælaborðið 
**Windows:**
Opnið skránna `Capstone.pbix.`
Ýtið á `view raw` til að opna skránna.

# Keyrsla á kóðanum 
Til þess að keyra kóðana er nóg að skrifa í terminal  `./start.sh` (þá birtast allar skrár).
Ef þú vilt keyra ákveðna skrá en nóg að skrifa í terminal `python3 (nafn á skrá).py`

# ATH: Tenging gagna og mælaborðs
Þess má geta að tvær töflur voru unnar í Postgres og voru þær notaðar til að gera fyrstu tvö gröfin í mælaborðinu. 
Graf 1: *Sýnir staðsetningu keppna*
Graf 2: *Lengd Eurovision frá upphafi*

## Í forrituninni: 
Í möppunni config sér um að lesa inn kerfisbreytur
Í möppunni data sér um að vista í grunni og tengjast postgres (keppnir, lengdKeppna)
Í möppunni logic má finna kóða sem skrapar og vinnur gögnin. 
Í models inniheldur klasa sem restin í forritinu getur notað. 

Hinar töflurnar voru úr csv.skrám. 
Hér að neðan má sjá hvaða .py skrá og .csv skrá á við um hvaða graf í mælaborði:
