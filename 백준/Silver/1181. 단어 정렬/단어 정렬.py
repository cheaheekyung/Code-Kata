n = int(input())
a = []
for _ in range(n) :
    a.append(input())
a = set(a)
b = sorted(a, key=lambda x : (len(x), x))
print(*b, sep='\n')