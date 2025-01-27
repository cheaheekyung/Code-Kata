def solution(nums):
    answer = 0
    a = len(nums) // 2
    c = len(set(nums))
  
    answer = min(a,c)
    
    return answer