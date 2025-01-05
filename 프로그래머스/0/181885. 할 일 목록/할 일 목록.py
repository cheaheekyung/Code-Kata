def solution(todo_list, finished):
    answer = []
    for i , x in zip(todo_list, finished) :
        if not x :
            answer.append(i)
    return answer