import requests
import re
import pandas as pd

from data import KeppnirData
from models import Keppnir

# Constants
URL = "https://eschome.net/databaseoutput410.php"
REGEX_GET_TABLE = r"(?s)<table id='tabelle1'.*?>(.*?)<\/table>"
REGEX_GROUPS = r"<td align='left'>\s*(.*?)\s*<\/td>"

class KeppnirLogic():
    def __init__(self):
        self.__keppnir_data = KeppnirData()

    def save_keppnir(self):
        response = requests.get(URL)
        text = response.text

        table_match = re.search(REGEX_GET_TABLE, text)
        table_str = table_match.group(1)

        groups = re.findall(REGEX_GROUPS, table_str)

        values = []
        for i in range(0, len(groups), 7):
            val = groups[i:i + 7]
            val.pop(1)

            values.append(val)


        df = pd.DataFrame(values, columns=['year', 'country', 'city', 'location', 'broadcaster', 'date'])
        list_keppnir = [Keppnir(data['year'], data['country'], data['city'], data['location'], data['broadcaster'], data['date']) for _, data in df.iterrows()]

        self.__keppnir_data.insert_data(list_keppnir)



