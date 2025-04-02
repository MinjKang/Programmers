def solution(strings, n):
    answer = []
    index = sorted(list(map(lambda string: (string[n], string), strings)))
    
    for i in index:
        answer.append(i[1])
    return answer
    


        
