# Projeto – Algoritmos de Grafos

### Caminho/Ciclo Euleriano • Caminho Hamiltoniano • Componentes Conexas

Este projeto implementa três algoritmos clássicos de Teoria dos Grafos,
cada um em seu próprio módulo Python.

**Módulos:**
- `euleriano.py` - Caminho e Ciclo Euleriano
- `hamiltoniano.py` - Caminho Hamiltoniano
- `componentes.py` - Componentes Conexas
- `main.py` - Programa Principal

---

## 📦 Dependências

Este projeto utiliza apenas a biblioteca padrão do Python, não requer instalação de pacotes externos.

**Requisitos:**
- Python 3.x

---

## 📌 Como executar

Execute o comando: `python main.py`

---

## 📝 Exemplos de Entrada e Saída

### Caminho/Ciclo Euleriano
**Grafo:** `A-B, B-C, C-D, D-A` (ciclo)

**Saída:** `A -> B -> C -> D -> A`

---

### Caminho Hamiltoniano
**Grafo:** `A-B, B-C, C-D, D-E, E-A`

**Saída:** `A -> B -> C -> D -> E`

---

### Componentes Conexas

Encontra todos os grupos de vértices conectados no grafo (componentes conexas).

**Entrada:**
- Vértices: `A, B, C, D, E, F`
- Arestas: `A-B, B-C, D-E`  

**Saída:**
- Componente 1: `['A', 'B', 'C']`
- Componente 2: `['D', 'E']`
- Componente 3: `['F']`
