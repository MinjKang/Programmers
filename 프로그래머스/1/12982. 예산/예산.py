def solution(d, budget):
    d.sort()
    sum_answer = 0
    answer = 0
    for i in d:
        sum_answer+=i
        if sum_answer >  budget:
            break
        answer += 1

    return answer