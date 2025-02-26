<details>
<summary><strong>🤖Prompts utilizados para a criação da base de dados🤖</strong></summary>


# 📌 **Comandos Prompts Utilizados para Criar a Base de Dados**

## **1️⃣ Definição do Tema**
**Prompt:**  
> "Pensei em criar dashboards de exemplos com algumas funções como CALCULATE, ALL, ALLEXCEPT, SUMX, etc..."

## **2️⃣ Escolha do Tema da Base de Dados**
**Prompt:**  
> "Podemos fazer sobre o tema Vendas e começar criando um conjunto de dados fictícios."

## **3️⃣ Geração Inicial da Base de Dados**
**Prompt:**  
> "Quero que você gere os arquivos Excel para essa base de dados."

## **4️⃣ Ajuste na Quantidade de Linhas**
**Prompt:**  
> "Quero sim. Pode gerar os arquivos Excel. Mas preciso que eles tenham mais linhas. O exemplo que você gerou tem poucas linhas."

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
> "Sim. Quero que a base contenha colunas de devoluções e reclamações."

## **9️⃣ Detalhamento dos Visuais e Métricas**
**Prompt:**  
> "Na parte de visuais essenciais, quero que detalhe os gráficos que vou usar e as métricas que usarei em cada gráfico."

## **🔟 Estruturação dos Comandos Utilizados**
**Prompt:**  
> "Quero que você estruture, no formato de markdown, os comandos prompts que dei para a criação da base de dados."

</details>


<details>
<summary><strong>📊Especificações do Dashboard📊</strong></summary>

# 📊 **Estrutura do Dashboard de Vendas**

## **📌 Estrutura das Telas**

### **📍 Tela 1 - Visão Geral**
**Objetivo**: Apresentar um resumo das principais métricas para uma rápida análise do desempenho geral.  
**Visuais**:
- **KPIs Principais**:
  - Total de Vendas  
  - Ticket Médio  
  - Receita Acumulada (YTD)  
  - Crescimento Percentual  
- **Gráfico de Tendência** (Linha): Evolução das vendas ao longo do tempo.  
- **Mapa Geográfico**: Faturamento por Estado/Cidade.  

---

### **📍 Tela 2 - Análise de Vendas**
**Objetivo**: Fornecer um detalhamento do comportamento das vendas.  
**Visuais**:
- **Ranking de Vendedores** (Gráfico de Barras)  
- **Produtos Mais Vendidos** (Gráfico de Colunas)  
- **Comparação de Vendas por Categoria** (Gráfico de Colunas Clusterizado)  
- **Participação por Canal de Vendas** (Gráfico de Rosca)  

---

### **📍 Tela 3 - Análise de Clientes (RFM)**
**Objetivo**: Identificar padrões de compra dos clientes com base na segmentação RFM.  
**Visuais**:
- **Segmentação RFM** (Gráfico de Dispersão)  
- **Frequência de Compra** (Gráfico de Barras)  
- **Recência x Valor Gasto** (Gráfico de Colunas)  

---

### **📍 Tela 4 - Indicadores de Qualidade e Devoluções**
**Objetivo**: Monitorar problemas que impactam as vendas.  
**Visuais**:
- **Devoluções por Categoria** (Gráfico de Colunas)  
- **Motivos de Devolução** (Gráfico de Rosca)  
- **Percentual de Pedidos com Reclamações** (Cartão KPI)  

---

## **📁 Estrutura dos Dados**
A base de dados contém as seguintes colunas principais:
- **Data do Pedido**
- **ID do Pedido**
- **Cliente**
- **Vendedor**
- **Categoria do Produto**
- **Produto**
- **Valor da Venda**
- **Canal de Venda**
- **Região**
- **Quantidade Devolvida**
- **Motivo da Devolução**
- **Reclamação** (Sim/Não)

---

Essa estrutura garante que o dashboard seja bem organizado e segmentado por temas, facilitando a análise de dados. 🚀  
Se precisar de ajustes, me avise!  

</details>
