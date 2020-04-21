# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

n = int(input('Ввдедите количество друзей: '))
graph = []

for i in range(n):
    line = [1] * n
    line[i] = 0
    graph.append(line)


handshakes = 0

for i in range(len(graph)):
    j = i
    while j < len(graph):
        if graph[i][j] == 1:
            handshakes += 1
        j += 1

print(f"Среди {n}-и друзей было {handshakes} рукопожатий")