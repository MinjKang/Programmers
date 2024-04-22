def solution(n):
    arr_n = list(str(n))
    arr_n.sort(reverse=True)
    
    arr_n = ''.join(arr_n)
    
    return int(arr_n)