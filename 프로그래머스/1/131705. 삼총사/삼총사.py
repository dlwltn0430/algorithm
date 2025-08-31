def solution(number):
    sum = 0
    #i = 2
    #-2, 0
    #2,-5
    cnt = 0
    for i in range(len(number) - 2): 
        for j in range(i + 1, len(number) - 1): 
            for k in range(j + 1, len(number)):
                sum += number[i] + number[j] + number[k]
                if (sum == 0):
                    cnt += 1
                sum = 0
    return cnt