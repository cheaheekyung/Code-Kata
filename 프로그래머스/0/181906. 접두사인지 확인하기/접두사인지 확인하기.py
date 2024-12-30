def solution(my_string, is_prefix):
    answer = 0
    prefix = ''
    for i in my_string :
        prefix += i
        if is_prefix == prefix :
            answer = 1
    return answer