def dijkstra(n, graph, start):
    INF = 10**100
    dist = [INF] * n
    dist[start] = 0
    visited = [False] * n
    prev = [-1] * n
    for _ in range(n):

        min_dist = INF
        min_index = -1
        for v in range(n):
            if not visited[v] and dist[v] < min_dist:
                min_dist = dist[v]
                min_index = v
        
        if min_index == -1:
            break
        

        visited[min_index] = True
        

        for neighbor, weight in graph[min_index]:
            if dist[min_index] + weight < dist[neighbor]:
                dist[neighbor] = dist[min_index] + weight
                prev[neighbor] = min_index

    return dist, prev

n = 9
graph = [
    [(1, 8), (3, 2)], 
    [(2, 1)],          
    [(3, 5), (5, 1)],  
    [(4, 4)],          
    [(5, 5), (7, 7)], 
    [(6, 1)],          
    [(7, 2)],          
    [(8, 8)],          
    []                
]

start = 0
dist, prev = dijkstra(n, graph, start)

print("Кратчайшие расстояния:", dist)
print(prev)

end = 8
path = []
while end != -1:
    path.append(end)
    end = prev[end]
path.reverse()
print(f"Кратчайший путь до {n-1}:", path)
