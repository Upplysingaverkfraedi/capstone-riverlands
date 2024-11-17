import requests
import pandas as pd
import json

URL = "https://raw.githubusercontent.com/josago97/EurovisionDataset/refs/heads/main/dataset/eurovision.json"

request = requests.get(URL)
text = request.text

parsed = json.loads(text)

results = []
for i in parsed:
    contestants = i['contestants']

    for c in contestants:
        results.append(c)

df = pd.DataFrame(results)

selected_columns = ['country', 'song', 'tone', 'bpm']
df = df[selected_columns]
df.to_csv('TontegundOgBPM.csv', index=None)