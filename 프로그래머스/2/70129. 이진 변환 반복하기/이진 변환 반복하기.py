     
def solution(s):
    answer = []
    repeat_num = 0
    delete_num = 0
    
    while s != '1': 
        repeat_num += 1
        delete_num += s.count('0') # 0의 갯수 세기
        
        s = s.replace('0', '')
        
        s = format(len(s), 'b')
        
    answer = [repeat_num, delete_num]
            
    return answer


