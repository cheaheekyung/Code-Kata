def solution(n, m):
    answer = []
    a = []
    b = []
    for i in range(1,n+1) :
        if n % i == 0 and m % i == 0 :
            a.append(i)
    for i in range(1,m+1) :
        if n * i % m ==0 :
            b.append(n*i)

    answer = [max(a), min(b)]
    return answer