def solution(money):

    count = int(money/5500)
    charge = money - (5500*count)
    print(count, charge)
    
    answer = [count, charge]
    return answer
