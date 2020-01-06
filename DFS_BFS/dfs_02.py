def solution(n, computers):
    answer = 0
    seg = [0] * n
    
    while computers:
        queue = []
        
        for i in range(n):
            if seg[i] == 0:
                queue.append(i)
                break
                
        if len(queue) == 0:
            break
        
        answer += 1
        while queue:
            next_comp = queue.pop(0)
            neighbor = computers[next_comp]
            
            for i, val in  enumerate(neighbor):
                if val == 1 and seg[i] == 0:
                    seg[i] = answer
                    queue.append(i)
                    
    return answer
