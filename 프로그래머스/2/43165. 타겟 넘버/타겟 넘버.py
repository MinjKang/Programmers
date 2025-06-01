from collections import deque

def solution(numbers, target):
    queue = deque()
    queue.append((0, 0))
    count = 0
    # print(queue)
    
    while queue:
        queue_sum, index = queue.popleft()
        
        if index == len(numbers):
            if queue_sum == target:
                count += 1
    
        else:
            queue.append((queue_sum + numbers[index], index+1))
            queue.append((queue_sum - numbers[index], index+1))

    # print(count)
    return count
