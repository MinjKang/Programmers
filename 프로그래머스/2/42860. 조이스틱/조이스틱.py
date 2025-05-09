def solution(name):
    answer = 0
    a_pos = ord('A') # 'A' : 65, 'Z' : 90
    z_pos = ord('Z') 
    
    for n in name:
        up = ord(n) - a_pos 
        down = z_pos - ord(n) + 1
        print(n, up, down)
        up_down_count = min(up, down)
        answer += up_down_count
        
    next_num = len(name) - 1    
    for i in range(len(name)):
        j = i + 1
        
        while j < len(name) and name[j] == 'A':
            j += 1
        # print(j, next_num_a, "개 연속 0임")
        
        next_num_a = 2 * i + (len(name) - j)   
        next_num_b = i + 2 * (len(name) - j)
        next_num = min(next_num, next_num_a, next_num_b)
    
    answer += next_num
    
    return answer