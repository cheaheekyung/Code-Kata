def solution(s):
    answer = True
    o = s.count("(") 
    c = s.count(")")
    if s[0] == ")" or s[-1] == "(" or o != c :
        answer = False

    return answer