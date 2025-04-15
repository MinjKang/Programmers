def solution(lottos, win_nums):
    answer = []
    count_zero = 0
    count_win = 0
    
    for i in range(len(lottos)):
        if lottos[i] == 0:
            count_zero += 1
        for j in range(len(win_nums)):
            if lottos[i] == win_nums[j]:
                count_win += 1
    # print('지워진 수', count_zero, '당첨 수', count_win)
    
    max_count = count_zero+count_win
    min_count = count_win
    
    award = [6, 6, 5, 4, 3, 2, 1]
    
    return ([award[max_count], award[min_count]])
    
    
    