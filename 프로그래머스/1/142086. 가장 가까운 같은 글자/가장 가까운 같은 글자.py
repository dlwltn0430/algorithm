def solution(s):
    answer = []
    l = []
    
    for i in range(len(s)):
        if s[i] not in l:
            l.append(s[i])
            answer.append(-1)
        else:
            answer.append(i - s.rfind(s[i], 0, i))

    return answer