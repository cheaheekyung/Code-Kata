def solution(lottos, win_nums):
    answer = []
    min_win = 0
    count_z = 0
    
    for i in lottos :
        if i in win_nums :
            min_win += 1
        elif i == 0 :
            count_z += 1
    
    max_win = min_win + count_z
    lotto_dic = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    answer = [lotto_dic.get(max_win),lotto_dic.get(min_win)]
    return answer