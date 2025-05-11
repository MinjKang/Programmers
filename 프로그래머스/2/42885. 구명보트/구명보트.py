def solution(people, limit):
    people.sort()
    i = 0
    j = len(people) - 1
    answer = 0
    
    while i<=j:
        if people[i]+people[j]<=limit:
            i=i+1
            j=j-1
            answer +=1 
        else:
            j = j-1
            answer += 1
    return answer