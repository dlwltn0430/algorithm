def solution(s):
    l = []
    
    for i in range(len(s)):
        if s[i] == "(":
            l.append(s[i])
        else:  
            if len(l) == 0:
                return False
            else:
                l.pop()

    if len(l) == 0:
        return True
    else:
        return False