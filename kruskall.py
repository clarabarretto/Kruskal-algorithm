adelaide_data = open('adelaide.CSV', 'r').readlines()[1:201] # a primeira linha é o título e não faz parte dos dados
adelaide_data

# Formatação do dataset
i = 0

v = []
e = []

for data in adelaide_data:
  data_set = adelaide_data[i]
  info = data_set.split(',')

  i+=1

  trip_id = info[0]
  stop_id = info[2]
  n_boarding = info[-1]

  if trip_id not in v:
    v.append(trip_id)

  if stop_id not in v:
    v.append(stop_id)

  p =  n_boarding
  remove = ' "'
  peso = int(p.translate(str.maketrans('', '', remove)))  # transforma em valor inteiro
  v1, v2 = info[0].translate(str.maketrans('', '', remove)), info[2].translate(str.maketrans('', '', remove))
  aresta = (peso, v1, v2)

  e.append(aresta)

v = [elem.replace('"', '') for elem in v]

# Classes e métodos
class KruskalMST:  # Minimum Spanning Tree (Kruskal)

    def __init__(self, vertices, edges):  # método construtor
        self.vertices = vertices
        self.edges = edges  # arestas
        self.parent = {v: v for v in vertices}  # nó pai (família/subconjunto); cada nó é pai dele mesmo originalmente (várias árvores unitárias)
        self.rank = {v: 0 for v in vertices}  # classificação (quantidade de itens que fazem parte da família/subconjunto)

    def find(self, v):  # retorna a raíz de um nó v
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])

        return self.parent[v]

    def union(self, v1, v2):  # une dois vértices que não pertencem a um(a) mesmo(a) subconjunto/família
        root1 = self.find(v1)
        root2 = self.find(v2)
        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
                self.rank[root1] += self.rank[root2]

            else:
                self.parent[root1] = root2
                self.rank[root2] += self.rank[root1]

    def kruskal(self):  # retorna o grafo da árvore geradora mínima
        Tree = []
        e = sorted(self.edges)  # organiza arestas pelo peso ascendentemente
        while len(e) > 0:
            aresta = e.pop(0)  # aresta de menor peso
            if aresta not in Tree:
                peso, v1, v2 = aresta

                if self.find(v1) != self.find(v2):
                    self.union(v1, v2)
                    Tree.append(aresta)

        return Tree

# Saída da árvore geradora mínima de Kruskal
mst = KruskalMST(v, e).kruskal()
print(mst)

# Pontuação extra
# Função para a vizualização do grafo
import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
G = nx.Graph()
for aresta in mst:
    peso, v1, v2 = aresta
    G.add_edge(v1, v2, weight=peso)

# Desenhando o grafo
pos = nx.spring_layout(G)  # posição dos vértices
labels = nx.get_edge_attributes(G, 'weight')  # rótulos das arestas

nx.draw_networkx_nodes(G, pos, node_color='pink', node_size=600)
nx.draw_networkx_edges(G, pos, edge_color='black')
nx.draw_networkx_labels(G, pos, font_size = 7)
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.axis('off')

plt.show()  # exibir o gráfico
