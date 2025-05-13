def solution(s):
    open_count=0
    closed_count=0
    
    if s[0] == ")":
        return False
    
    for i in range(len(s)):
        if s[i] == "(":
            open_count+=1
        elif s[i] == ")":
            if open_count==closed_count:
                return False
            closed_count +=1
        else:
            return False
        
    return open_count == closed_count