def solution(num_list):
    answer = 0
    sums = sum(num_list)**2
    mul = 1
    for i in num_list :
        mul *= i
    if mul < sums :
        answer = 1
    else :
        answer = 0
    return answer