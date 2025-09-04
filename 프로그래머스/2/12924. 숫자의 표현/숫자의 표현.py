def solution(n):
    start = 1
    end = n
    sum = 0
    cnt = 0
    
    while (start <= n):
        for i in range(start, n+1):
            sum += i
            if (sum == n):
                cnt += 1
            elif (sum > n):
                break
        start += 1
        sum = 0
        
    return cnt