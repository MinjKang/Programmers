def solution(myString, pat):
    answer = 0
    for m in range(0, len(myString)):
        if len(list(myString)[m:m+len(pat)]) == len(pat):
            if (''.join(list(myString)[m:m+len(pat)])) == pat:
                answer += 1
    return answer