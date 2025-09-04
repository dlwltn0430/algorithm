def get_count(n):
    binary = []
    
    while(n > 0):
        binary.append(n % 2)
        n = n // 2
        
    # binary.reverse()

    return binary.count(1)
    
def solution(n):
    num = n + 1
    
    while(True):
        if get_count(n) == get_count(num):
            return num
        num += 1