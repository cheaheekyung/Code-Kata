def solution(phone_number):
    answer = ''
    a = len(phone_number)-4
    
    for i in range(a) :
        answer += '*'
    return answer+phone_number[-4::]