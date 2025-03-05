import pandas as pd
from pathlib import Path

arquivo = Path("OnyxData/2025.03/data/washington_crimes_dataset.xlsx")

if not arquivo.exists():
    raise FileNotFoundError(f"Arquivo não encontrado: {arquivo.resolve()}")

df = pd.read_excel(arquivo, sheet_name="Onyx Data -DataDNA Dataset Chal")

df[['START_DATE', 'START_HOUR']] = df['START_DATE'].str.split(', ', expand=True)
df["START_DATE"] = pd.to_datetime(df["START_DATE"], format="%m/%d/%Y")

def generate_calendar_table_from_dataframe(df, date_column='START_DATE'):
    df[date_column] = pd.to_datetime(df[date_column])

    start_date = df[date_column].min()
    end_date = df[date_column].max()

    date_range = pd.date_range(start=start_date, end=end_date)
    calendar = pd.DataFrame(date_range, columns=['Date'])

    calendar['Year'] = calendar['Date'].dt.year
    calendar['Month'] = calendar['Date'].dt.strftime('%B')
    calendar['YearMonth'] = calendar['Date'].dt.strftime('%Y.%b')
    calendar['YearMonth_No'] = calendar['Date'].dt.strftime('%Y%m')
    calendar['MonthYear'] = calendar['Date'].dt.strftime('%b.%Y')
    calendar['MonthNumber'] = calendar['Date'].dt.month
    calendar['Trim'] = 'Q' + calendar['Date'].dt.quarter.astype(str) + '° Quarter - ' + calendar['Date'].dt.year.astype(str)
    calendar['Sem'] = calendar['Date'].apply(lambda x: '1° Semester - ' if x.month <= 6 else '2° Semester - ') + calendar['Date'].dt.year.astype(str)
    calendar['Weekday'] = calendar['Date'].dt.strftime('%A')
    calendar['Weekday_No'] = calendar['Date'].dt.dayofweek + 1
    calendar['Weekday_No'] = calendar['Weekday_No'].replace({7:0})
    calendar['Weekday_No'] = calendar['Weekday_No'] +1


    return calendar

df_calendar = generate_calendar_table_from_dataframe(df)
df_calendar.to_excel("OnyxData/2025.03/data/data_calendar.xlsx", index=False)

print("Processo concluído! Novo arquivo salvo como 'data_calendar.xlsx'.")