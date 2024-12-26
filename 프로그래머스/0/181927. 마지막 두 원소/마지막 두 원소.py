def solution(num_list):
    answer = num_list
    last = num_list[-1]
    last2 = num_list[-2]
    
    if last > last2 :
        answer.append(last-last2)
    else :
        answer.append(last*2)
    return answer