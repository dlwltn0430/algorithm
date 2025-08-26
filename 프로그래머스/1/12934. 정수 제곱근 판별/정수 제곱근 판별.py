def solution(n):
    n = n ** (1/2)
    
    if (n.is_integer()):
        return (n + 1) ** 2
    else:
        return -1