def solution(food):
    left = ''
    answer = ''
    
    for i in range(1, len(food)):
        div = food[i] // 2
        for j in range(div):
            left += str(i)
    
    answer += left + "0"
    
    left = list(left)
    left.reverse()
    right = "".join(left)
    answer += right
    
    return answer