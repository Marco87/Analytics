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

