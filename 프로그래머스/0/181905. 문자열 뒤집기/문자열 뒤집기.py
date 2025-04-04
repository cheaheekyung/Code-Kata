def solution(my_string, s, e):
    one = my_string[:s]  
    re = my_string[s:e+1][::-1]
    two = my_string[e+1:]
    answer = one+re+two
    return answer

