# MergeSort em C e Python

Relatório: https://docs.google.com/document/d/1w83m2CYYS56A47Yozz4oZcINjUA2YNiE_5s9zP5Hgto/edit?usp=sharing

---

Implementação do algoritmo **Merge Sort** em **C** e **Python**, com foco em análise de desempenho em diferentes tamanhos de listas (pequenas, médias e grandes).<br>
Predefinimos para lista ser pequena ela deve ter até 1000 números, para ela ser média ela deve ter entre 1000 e 10000 números e para ser grande deve ter mais de 10000 números.

---

## 🔍 Sobre o algoritmo

Merge Sort é um algoritmo de ordenação estável com complexidade **O(n log n)** em todos os casos. Funciona via **divide-e-conquista**:

1. Divide a lista em duas partes recursivamente
2. Ordena as partes individualmente
3. Junta as partes ordenadas

---

## 📊 Desempenho (tempo médio em segundos)

### Python

| Tipo     | Tempo médio |
|----------|-------------|
| Pequeno  | 0.00057     |
| Médio    | 0.014       |
| Grande   | 0.023       |

### C

| Tipo     | Tempo médio |
|----------|-------------|
| Pequeno  | 0.00011     |
| Médio    | 0.00296     |
| Grande   | 0.00572     |

---

## ✅ Quando usar

- Quando precisa de ordenação estável
- Para grandes volumes de dados
- Em sistemas paralelos

## ❌ Evite quando

- Há limitação de memória
- A lista já está quase ordenada
- Em sistemas embarcados

## Como Rodar?

- Rode o arquivo scriptGeracaoLista.py
- Cole a lista gerada no local indicado pela frase "Digite aqui a lista de números a serem ordenados"
- Rode o arquivo de ordenação mergesort