def solution(s):
    answer = 0
    list_s = s.split()
    for i in range(len(list_s)-1) :
        if list_s[i] != 'Z' and list_s[i+1] != 'Z':
            answer += int(list_s[i])
    if list_s[-1] != 'Z' :
        answer += int(list_s[-1])
    return answer