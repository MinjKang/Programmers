def solution(number):
    count = 0
    for i in range(0, len(number)):
        for j in range(i+1, len(number)):
            for k in range(j+1, len(number)):
                ans = number[i] + number[j] + number[k]
                if ans == 0:
                    count += 1
    return count
                
            
            