def solution(array):
    answer = []
    max_num = max(array)
    index_num = -1
    for i in array :
        if i :
            index_num += 1
            if i == max_num :
                break
                
    answer.append(max_num)
    answer.append(index_num)
    return answer