def solution(clothes):
    counter = {}
    
    for a, b in clothes:
        if b in counter:
            counter[b] += 1
        else:
            counter[b] = 1

    total = 1

    for key in counter:
        count = counter[key]
        if count > 1:
            total *= (count + 1)
        else:
            total *= 2  

    return total - 1  
