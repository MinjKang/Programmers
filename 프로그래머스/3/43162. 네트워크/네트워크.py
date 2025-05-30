def solution(n, computers):
    visited = [False] * n  
    count = 0  

    for i in range(n):
        if not visited[i]:  
            stack = [i] 

            while stack:
                now = stack.pop()
                visited[now] = True 

                for j in range(n):
                    if computers[now][j] == 1 and not visited[j]:
                        stack.append(j)

            count += 1  
    return count