def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)) :
        a = []
        for s in range(len(arr1[i])) :
            a.append(arr1[i][s]+arr2[i][s])
        answer.append(a)
            
        
    return answer