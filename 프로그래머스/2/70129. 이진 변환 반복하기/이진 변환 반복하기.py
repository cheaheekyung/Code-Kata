def solution(s):
    answer = []
    count = 0
    count1 = 0
    while len(s) != 1:

        count += s.count('0')
        s = s.replace('0','')
        s = bin(len(s))[2:]
        count1 += 1
    answer = [count1, count]
    return answer