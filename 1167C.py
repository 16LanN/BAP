import sys

def find(a):
    if a == p[a]:
        return a
    p[a] = find(p[a])
    return p[a]

def unite(a, b):
    a, b = find(a), find(b)
    if a == b:
        return
    if rk[a] < rk[b]:
        a, b = b, a
    p[b] = a
    rk[a] += rk[b]

n, m = map(int, sys.stdin.readline().split())
p = list(range(n))
rk = [1] * n

for _ in range(m):
    data = list(map(int, sys.stdin.readline().split()))[1:]
    lst = -1
    for x in data:
        x -= 1
        if lst != -1:
            unite(x, lst)
        lst = x

print(" ".join(str(rk[find(i)]) for i in range(n)))