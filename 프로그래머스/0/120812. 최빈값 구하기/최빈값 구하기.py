def solution(array):
    answer = 0
    max_count = 0 
    
    for i in set(array):  
        count_i = array.count(i)  
        if count_i > max_count: 
            max_count = count_i
            answer = i
        elif count_i == max_count:  
            answer = -1
    
    return answer