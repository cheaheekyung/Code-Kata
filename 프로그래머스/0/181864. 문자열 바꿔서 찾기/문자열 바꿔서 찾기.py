def solution(myString, pat):
    answer = 0
    a = myString.replace("A","b")
    b = a.replace("B","A")
    c = b.upper()
    answer = 1 if pat in c else 0
    return answer