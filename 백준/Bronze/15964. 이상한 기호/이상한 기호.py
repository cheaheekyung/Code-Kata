#연산자의 기호는 ＠으로, A＠B = (A+B)×(A-B)으로 정의내리기로 했다.

def cal(a, b) :
    print((a+b)*(a-b))

a, b = map(int, input().split())
cal(a,b)