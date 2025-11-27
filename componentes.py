def dfs(grafo, vertice, visitado, componente):
    visitado.add(vertice)
    componente.append(vertice)

    for vizinho in grafo[vertice]:
        if vizinho not in visitado:
            dfs(grafo, vizinho, visitado, componente)


def executar_componentes(grafo):
    visitado = set()
    componentes = []

    for vertice in grafo:
        if vertice not in visitado:
            componente = []
            dfs(grafo, vertice, visitado, componente)
            componentes.append(componente)

    print("\n=== COMPONENTES CONEXAS ENCONTRADAS ===")
    for i, comp in enumerate(componentes, 1):
        print(f"Componente {i}: {comp}")

