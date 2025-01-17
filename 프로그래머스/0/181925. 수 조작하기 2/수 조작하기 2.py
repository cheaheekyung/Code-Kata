def solution(numlog):
    answer = ''
    for i in range(len(numlog)-1):
        if numlog[i+1]-numlog[i] == 1 :
            answer += 'w'
        elif numlog[i+1]-numlog[i] == -1 :
            answer += 's'
        elif numlog[i+1]-numlog[i] == 10 :
            answer += 'd'
        elif numlog[i+1]-numlog[i] == -10 :
            answer += 'a'
        
    return answer