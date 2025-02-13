def max_weight_path(n, roads, s, t):
    adj_list = [[] for _ in range(n + 1)]
    for a, b, w in roads:
        adj_list[a].append((b, w))
        adj_list[b].append((a, w))

    def transport(min_weight):
        queue = [s]
        visited = [False] * (n + 1)
        parent = [-1] * (n + 1)
        visited[s] = True

        for i in queue:
            for neighbor, weight in adj_list[i]:
                if not visited[neighbor] and weight >= min_weight:
                    visited[neighbor] = True
                    parent[neighbor] = i
                    queue.append(neighbor)
                    if neighbor == t:
                        return parent
        return None

    left, right, max_weight = 1, 10**10, 0
    best_path = []

    while left <= right:
        mid = (left + right) // 2
        parent = transport(mid)
        if parent:
            max_weight = mid
            left = mid + 1
            best_path = []
            current = t
            while current != -1:
                best_path.append(current)
                current = parent[current]
            best_path.reverse()
        else:
            right = mid - 1

    return max_weight, best_path

n = int(input())
m = int(input())
roads = []
for i in range(m):
    road = list(map(int, input().split()))
    roads.append(road)
s, t = map(int, input().split())
print(roads)

max_weight, best_path = max_weight_path(n, roads, s, t)
print(f"Максимальный вес груза, который можно перевезти: {max_weight}")
print(f"Маршрут: {' -> '.join(map(str, best_path))}")
