def solution(k, score):
    answer = []
    min_answer_list = []
    
    for s in score:
        answer.append(s)
        min_answer = min(answer)
        
        if len(answer)>k:
            answer = sorted(answer)
            answer = (answer[-k:])
            min_answer = min(answer)
        
        min_answer_list.append(min_answer)
        
    return min_answer_list