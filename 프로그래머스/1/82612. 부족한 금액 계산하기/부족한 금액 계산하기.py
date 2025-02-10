def solution(price, money, count):
    answer = -1
    sumprice = 0
    for i in range(1,count+1) :
        sumprice += price * i
    if sumprice >= money :
        answer = sumprice - money
    else :
        answer= 0
    return answer