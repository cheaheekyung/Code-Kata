def solution(keyinput, board):
    answer = [0, 0]
    x_limit, y_limit = board[0] // 2, board[1] // 2  # 이동 가능한 최대 좌표

    for key in keyinput:
        if key == "up" and answer[1] < y_limit:
            answer[1] += 1
        elif key == "down" and answer[1] > -y_limit:
            answer[1] -= 1
        elif key == "left" and answer[0] > -x_limit:
            answer[0] -= 1
        elif key == "right" and answer[0] < x_limit:
            answer[0] += 1

    return answer