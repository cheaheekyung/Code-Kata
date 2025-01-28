def solution(s):
    answer = True
    s1 = s.lower()
    countp = 0
    county = 0 
    for i in s1 :
        if i == 'p' :
            countp += 1
        elif i == 'y' :
            county += 1
    if countp != county :
        answer = False
    
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')

    return answer