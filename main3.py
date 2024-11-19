import requests
import re
import pandas as pd

URL = "https://eschome.net/databaseoutput402.php"
REGEX_GET_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)<\/table>"
REGEX_GROUPS = r"<td align='.*'>\s*(.*?)\s*<\/td>"

response = requests.get(URL)
text = response.text
table_match = re.search(REGEX_GET_TABLE, text)
table_str = table_match.group(1)

groups = re.findall(REGEX_GROUPS, table_str)

values = []
OFFSET = 7
for i in range(0, len(groups), OFFSET):
    val = groups[i:i + OFFSET]
    val.pop(3)
    values.append(val)


df = pd.DataFrame(values)
df.to_csv('winners.csv', index=None, header=["Ár", "Stig", "Nr", "Land", "Perfomer", "Lag"])



