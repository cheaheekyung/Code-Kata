def gcd(a,b) :
    while b:
        a, b = b ,a % b
    return a

def lcm(a, b) :
    l = a*b // gcd(a,b)
    return l

a, b = map(int, input().split())
print(gcd(a, b), lcm(a, b))
