def solution(n):
    answer = []
    n1 = str(n)[::-1]
    for i in n1 :
        answer.append(int(i))
    return answer