def solution(arr, k):
    answer = [i+k if k % 2 == 0 else i*k for i in arr ]
    # if k % 2 :
    #     for i in arr :
    #         answer.append(i*k)
    # else :
    #     for i in arr :
    #         answer.append(i+k)
    return answer