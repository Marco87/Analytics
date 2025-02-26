<details>
<summary><strong>🤖Prompt para a criação da base de dados🤖</strong></summary>

# 📌 **Comandos Prompts Utilizados para Criar a Base de Dados**

## **1️⃣ Definição do Tema**
**Prompt:**  
> "Pensei em criar dashboards de exemplos com algumas funções como CALCULATE, ALL, ALLEXCEPT, SUMX."

## **2️⃣ Escolha do Tema da Base de Dados**
**Prompt:**  
> "Podemos fazer sobre o tema Vendas e começar criando um conjunto de dados fictícios."

## **3️⃣ Geração Inicial da Base de Dados**
**Prompt:**  
> "Quero que você gere os arquivos Excel para essa base de dados."

## **4️⃣ Ajuste na Quantidade de Linhas**
**Prompt:**  
> "Pode gerar os arquivos Excel. Mas preciso que eles tenham mais linhas. O exemplo que você gerou tem poucas linhas."

## **5️⃣ Solicitação de Métricas e Medidas DAX**
**Prompt:**  
> "Quero sugestões de visuais para esta base de dados, além também de sugestões de cálculos complexos em DAX."

## **6️⃣ Estruturação dos Visuais no Dashboard**
**Prompt:**  
> "Quero um mockup, e também quero que os visuais sejam divididos em telas por temas específicos."

## **7️⃣ Inclusão de Indicadores de Devoluções e Reclamações**
**Prompt:**  
> "A Tela 4 tem indicadores de devoluções e reclamações. Temos essa informação na base de dados?"

## **8️⃣ Atualização da Base com Novas Colunas**
**Prompt:**  
> "Quero que a base contenha colunas de devoluções e reclamações."

## **9️⃣ Detalhamento dos Visuais e Métricas**
**Prompt:**  
> "Na parte de visuais essenciais, quero que detalhe os gráficos que vou usar e as métricas que usarei em cada gráfico."

## **🔟 Estruturação dos Comandos Utilizados**
**Prompt:**  
> "Quero que você estruture, no formato de markdown, os comandos prompts que dei para a criação da base de dados."

</details>


<details>
<summary><strong>📊Estrutura do Dashboard📊</strong></summary>

**Dashboard de Vendas - Estrutura das Telas**

## **📌 Estrutura das Telas do Dashboard**

### **📍 Tela 1 - Visão Geral**
**Objetivo**: Resumo das principais métricas para uma rápida análise do desempenho geral.  
**Visuais**:
- **KPIs Principais**: 
  - Total de Vendas (`SUM(Valor_Venda)`) 
  - Ticket Médio (`DIVIDE(SUM(Valor_Venda), COUNT(ID_Pedido))`)
  - Receita Acumulada (YTD) (`TOTALYTD(SUM(Valor_Venda), 'Calendário'[Data])`)
  - Crescimento Percentual (`VAR Atual = SUM(Valor_Venda) VAR Anterior = CALCULATE(SUM(Valor_Venda), SAMEPERIODLASTYEAR('Calendário'[Data])) RETURN DIVIDE(Atual - Anterior, Anterior, 0)`) 
- **Gráfico de Tendência** (Linha): Evolução das vendas ao longo do tempo (`SUM(Valor_Venda) por 'Calendário'[Data]`).
- **Mapa Geográfico**: Faturamento por Estado/Cidade (`SUM(Valor_Venda) agrupado geograficamente`).

---

### **📍 Tela 2 - Análise de Vendas**
**Objetivo**: Detalhamento do comportamento das vendas.  
**Visuais**:
- **Ranking de Vendedores** (Gráfico de Barras): 
  - `SUM(Valor_Venda) por Vendedor`.
- **Produtos Mais Vendidos** (Gráfico de Colunas): 
  - `SUM(Valor_Venda) por Produto`.
- **Comparação de Vendas por Categoria** (Gráfico de Colunas Clusterizado): 
  - `SUM(Valor_Venda) por Categoria`.
- **Participação por Canal de Vendas** (Gráfico de Rosca): 
  - `SUM(Valor_Venda) por Canal_Venda`.

---

### **📍 Tela 3 - Análise de Clientes (RFM)**
**Objetivo**: Identificar padrões de clientes.  
**Visuais**:
- **Segmentação RFM** (Gráfico de Dispersão): 
  - `Clientes segmentados com base em Recência, Frequência e Valor Monetário`.
- **Frequência de Compra** (Gráfico de Barras): 
  - `COUNT(ID_Pedido) por Cliente`.
- **Recência x Valor Gasto** (Gráfico de Colunas): 
  - `Dias desde última compra x SUM(Valor_Venda)`.

---

### **📍 Tela 4 - Indicadores de Qualidade e Devoluções**
**Objetivo**: Monitorar problemas que impactam as vendas.  
**Visuais**:
- **Devoluções por Categoria** (Gráfico de Colunas): 
  - `SUM(Qtd_Devolucoes) por Categoria`.
- **Motivos de Devolução** (Gráfico de Rosca): 
  - `COUNT(ID_Pedido) por Motivo_Devolucao`.
- **Percentual de Pedidos com Reclamações** (Cartões KPI): 
  - `DIVIDE(COUNTROWS(FILTER(Tabela_Vendas, Tabela_Vendas[Reclamacao] = "Sim")), COUNTROWS(Tabela_Vendas), 0)`. 

---

</details>
