import pandas as pd
from pathlib import Path

arquivo = Path("OnyxData/2025.03/data/washington_crimes_dataset.xlsx")

if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo.resolve()}")

df = pd.read_excel(arquivo, sheet_name="Onyx Data -DataDNA Dataset Chal")

df[['START_DATE', 'START_HOUR']] = df['START_DATE'].str.split(', ', expand=True)

def generate_hour_dimension_table(df, hour_column='START_HOUR'):
    unique_hours = df[hour_column].unique()
    hour_dimension = pd.DataFrame(unique_hours, columns=['START_HOUR'])

    hour_dimension['Time_Text'] = hour_dimension['START_HOUR'].astype(str)
    hour_dimension['Time_No'] = hour_dimension['START_HOUR'].str[:2].astype(int)

    def get_interval(hour_no):
        if 0 < hour_no <= 6:
            return "00:00 às 06:00"
        elif 6 < hour_no <= 12:
            return "06:00 às 12:00"
        elif 12 < hour_no <= 18:
            return "12:00 às 18:00"
        else:
            return "18:00 às 00:00"

    hour_dimension['Interval'] = hour_dimension['Time_No'].apply(get_interval)

    return hour_dimension

df_hour = generate_hour_dimension_table(df)

print(df_hour)
