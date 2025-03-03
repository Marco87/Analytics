import pandas as pd

arquivo = "OnyxData/2025.03/data/washington_crimes.xlsx"

df = pd.read_excel(arquivo, sheet_name="Data Dictionary", header=None, skiprows=4, usecols=[0])

nomes = df.iloc[::2, 0].reset_index(drop=True)
descricoes = df.iloc[1::2, 0].reset_index(drop=True)

df_final = pd.DataFrame({"item": nomes, "description": descricoes})
df_final.to_excel("OnyxData/2025.03/data/data_dictionary.xlsx", index=False)

print("Processo concluído! Novo arquivo salvo como 'dicionario_dados_corrigido.xlsx'.")