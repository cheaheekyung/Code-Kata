def solution(arr):
    answer = []
    
    for i in range(len(arr)) :
        if i < len(arr) :
            if answer == [] :
                answer.append(arr[i])
            else :
                if answer[-1] == arr[i] :
                    answer.pop()
                else :
                    answer.append(arr[i])
    
    if answer == [] :
        answer = [-1]
    return answer