import math

def solution(numer1, denom1, numer2, denom2):
    up = numer1*denom2 + numer2*denom1
    down = denom1*denom2
    gcd = math.gcd(numer1*denom2 + numer2*denom1, denom1*denom2)
    ups = up//gcd
    downs = down//gcd
    return ups, downs