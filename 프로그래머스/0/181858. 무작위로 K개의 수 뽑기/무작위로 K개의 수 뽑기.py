def solution(arr, k):
    answer = []
    for i in arr :
        if i not in answer :
            if len(answer) != k :
                answer.append(i)
    
    if len(answer) < k :
        answer += [-1]*(k-len(answer))

    return answer