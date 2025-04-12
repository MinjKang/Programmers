def solution(answers):
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    a_count = 0
    b_count = 0
    c_count = 0
    
    for i in range(0, len(answers)):
        if a[i%len(a)] == answers[i]:
            a_count += 1
        if b[i%len(b)] == answers[i]:
            b_count += 1
        if c[i%len(c)] == answers[i]:
            c_count += 1
    
    man = [a_count, b_count, c_count]
    answer = []
    for i in range(0, len(man)):
        if man[i] == max(man):
            answer.append(i+1)
            
    return answer