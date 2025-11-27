from euleriano import executar_euleriano
from hamiltoniano import executar_hamiltoniano
from componentes import executar_componentes


def definir_vertices():
    n = int(input("Digite o número de vértices: "))
    vertices = []
    for i in range(n):
        nome = input(f"Nome do vértice {i+1}: ").upper()
        vertices.append(nome)
    return vertices


def criar_grafo(vertices):
    return {v: [] for v in vertices}


def inserir_aresta(grafo, vertices):
    origem = input("Origem: ").upper()
    destino = input("Destino: ").upper()

    if origem in vertices and destino in vertices:
        grafo[origem].append(destino)
        grafo[destino].append(origem)
        print(f"Aresta {origem} -- {destino} adicionada.")
    else:
        print("Vértice inválido!")


def mostrar_arestas(grafo):
    print("\nArestas do grafo:")
    tem = False
    for v in grafo:
        for adj in grafo[v]:
            print(f"{v} -- {adj}")
            tem = True
    if not tem:
        print("Nenhuma aresta.")

vertices = definir_vertices()
grafo = criar_grafo(vertices)

print("\n--- Cadastro das arestas ---")
while True:
    op = input("Inserir aresta? (s/n): ").lower()
    if op == "s":
        inserir_aresta(grafo, vertices)
    else:
        break

mostrar_arestas(grafo)

while True:
    print("\nEscolha a operação:")
    print("1 - Caminho/Ciclo Euleriano")
    print("2 - Caminho Hamiltoniano")
    print("3 - Componentes Conexas")
    print("0 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        executar_euleriano(grafo)
    elif escolha == "2":
        executar_hamiltoniano(grafo)
    elif escolha == "3":
        executar_componentes(grafo)
    elif escolha == "0":
        break
    else:
        print("Opção inválida!")

print("\nFim.")
