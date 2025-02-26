def solution(arr):
    stk = []
    for i in range(len(arr)):
        a = arr[i]
        if not stk :
            stk.append(a)
            
        elif stk[-1] < a :
            stk.append(a)
            
        else :
            while stk and stk[-1] >= a:
                stk.pop()
            stk.append(a)
        
    return stk