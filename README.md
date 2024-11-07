# Verkefnalýsing
Verkefnið fól í sér að útbúa og hanna mælaborð sem lýsti samanburði milli Svíþjóðar og Íslands í söngvakeppninni Eurovision á 20 ára tímabili eða milli 2004-2024. Ástæðan af hverju ofantöld lönd voru valin, þau taka keppninni hvað alvarlegast af öllum löndum en hafa samt sem áður notið mjög ólíkrar velgengni í gegnum árin.  

# Niðurstöður
Ýmsar áhugaverðar niðurstöður komu í ljós við gerð mælaborðsins. Þar má meðal annars sjá að hvernig uppröðun atriða getur haft áhrif á velgengni landa í keppninni; best er að vera 16. í röðinni eða seinna. Svíþjóð og Írland hafa unnið oftast eða 8 sinnum hvor, flest lög eru í Dúr og með taktgildinu (bpm) 12-130 sem gefur til kynna að flest lög eru hress og flokkast sem electro-pop eða disco lög.  Einnig voru stig Íslands borin saman við Svíþjóðar og kom þá í ljós að Ísland gefur Svíþjóð flest sín stig en Ísland er ekki nema númer 10 hjá Svíþjóð. Áhugavert var þó að sjá að Mónakó og Ungverjaland gefa Íslandi hlutfallslega mörg stig. Annars eiga Ísland og Svíþjóð það sameiginlegt að gefa og fá sín stig frá Norðurlöndunum. 

# Möppustrúktúr
```bash
.
├── FogSF.csv
├── fromISL.csv
├── FromSE.csv
├── ISLpoints.csv
├── LICENSE
├── README.md
├── SEpoints.csv
├── TeleVsJury.csv
├── TontegundOgBPM.csv
├── fromISL.csv
├── keppnihaldin.csv
├── lengdogvote.csv
├── losers.csv
├── main.py
├── main2.py
├── main3.py
├── main4.py
├── main5.py
├── main6.py
├── main7.py
├── main8.py
├── main9.py
├── main10.py
├── main11.py
├── winners
└── winners.csv
```
# Nauðsynleg forrit og uppsetning
## Sækja PowerBI 
- Fyrir **mac** 
Þarf að fara inn á þessa slóð: https://app.powerbi.com/home?experience=power-bi
Þar sem PowerBI vefsíðan er aðeins hægt að nota á mac, ekki sjálft forritið.
- Fyrir **Windows**
Hægt er að downloada forritinu PowerBI með því að fara inná Microsoft Store. 
- Sækja **Python**
Hægt er að sækja Python á þessari slóð: https://www.python.org/downloads/

Hlaða niður pakkanum “pandas”
`Import pandas as pd`
Skrifa í Terminal til að hlaða niður: `Pip install pandas`

**Opna .pbic skrána til að skoða mælaborðið:**
Aðeins hægt í Windows. 
1. Opnið skránna Capstone2.pbix.
2. Ýtið á view raw til að opna skránna. 


# Keyrsla á kóðanum 
Til þess að keyra kóðann er nóg að skrifa í terminal  `./start.sh` (þá birtast allar skrár)
Ef þú vilt keyra ákveðna skrá en nóg að skrifa í terminal `python3 (nafn á skrá).py`




