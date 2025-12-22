s = input()

d = {chr(i) : -1 for i in range(ord('a'), ord('z')+1)}

for i in s :
    d[i] = s.index(i)

print(*d.values())