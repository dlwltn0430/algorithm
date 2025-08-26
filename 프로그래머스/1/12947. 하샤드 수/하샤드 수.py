def solution(x):
    sum = 0
    y = x
    
    for i in range(len(str(x))):
        sum += y % 10
        y = y // 10

    if (x % sum == 0):
        return True
    else:
        return False