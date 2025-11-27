def hamiltoniano_backtracking(grafo, atual, visitados, caminho_final):
    visitados.add(atual)
    caminho_final.append(atual)

    if len(visitados) == len(grafo):
        return True

    for viz in grafo[atual]:
        if viz not in visitados:
            if hamiltoniano_backtracking(grafo, viz, visitados, caminho_final):
                return True

    visitados.remove(atual)
    caminho_final.pop()
    return False


def encontrar_caminho_hamiltoniano(grafo):
    for v in grafo:
        visitados = set()
        caminho = []
        if hamiltoniano_backtracking(grafo, v, visitados, caminho):
            return caminho
    return None


def executar_hamiltoniano(grafo):
    caminho = encontrar_caminho_hamiltoniano(grafo)
    if caminho:
        print("\nCaminho Hamiltoniano encontrado:")
        print(" -> ".join(caminho))
    else:
        print("\nNão existe caminho Hamiltoniano para este grafo.")
