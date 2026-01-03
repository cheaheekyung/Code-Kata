def solution(polynomial):
    answer = ''
    a = polynomial.split()
    x = 0
    n = 0
    for i in range(len(a)) :
        if a[i].isdigit() :
            n += int(a[i])
        else :
            if a[i] == 'x' :
                x += 1
            elif a[i] == '+' :
                pass
            else :
                x += int(a[i][:-1])
                
    if x > 0 and n > 0 :
        if x > 1 :
            answer = f'{x}x + {n}'
        else :
            answer = f'x + {n}'
    elif x > 0 and n == 0 :
        if x > 1 :
            answer = f'{x}x'
        else :
            answer = f'x'
    elif x == 0 and n > 0 :
        answer = f'{n}'
    return answer