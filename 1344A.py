def rearrange(n, a):
    booked = set()

    for i in range(n):
        room = (i + a[i] % n) % n
        booked.add(room)

    return "YES" if len(booked) == n else "NO"

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(rearrange(n, a))