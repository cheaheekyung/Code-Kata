def solution(s):
    count = 0
    for char in s:
        if char == '(':
            count += 1
        else:  # char == ')'
            count -= 1
            if count < 0:
                return False  # ')'가 '('보다 먼저 나옴 -> 올바르지 않음
    return count == 0  # 모두 짝이 맞으면 0이어야 함