def solution(my_string, m, c):
    answer = ''
    for i in range(len(my_string)//m) : 
        answer += my_string[c+(i*m)-1]
    return answer