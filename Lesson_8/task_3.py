# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).

n = int(input('Введите число вершин: '))
start = int(input('Введите начальную точку: '))


def graph(n):
    a = dict([(i, 0) for i in range(n)])

    for i in a:
        b = [i for i in range(n)]
        b.pop(i)
        a[i] = b
    return a


def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for i in graph[node]:
            dfs(graph, i, visited)
    return visited


print('Сгенерированный граф', graph(n))
print('Путь обхода графа', dfs(graph(n), start, []))
