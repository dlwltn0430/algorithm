def solution(a, b, n):
    rest = 0
    answer = 0
    
    while(True):
        exchanged = n // a * b
        answer += exchanged
        n = exchanged + n % a
        if (n < a):
            break
            
    return answer