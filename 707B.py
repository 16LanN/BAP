def min_delivery_cost(n, k, roads, storages):
    if k == 0 or k == n:
        return -1

    storage_set = set(storages)
    min_cost = 10**100

    for u, v, l in roads:
        if u in storage_set and v not in storage_set:
            min_cost = min(min_cost, l)
        elif v in storage_set and u not in storage_set:
            min_cost = min(min_cost, l)

    return min_cost if min_cost != 10**100 else -1

n, m, k = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
storages = list(map(int, input().split())) if k > 0 else []

print(min_delivery_cost(n, k, roads, storages))
