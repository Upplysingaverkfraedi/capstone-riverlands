import requests
import pandas as pd
from io import StringIO

URL = "https://github.com/Spijkervet/eurovision-dataset/releases/download/2023/contestants.csv"

request = requests.get(URL)
text = request.text

df = pd.read_csv(StringIO(text))

selected_columns = ['year', 'points_tele_final', 'points_jury_final', 'points_tele_sf', 'points_jury_sf']
df = df[selected_columns]
df.to_csv('TeleVsJury.csv')