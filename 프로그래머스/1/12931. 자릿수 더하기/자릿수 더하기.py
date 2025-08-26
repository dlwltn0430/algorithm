def solution(n):
    sum = 0
    
    for i in range(len(str(n))):
        sum += n % 10
        n = n // 10
        
    return sum