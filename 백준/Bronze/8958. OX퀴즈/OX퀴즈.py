n = int(input())

for _ in range(n) :
    s = input()
    a = []
    for i in range(len(s)) :
        if i == 0 :
            if s[0] == 'O' :
                a.append(1)
            else :
                a.append(0)
        elif s[i] == 'O' :
            a.append(a[i-1]+1)
        elif s[i] == 'X' :
            a.append(0)
    print(sum(a))