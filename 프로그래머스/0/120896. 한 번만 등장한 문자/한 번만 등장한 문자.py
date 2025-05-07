from collections import Counter

def solution(s):
    answer = []
    str_num = Counter(s)
    for k, v in str_num.items():
        if v == 1:
            answer.append(k)
    return (''.join(sorted(answer)))
            