def solution(arr, flag):
    answer = []
    for i in range(len(flag)) :
        if flag[i] :
            n = 0
            while n != arr[i]*2 :
                answer.append(arr[i])
                n += 1
        else :
            n = 0
            while n != arr[i] :
                answer.pop()
                n += 1
    return answer