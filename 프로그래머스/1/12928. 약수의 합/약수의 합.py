def solution(n):
    d = []
    
    for i in range(n, 0, -1):
        if (n % i == 0):
            d.append(i)
    
    return sum(d)