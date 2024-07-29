import networkx as nx
import matplotlib.pyplot as plt

# Крок 2: Створення графа
G = nx.Graph()

# Додавання вершин
nodes = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodes)

# Додавання ребер (наприклад, транспортні зв'язки)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
G.add_edges_from(edges)

# Крок 3: Візуалізація графа
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15)
plt.title('Транспортний мережевий граф')
plt.show()

# Крок 4: Аналіз графа
# Кількість вершин та ребер
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

# Ступінь кожної вершини
degrees = dict(G.degree())

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
print("Ступінь кожної вершини:")
for node, degree in degrees.items():
    print(f"{node}: {degree}")
