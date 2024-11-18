import requests
import re
import pandas as pd

URL = 'https://eschome.net/databaseoutput427.php'
REGEX_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)</table>"
REGEX_GROUPS = r"<td align='.*'>\s*(.*?)\s*</td>"

response = requests.post(URL, data=
{
    "art": 1,
    "direction": 1,
    "country_x": "IS",
    "year_from": 2004,
    "year_to": 2024
})

text = response.text
table = re.search(REGEX_TABLE, text).group(1)

groups = re.findall(REGEX_GROUPS, table)

values = []
OFFSET = 8
for i in range(0, len(groups), OFFSET):
    val = groups[i:i+OFFSET]
    val.pop(0)
    val.pop(6)
    values.append(val)

df = pd.DataFrame(values)
df.to_csv('FromISL.csv', index=False, header=["Land", "Stig", "Stig(%)","Votings", "Votings not null", "Votings not null (%)"])