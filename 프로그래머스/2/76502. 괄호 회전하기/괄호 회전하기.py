def solution(s):
    answer = 0
    
    for i in range(len(s)):
        s = s[1:] + s[0]  

        if s[0] in [')', ']', '}']:
            continue  

        slist = []  
        valid = True

        for a in s:
            if a in ['[', '(', '{']:
                slist.append(a)
            elif a in [')', ']', '}']:
                if not slist:
                    valid = False
                    break
                top = slist[-1]
                if (a == ')' and top != '(') or \
                   (a == ']' and top != '[') or \
                   (a == '}' and top != '{'):
                    valid = False
                    break
                slist.pop()
            else:
                valid = False
                break
        
        if valid and not slist:
            answer += 1

    return answer
