a = int(input())
for i in range(a):
    flag = False
    b = int(input())
    while True:
        if b%11 == 0:
            flag = True
            break
        b -= 111
        if b < 0:
            break
    if flag:
        print("YES")
    else:
        print("NO")

