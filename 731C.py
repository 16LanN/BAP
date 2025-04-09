import sys
sys.setrecursionlimit(1 << 25)

n, m, k = map(int, input().split())
colors = list(map(int, input().split()))
adj = [[] for _ in range(n)]

for _ in range(m):
    l, r = map(int, input().split())
    adj[l - 1].append(r - 1)
    adj[r - 1].append(l - 1)

visited = [False] * n
res = 0

def dfs(u, component):
    visited[u] = True
    component.append(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v, component)

for i in range(n):
    if not visited[i]:
        component = []
        dfs(i, component)
        freq = {}
        for sock in component:
            c = colors[sock]
            freq[c] = freq.get(c, 0) + 1
        max_freq = max(freq.values())
        res += len(component) - max_freq

print(res)
