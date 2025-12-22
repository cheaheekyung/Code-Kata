l = list(map(int,input().split()))

a = sorted(l)
b = sorted(l, reverse = True)

if l == a :
    print('ascending')
elif l == b :
    print('descending')
else :
    print('mixed')