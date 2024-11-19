import requests
import re
import pandas as pd

URL = 'https://eschome.net/databaseoutput429.php'
REGEX_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)</table>"
REGEX_GROUPS = r"<td align='.*'>\s*(.*?)\s*</td>"

response = requests.post(URL, data=
{
    "year_from": 2004,
    "year_to": 2024
})

text = response.text
table = re.search(REGEX_TABLE, text).group(1)

groups = re.findall(REGEX_GROUPS, table)

values = []
OFFSET = 6
for i in range(0, len(groups), OFFSET):
    val = groups[i:i+OFFSET]
    val.pop(0)
    val.pop(4)
    values.append(val)

df = pd.DataFrame(values)
df.to_csv('FogSF.csv', index=False, header=["Land", "semifinal", "Final","Final(%)"])