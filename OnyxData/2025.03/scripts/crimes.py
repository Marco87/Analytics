import pandas as pd
from pathlib import Path

arquivo = Path("OnyxData/2025.03/data/washington_crimes_dataset.xlsx")

if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo.resolve()}")

df = pd.read_excel(arquivo, sheet_name="Onyx Data -DataDNA Dataset Chal")

df[['END_DATE', 'END_HOUR']] = df['END_DATE'].str.split(', ', expand=True)
df[['REPORT_DATE', 'REPORT_HOUR']] = df['REPORT_DAT'].str.split(', ', expand=True)
df[['START_DATE', 'START_HOUR']] = df['START_DATE'].str.split(', ', expand=True)
df["END_DATE"] = pd.to_datetime(df["END_DATE"], format="%m/%d/%Y")
df["REPORT_DATE"] = pd.to_datetime(df["REPORT_DATE"], format="%m/%d/%Y")
df["START_DATE"] = pd.to_datetime(df["START_DATE"], format="%m/%d/%Y")

df = df.astype({
    "LATITUDE": "float",
    "LONGITUDE": "float",
    "YBLOCK": "float",
    "XBLOCK": "float",
    "CCN": "Int64",
    "PSA": "Int64",
    "CENSUS_TRACT": "Int64",
    "WARD": "Int64",
    "DISTRICT": "Int64",
    "ucr-rank": "Int64"
})

df = df.drop(columns=["location", "offense-text", "offensekey", "OCTO_RECORD_ID", "YEAR", "REPORT_DAT"])
df.to_excel("OnyxData/2025.03/data/washington_crimes.xlsx", index=False)

print("Processo concluído! Novo arquivo salvo como 'washington_crimes_cleaned.xlsx'.")