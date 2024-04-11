def solution(array, commands):
    answer = []
    split_array = []
    third_num = 0
    
    for params in commands:
        i = params[0]
        j = params[1]
        k = params[2]
        
        split_array = array[i-1:j]
        split_array.sort()
        third_num = split_array[k-1]
        
        answer.append(third_num)
        
    return answer
        
        
    
    
    