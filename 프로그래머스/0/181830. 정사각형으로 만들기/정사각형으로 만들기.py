def solution(arr):
    answer = []
    row = len(arr[0])
    col = len(arr)
    if row > col :
        answer += (arr + [[0]*row]*(row-col))
    elif col > row :
        for i in arr :
            answer += [i+[0]*(col-row)]
    else :
        answer = arr
    return answer