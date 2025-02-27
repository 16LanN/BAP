def maximum(n, s):
    s = list(s)
    count = 0
    
    while True:
        flag = False
        i = 0
        
        while i < len(s):
            if (i > 0 and ord(s[i]) == ord(s[i - 1]) + 1) or (i < len(s) - 1 and ord(s[i]) == ord(s[i + 1]) + 1):
                del s[i]
                count += 1
                flag = True
            else:
                i += 1 
        
        if not flag:
            break 
    
    return count

n = int(input())
s = input()
print(maximum(n, s))
