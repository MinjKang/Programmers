def solution(numbers):
    a = sorted(numbers)[-1]
    b = sorted(numbers)[-2]
    c = sorted(numbers)[0]
    d = sorted(numbers)[1]
        
    pos_num = a*b
    neg_num = c*d
    
    return max(pos_num, neg_num)
    