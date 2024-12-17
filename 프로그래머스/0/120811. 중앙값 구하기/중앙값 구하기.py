def solution(array):
    answer = 0
    array1 = sorted(array)
    answer = array1[len(array1)-(len(array1)//2)-1]
    return answer