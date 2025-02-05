def solution(s):
    
    for index, strnum in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]) :
        s = s.replace(strnum, str(index))
    answer = int(s)
    return answer