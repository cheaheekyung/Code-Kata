def solution(hp):
    answer = 0
    jang = hp // 5
    byung = hp % 5 // 3
    il = hp % 5 % 3 // 1
    answer = jang + byung + il
    return answer