from itertools import combinations

def is_prime(num):
    if num < 2:
        return False
    for a in range(2, int(num**0.5+1)):
        if num % a == 0:
            return False
    return True 

def solution(nums):
    answer = 0
    for i in combinations(nums, 3):
        num_sum= 0
        for j in i:
            num_sum+=j
        if (is_prime(num_sum)) == True:
            answer+=1
    return answer