def solution(my_string):
    answer = []
    hard = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in hard :
        counts = my_string.count(i)
        answer.append(counts)
    
    return answer