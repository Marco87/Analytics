import pandas as pd

# Caminho correto do arquivo (voltando um nível e entrando na pasta "data")
arquivo = "../data/Onyx Data -DataDNA Dataset Challenge - Washington Crimes Dataset - March 2025.xlsx"

# Carregar a aba "Data Dictionary", ignorando as três primeiras linhas e pegando apenas a primeira coluna
df = pd.read_excel(arquivo, sheet_name="Data Dictionary", header=None, skiprows=3, usecols=[0])

# Separar os nomes dos itens (linhas ímpares) e descrições (linhas pares)
nomes = df.iloc[::2, 0].reset_index(drop=True)  # Pegando linhas ímpares a partir da linha 4
descricoes = df.iloc[1::2, 0].reset_index(drop=True)  # Pegando linhas pares a partir da linha 5

# Criar um novo DataFrame com duas colunas
df_final = pd.DataFrame({"Nome do Item": nomes, "Descrição": descricoes})

# Salvar em um novo arquivo Excel no mesmo diretório do script
df_final.to_excel("dicionario_dados_corrigido.xlsx", index=False)

print("Processo concluído! Novo arquivo salvo como 'dicionario_dados_corrigido.xlsx'.")
