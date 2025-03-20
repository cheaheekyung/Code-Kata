def solution(id_pw, db):
    answer = 'fail'
    for idd, pw in db :
        if id_pw[0] == idd :
            if id_pw[1] !=pw : 
                answer = 'wrong pw'
            else :
                answer = 'login'

    return answer