def solution(n):
    cnt = 0
    answer = 0
    
    for i in range(1, n+1):
        answer = 0
        if i == n:
            cnt += 1
            break
        for j in range(i, n+1):
            answer += j
            if answer > n:
                break
            if answer == n:
                cnt+=1
                break   
    return cnt