"""
Pandas

Egy C- ben megírt third party data library
amivel az adat vizsgálat, feldolgozás műveleteket tudjuk optimalizálni
az által , hogy nagyon sok funkció előre le van fejlesztve

"""

import pandas as pd

filename = r"C:\2025-project\data\constructor_results.csv"

df = pd.read_csv(filepath_or_buffer=filename)
json_data = df.to_dict(orient="records")

df.fillna(0, inplace=True)
# print(json_data)
print(df['constructorResultsId'].median())

# print(df.columns)
# print(df.dtypes)
# print(df['constructorResultsId']) # egy oszlop lekérése
# print(df[['constructorResultsId', 'raceId']].columns) # object - string

