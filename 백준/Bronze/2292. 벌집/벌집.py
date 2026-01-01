n = int(input())

a = 1
b = 0
for i in range(n):
    if a < n:
        a += 6 * i
        b += 1
    else:
        break
if n == 1:
    b = 1
print(b)