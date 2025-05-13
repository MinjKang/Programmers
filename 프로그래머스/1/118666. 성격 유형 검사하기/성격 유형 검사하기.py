def solution(survey, choices):
    scores = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    for i in range(len(survey)):
        choice = choices[i]
        if choice > 4:
            scores[survey[i][1]] += choices[i]-4
        elif choice < 4:
            scores[survey[i][0]] += 4-choices[i]
    
    pscore = list(scores.values())
    ptype = list(scores.keys())
    answer = []
    print(pscore, ptype)
    
    for i in range(0, len(scores), 2):
        if pscore[i] > pscore[i+1]:
            answer.append(ptype[i])
        elif pscore[i] < pscore[i+1]:
            answer.append(ptype[i+1])
        elif pscore[i] == pscore[i+1]:
            if ord(ptype[i]) < ord(ptype[i+1]):
                answer.append(ptype[i])
            else:
                answer.append(ptype[i+1])
    return ''.join(answer)
            
        

            