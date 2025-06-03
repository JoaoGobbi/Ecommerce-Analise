
# 🛍️ Análise de Dados E-commerce Olist — Segmentação de Clientes (RFM + Clusterização)

## 🔍 Objetivo
Aplicar técnicas de análise de dados para entender o comportamento dos clientes do e-commerce Olist, utilizando métricas de Recência, Frequência e Valor (RFM) combinadas com clusterização via KMeans.

---

## 🚀 Etapas do Projeto
- ✅ Carregamento dos dados brutos do Kaggle.
- ✅ Limpeza, transformação e enriquecimento dos dados.
- ✅ Análise de comportamento dos clientes via matriz RFM.
- ✅ Criação de clusters para segmentação dos clientes.
- ✅ Análise exploratória detalhada dos dados (EDA).
- ✅ Geração de insights visuais e estratégicos.

---

## 📈 Principais Resultados

| Cluster | Recência Média | Frequência Média | Valor Médio | Perfil                  |
|---------|-----------------|------------------|-------------|-------------------------|
| 0       | Alta            | Baixa            | Médio       | Clientes inativos       |
| 1       | Baixa           | Baixa            | Baixo       | Clientes recentes       |
| 2       | Média           | Alta             | Alto        | Melhores clientes       |
| 3       | Baixa           | Baixa            | Alto        | Compradores esporádicos |

---

## 💡 Insights e Ações Sugeridas
- 🎯 **Cluster 2 (Melhores clientes):** Foco em retenção, programas de fidelidade e ofertas exclusivas.
- 🔥 **Cluster 3 (Esporádicos de alto valor):** Incentivar recorrência através de campanhas personalizadas.
- ♻️ **Cluster 0 (Inativos):** Campanhas de reativação, cupons e ofertas específicas.
- 🚀 **Cluster 1 (Novos/Recentes):** Estratégias para converter em clientes recorrentes.

---

## 🗺️ Arquitetura do Projeto

```
ecommerce-olist-analysis/
├── data/
│   ├── raw/           → Dados brutos
│   └── processed/     → Dados processados e outputs
├── notebooks/         → Análises exploratórias e geração de gráficos
├── reports/
│   └── figures/       → Gráficos gerados
├── src/               → Scripts Python
├── tests/             → Testes unitários
├── main.py            → Pipeline principal
├── README.md          → Este arquivo
├── requirements.txt   → Dependências
```

---

## 🛠️ Tecnologias Utilizadas
- Python (Pandas, Numpy, Matplotlib, Seaborn, Scikit-learn)
- Jupyter Notebook
- VSCode
- Git + GitHub

---

## 👨‍💻 Como Rodar o Projeto

```bash
# Clone este repositório
git clone https://github.com/JoaoGobbi/Ecommerce-Analise.git

# Acesse a pasta do projeto
cd ecommerce-olist-analysis

# Instale as dependências
pip install -r requirements.txt

# Execute o pipeline completo
python main.py
```

---

## 🎨 Gráficos Gerados

- 📊 Análise exploratória dos dados (EDA)
- 📊 Distribuição dos scores R, F, V
- 📊 Distribuição dos clientes por cluster
- 📊 Dispersão: Frequência vs Valor colorido pelos clusters

Todas as figuras estão disponíveis na pasta:

```
/reports/figures
```

---

## ✅ Projeto finalizado com sucesso e pronto para portfólio no GitHub!
