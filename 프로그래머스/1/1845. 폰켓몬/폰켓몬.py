def solution(nums):
    answer = len(nums)/2
    if len(set(nums))<answer:
        answer = len(set(nums))
    return answer
    
#     answer = 0
#     answer = len(set(nums))
    
#     if answer > len(nums)/2:
#         answer = len(nums)/2

#     return(int(answer))
    
