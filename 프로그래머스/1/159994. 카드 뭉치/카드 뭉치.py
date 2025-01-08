def solution(cards1, cards2, goal):
    cards1index, cards2index = 0, 0  
    for i in goal:
        
        if cards1index < len(cards1) and i == cards1[cards1index]:
            cards1index += 1
       
        elif cards2index < len(cards2) and i == cards2[cards2index]:
            cards2index += 1
        
        else:
            return "No"
    return "Yes" 