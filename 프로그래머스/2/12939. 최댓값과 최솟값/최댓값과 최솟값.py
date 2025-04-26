def solution(s):
    answer = ''
    a = s.split(" ")
    b = []
    for i in a : 
        b.append(int(i))
    answer += str(min(b))
    answer += " "
    answer += str(max(b))
    return answer