from collections import deque

def solution(n, computers):
    visited = [False] * n
    count = 0
    
    for i in range(n):
        if not visited[i]: 
            queue = deque([i])
            # print(queue)
            visited[i] = True
        
            while queue:
                now = queue.popleft()
                for j in range(n):
                    if computers[now][j] == 1 and visited[j]==False:
                        # print(i, j)
                        queue.append(j)
                        visited[j] = True
            count+=1    
    return count