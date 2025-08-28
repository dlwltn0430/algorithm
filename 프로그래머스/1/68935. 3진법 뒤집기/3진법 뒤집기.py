def solution(n):
    t = []
    sum = 0
    
    while(True):
        t.append(n % 3)
        n = n // 3
        if (n == 0):
            break
    
    t.reverse()
    
    for i in range(len(t)):
        sum += t[i] * (3**(i))
        
    return sum
