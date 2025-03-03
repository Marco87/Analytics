import pandas as pd
from pathlib import Path

# Definir caminho do arquivo
arquivo = Path("OnyxData/2025.03/data/washington_crimes.xlsx")

# Verificar se o arquivo existe
if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo.resolve()}")

# Carregar a aba específica "Onyx Data -DataDNA Dataset Chal"
df = pd.read_excel(arquivo, sheet_name="Onyx Data -DataDNA Dataset Chal")

# 📌 1️⃣ Dividir colunas por delimitador ", "
df[['END_DATE', 'END_HOUR']] = df['END_DATE'].str.split(', ', expand=True)
df[['REPORT_DATE', 'REPORT_HOUR']] = df['REPORT_DAT'].str.split(', ', expand=True)
df[['START_DATE', 'START_HOUR']] = df['START_DATE'].str.split(', ', expand=True)

# 📌 2️⃣ Renomear colunas
df = df.rename(columns={
    "END_DATE": "END_DATE",
    "END_HOUR": "END_HOUR",
    "REPORT_DATE": "REPORT_DATE",
    "REPORT_HOUR": "REPORT_HOUR",
    "START_DATE": "START_DATE",
    "START_HOUR": "START_HOUR"
})

# 📌 3️⃣ Converter tipos de dados
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
    "YEAR": "Int64",
    "ucr-rank": "Int64"
})

# 📌 4️⃣ Converter colunas de data e hora
df["END_DATE"] = pd.to_datetime(df["END_DATE"], errors="coerce")
df["REPORT_DATE"] = pd.to_datetime(df["REPORT_DATE"], errors="coerce")
df["START_DATE"] = pd.to_datetime(df["START_DATE"], errors="coerce")

df["END_HOUR"] = pd.to_datetime(df["END_HOUR"], format="%H:%M:%S", errors="coerce").dt.time
df["REPORT_HOUR"] = pd.to_datetime(df["REPORT_HOUR"], format="%H:%M:%S", errors="coerce").dt.time
df["START_HOUR"] = pd.to_datetime(df["START_HOUR"], format="%H:%M:%S", errors="coerce").dt.time

# 📌 5️⃣ Remover colunas desnecessárias
df = df.drop(columns=["location", "offense-text", "offensekey", "OCTO_RECORD_ID"])

# 📌 6️⃣ Salvar o resultado em um novo arquivo Excel
df.to_excel("OnyxData/2025.03/data/washington_crimes_cleaned.xlsx", index=False)

print("Processo concluído! Novo arquivo salvo como 'washington_crimes_cleaned.xlsx'.")
