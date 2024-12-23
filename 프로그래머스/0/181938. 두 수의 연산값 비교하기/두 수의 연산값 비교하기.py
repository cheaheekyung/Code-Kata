def solution(a, b):
    ab = str(a)+str(b)
    cd = 2 * a * b
    answer = max(int(ab),cd)
    return answer