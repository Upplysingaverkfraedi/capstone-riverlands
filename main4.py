import requests
import re
import pandas as pd

URL = "https://eschome.net/databaseoutput419.php"
REGEX_GET_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)<\/table>"
REGEX_GROUPS = r"<td align='.*'>\s*(.*?)\s*<\/td>"

response = requests.get(URL)
text = response.text
table_match = re.search(REGEX_GET_TABLE, text)
table_str = table_match.group(1)

groups = re.findall(REGEX_GROUPS, table_str)

values = []
OFFSET = 8
for i in range(0, len(groups), OFFSET):
    val = groups[i:i + OFFSET]
    val.pop(4)
    values.append(val)


df = pd.DataFrame(values)
df.to_csv('losers.csv', index=None, header=["Ár", "Place", "Stig", "Nr", "Land", "Perfomer", "Lag"])



