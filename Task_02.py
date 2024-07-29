import networkx as nx
import matplotlib.pyplot as plt

# Створення графа з першого завдання
G = nx.Graph()
nodes = ['A', 'B', 'C', 'D', 'E']
G.add_nodes_from(nodes)
edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'E')]
G.add_edges_from(edges)

# Функція для пошуку шляхів за допомогою DFS
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

# Функція для пошуку шляхів за допомогою BFS
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in set(graph.neighbors(vertex)) - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Застосування DFS та BFS для пошуку шляхів з A до E
start_node = 'A'
goal_node = 'E'
dfs_result = list(dfs_paths(G, start_node, goal_node))
bfs_result = list(bfs_paths(G, start_node, goal_node))

# Виведення результатів
print("Шляхи знайдені за допомогою DFS:")
for path in dfs_result:
    print(path)

print("\nШляхи знайдені за допомогою BFS:")
for path in bfs_result:
    print(path)

# Запис висновків у файл readme.md
conclusions = """
# Висновки

## DFS (Глибина Пошуку)
DFS знаходить шлях з глибокими переходами. Для даного графа шляхи знайдені за допомогою DFS:

{}

## BFS (Ширина Пошуку)
BFS знаходить шлях шляхом поступового розширення від початкової вершини. Для даного графа шляхи знайдені за допомогою BFS:

{}

## Порівняння
Основна різниця між DFS та BFS полягає в підході до пошуку. DFS йде в глибину, тоді як BFS досліджує кожен рівень перед переходом на наступний. Це може призвести до різних шляхів для тих же самих початкової та кінцевої вершин.
""".format(dfs_result, bfs_result)

with open("readme.md", "w", encoding="utf-8") as file:
    file.write(conclusions)
