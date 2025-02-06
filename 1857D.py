def edge():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        c = []
        for u in range(n):
            ci = a[u] - b[u]
            c.append(ci)

        max_strength = max(c)
        strongest = [i + 1 for i in range(n) if c[i] == max_strength]

        print(len(strongest))
        print(*strongest)

edge()