def solution(prices):
    answer = 0
    answer_list = []
    
    for i in range(len(prices)):
        answer = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                answer+=1
            else:
                answer+=1
                break
        answer_list.append(answer)
    return answer_list