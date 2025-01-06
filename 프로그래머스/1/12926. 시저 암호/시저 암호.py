def solution(s, n) :
    answer = ''
    ALP =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    for i in s :
        if i in ALP : 
            answer += ALP[(ALP.index(i) + n) % len(ALP)]
        elif i in alp :
            answer += alp[(alp.index(i) + n) % len(alp)]
        elif i == ' ' :
            answer += ' '
    return answer

print(solution('a B z',4))