
n = int(input())
s = list(map(int, input().split()))

s.sort()
for i in range(len(s)) :
    s[i] = s[i]/s[-1]*100
print(sum(s)/len(s))