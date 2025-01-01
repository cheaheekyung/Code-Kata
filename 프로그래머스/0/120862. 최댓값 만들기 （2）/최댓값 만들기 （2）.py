def solution(numbers):
    answer = 0
    numbers.sort()
    if numbers[1] < 0 :
        if numbers[0]*numbers[1] > numbers[-1]*numbers[-2] :
            answer = numbers[0]*numbers[1]
        else :
            answer = numbers[-1]*numbers[-2]
    else : 
        answer = numbers[-1]*numbers[-2]
        
    return answer