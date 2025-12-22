n = int(input())

for _ in range(n) :
    h, w, r = map(int, input().split())
    print(f"{(r-1) % h +1}{((r-1) // h)+1:02d}") 