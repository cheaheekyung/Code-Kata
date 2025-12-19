x = list(range(1,31))

for _ in range(28) :
    i = int(input())
    x.remove(i)

print(*x, sep="\n")