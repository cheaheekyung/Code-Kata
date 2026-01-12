a, b, v = map(int, input().split())

d = (v - a + (a - b) - 1) // (a - b) + 1

print(d)