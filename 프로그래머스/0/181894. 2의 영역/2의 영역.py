def solution(arr):
    answer = []
    a = []
    for i in range(len(arr)) :
        if arr[i] == 2 :
            a.append(i)
    if a :
        answer = arr[a[0]:a[-1]+1]
    else :
        answer = [-1]
    
    return answer