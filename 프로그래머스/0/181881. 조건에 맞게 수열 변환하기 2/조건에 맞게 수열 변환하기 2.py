def solution(arr):
    x = 0
    while True:
        new_arr = []
        for a in arr:
            if a >= 50 and a % 2 == 0:
                new_arr.append(a // 2)
            elif a < 50 and a % 2 == 1:
                new_arr.append(a * 2 + 1)
            else:
                new_arr.append(a)
        
        if new_arr == arr:
            return x
        arr = new_arr
        x += 1