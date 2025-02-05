def princessesprefers():
    tests = int(input())

    for _ in range(tests):
        n = int(input())
        princesses = []
        married = [False] * n
        kingdom = set(range(1, n + 1))

        for i in range(n):
            data = list(map(int, input().split()))
            k = data[0]
            pref = data[1:]
            princesses.append(pref)

        for i in range(n):
            for prince in princesses[i]:
                if prince in kingdom:
                    married[i] = True
                    kingdom.remove(prince)
                    break

        if kingdom:
            for i in range(n):
                if not married[i]:
                    print(f"""IMPROVE
{i + 1} {min(kingdom)}""")
                    break
        else:
            print("OPTIMAL")

princessesprefers()
