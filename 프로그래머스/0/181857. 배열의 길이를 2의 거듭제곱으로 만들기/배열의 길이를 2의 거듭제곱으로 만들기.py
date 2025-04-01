def solution(arr):
    n = len(arr)
    a = 1
    while a < n:
        a *= 2
    return arr + [0] * (a - n)