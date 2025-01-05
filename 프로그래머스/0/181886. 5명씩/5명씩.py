def solution(names):
    answer = [names[i] for i in range(0,len(names)) if i % 5 == 0]
    # for i in range(0,len(names)) :
    #     if i % 5 == 0 :
    #         answer.append(names[i])
    return answer