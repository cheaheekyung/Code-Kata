def solution(number):
    answer = 0
    for i in range(len(number) - 2):
        for j in range(i+1, len(number)-1):
            if -(number[i]+number[j]) in number[j+1:] :
                answer += number[j+1:].count(-(number[i]+number[j]))
            
    return answer