def solution(my_string, s, e):
    one = my_string[:s]  
    re = my_string[e:s-1:-1]  if s > 0 else my_string[e::-1]
    two = my_string[e+1:]
    answer = one+re+two
    return answer