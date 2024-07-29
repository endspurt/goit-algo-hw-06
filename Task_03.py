import networkx as nx
import matplotlib.pyplot as plt
import heapq

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

# Реалізація алгоритму Дейкстри без використання готових рішень з бібліотеки
def dijkstra(graph, start):
    # Ініціалізація
    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    shortest_path_tree = {}
    
    while queue:
        (current_distance, current_node) = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight['weight']
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                shortest_path_tree[neighbor] = current_node
    
    return distances, shortest_path_tree

# Застосування алгоритму Дейкстри для пошуку найкоротшого шляху з A до E
start_node = 'A'
goal_node = 'E'
distances, shortest_path_tree = dijkstra(G, start_node)

# Відновлення шляху з shortest_path_tree
def get_shortest_path(tree, start, goal):
    path = [goal]
    while goal in tree:
        goal = tree[goal]
        path.append(goal)
    path.reverse()
    return path

shortest_path = get_shortest_path(shortest_path_tree, start_node, goal_node)
shortest_path_length = distances[goal_node]

# Виведення результатів
print(f"Найкоротший шлях з {start_node} до {goal_node}: {shortest_path}")
print(f"Довжина найкоротшого шляху: {shortest_path_length}")
