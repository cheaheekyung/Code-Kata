n = 1
for _ in range(3) :
    n *= int(input())
s = str(n)
d = { i : 0 for i in range(0, 10)}

for i in s :
    d[int(i)] += 1

print(*d.values(), sep="\n")
        