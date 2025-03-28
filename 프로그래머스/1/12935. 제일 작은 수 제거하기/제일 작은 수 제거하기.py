def solution(arr):
    answer = []
    m = min(arr)
    if arr == [10] :
        answer.append(-1)
    else :
        for i in arr :
            if i != m :
                answer.append(i)
    return answer