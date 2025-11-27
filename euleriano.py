def tem_caminho_ou_ciclo_euleriano(grafo):
    graus = {v: len(grafo[v]) for v in grafo}
    impares = [v for v in graus if graus[v] % 2 != 0]

    if len(impares) == 0:
        return "ciclo"
    elif len(impares) == 2:
        return "caminho"
    else:
        return None


def gerar_caminho_euleriano(grafo):
    g = {v: list(grafo[v]) for v in grafo}
    
    impares = [v for v in g if len(g[v]) % 2 != 0]

    if len(impares) == 0:
        atual = list(g.keys())[0]  
    else:
        atual = impares[0]

    caminho = []
    pilha = [atual]

    while pilha:
        v = pilha[-1]

        if g[v]:
            u = g[v].pop()
            g[u].remove(v)
            pilha.append(u)
        else:
            caminho.append(pilha.pop())

    return caminho[::-1] 


def executar_euleriano(grafo):
    tipo = tem_caminho_ou_ciclo_euleriano(grafo)

    if tipo is None:
        print("\nNão existe caminho nem ciclo euleriano.")
        return

    print(f"\nExiste {tipo} euleriano!")
    caminho = gerar_caminho_euleriano(grafo)
    print("Caminho encontrado:")
    print(" -> ".join(caminho))
