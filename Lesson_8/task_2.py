# 2. Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.


g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]


def dijkstra(graph, start):
    length = len(graph)
    is_visited = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length
    ways = []

    current = start
    cost[current] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_visited[current] = True

        for i, vertex in enumerate(graph[current]):
            if vertex != 0 and not is_visited[i]:

                if cost[i] > vertex + cost[current]:
                    cost[i] = vertex + cost[current]
                    parent[i] = current

        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                current = i

    for i in range(length):
        if cost[i] != float('inf'):
            goal = i
            way = [goal, ]

            while goal != start:
                goal = parent[goal]
                way.append(goal)

            way.reverse()
            ways.append(way)
        else:
            ways.append(None)

    return cost, ways


s = int(input('От какой вершины идти: '))
cost, way = dijkstra(g, s)

for i in range(len(cost)):
    print(f'Цена пути до вершины {i:3d} = {cost[i]},\tмаршрут: {way[i]}')
