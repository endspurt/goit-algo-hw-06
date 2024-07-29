import networkx as nx
import matplotlib.pyplot as plt

# Створення графа з вагами ребер
G = nx.Graph()

# Додавання вершин
nodes = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodes)

# Додавання ребер з вагами (наприклад, транспортні зв'язки з відстанями)
edges = [('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 4), ('C', 'D', 1), ('D', 'E', 3)]
G.add_weighted_edges_from(edges)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиції для всіх вершин
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, edge_color='gray', font_size=15)

# Додавання ваг ребер на граф
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title('Граф з вагами ребер')
plt.show()

# Виконання алгоритму Дейкстри для пошуку найкоротшого шляху з A до E
start_node = 'A'
goal_node = 'E'
shortest_path = nx.dijkstra_path(G, start_node, goal_node)
shortest_path_length = nx.dijkstra_path_length(G, start_node, goal_node)

# Виведення результатів
print(f"Найкоротший шлях з {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_path_length}")
