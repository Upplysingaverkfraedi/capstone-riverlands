import requests
import re
import pandas as pd

from data import LengdKeppnaData
from models import LengdKeppna

# Constants
URL = "https://eschome.net/databaseoutput434.php"
REGEX_GET_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)<\/table>"
REGEX_GROUPS = r"<td align='.*'>\s*(.*?)\s*<\/td>"

class LengdKeppnaLogic():
    def __init__(self):
        self.__lengd_keppna_data = LengdKeppnaData()

    def save_lengd_keppna(self):
        response = requests.get(URL)
        text = response.text
        table_match = re.search(REGEX_GET_TABLE, text)
        table_str = table_match.group(1)

        groups = re.findall(REGEX_GROUPS, table_str)

        values = []
        OFFSET = 10
        for i in range(0, len(groups), OFFSET):
            val = groups[i:i + OFFSET]
            values.append(val)


        df = pd.DataFrame(values, columns=["Ár", "Borg", "Show", "Lög", "Skemmtiatriði", "Voting", "Fyrstalag", "Seinastalag", "Fyrstavote", "Seinastavote"])
        list_length_competitions = [LengdKeppna(row['Ár'], row['Show'], row['Lög'], row['Skemmtiatriði'], row['Voting'], row['Fyrstalag'], row['Seinastalag'], row['Fyrstavote'], row['Seinastavote']) for _, row in df.iterrows()]
        
        self.__lengd_keppna_data.insert_data(list_length_competitions)