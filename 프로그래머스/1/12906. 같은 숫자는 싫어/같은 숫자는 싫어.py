def solution(arr):
    answer_list = []
    answer_list.append(arr[0])
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer_list.append(arr[i])

    return answer_list
