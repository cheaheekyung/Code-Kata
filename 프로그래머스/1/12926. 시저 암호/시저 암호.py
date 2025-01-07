def solution(s, n) :
    answer = ''
    ALP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alp = ALP.lower()

    for i in s :
        if i in ALP : 
            answer += ALP[(ALP.index(i) + n) % len(ALP)]
        elif i in alp :
            answer += alp[(alp.index(i) + n) % len(alp)]
        else :
            answer += i
    return answer
