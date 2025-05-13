def solution(progresses, speeds):
    rest_list = []
    answer_list = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i] != 0:
            rest = ((100-progresses[i])//speeds[i])+1
            rest_list.append(rest)
        else:
            rest = (100-progresses[i])//speeds[i]
            rest_list.append(rest)
    
    i=0
    while i < len(rest_list):
        answer = 0
        for j in range(i, len(rest_list)):
            if rest_list[i] >= rest_list[j]:
                answer+=1
            else:
                break
        answer_list.append(answer)
        i+=answer
    
    return answer_list

