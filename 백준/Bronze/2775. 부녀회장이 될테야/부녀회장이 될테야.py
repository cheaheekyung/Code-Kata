a = list(map(int,open(0).read().split()))

def main(n,m) :
    l = [j for j in range(1,m+1)]
    for _ in range(0, n) :
        s = 0
        for i, j in enumerate(l) :
            s += j
            l[i] = s
    return l[-1]

for i in range(1, len(a), 2) : 
    b = a[i:i+2]
    n, m = b[0], b[1] 
    print(main(n,m))
    