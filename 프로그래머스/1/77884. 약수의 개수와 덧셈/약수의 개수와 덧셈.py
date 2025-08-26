def solution(left, right):
    n = []
    cnt = 0
    answer = 0
    
    for i in range(left, right + 1):
        for j in range(1, i + 1):
            if (i % j == 0):
                cnt += 1
        n.append(cnt)
        cnt = 0
    
    for i in range(len(n)):
        if (n[i] % 2 == 0):
            answer += left + i
        else:
            answer -= left + i
            
    return answer