def solution(myString):
    answer = ''
    a = ['a','b','c','d','e','f','g','h','i','j','k']
    for i in myString :
        if i in a :
            answer += 'l'
        else :
            answer += i
    return answer