n, m = map(int, input().split())
l = list(map(int, input().split()))

from itertools import combinations
a = []
for i in list(combinations(l, 3)) :
    if sum(i) <= m :
        a.append(sum(i))
a.sort()
print(a[-1])
    