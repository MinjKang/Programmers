def solution(bridge_length, weight, truck_weights):
    answer = 0
    stack = [0]*bridge_length
    
    while truck_weights:
        stack.pop(0)
        answer +=1
        
        if sum(stack) + truck_weights[0] <= weight:
            stack.append(truck_weights.pop(0))
        else:
            stack.append(0)
                           
    answer+=bridge_length
    return answer