def solution(a, b, c):
    answer = ""
    if a != b and b != c and a != c :
        answer = a + b + c
    elif a == b == c :
        answer = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    else:
        if a == b :
            if a != c:
                answer = (a + b + c) * (a**2 + b**2 + c**2 )
        elif a == c :
            if a != b :
                answer = (a + b + c) * (a**2 + b**2 + c**2 )
        elif b == c :
            if b != a :
                answer = (a + b + c) * (a**2 + b**2 + c**2 )
    return answer