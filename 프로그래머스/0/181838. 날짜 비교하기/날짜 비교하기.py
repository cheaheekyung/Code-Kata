def solution(date1, date2):
    answer = 0
    day1 =''.join(map(str, date1))
    day2 =''.join(map(str, date2))
    if int(day1) < int(day2) :
        answer = 1
    return answer