def solution(s):
    s = s.upper()
    num_p = 0
    num_y = 0
    
    for i in range(len(s)):
        if (s[i] == 'P'):
            num_p += 1
        elif (s[i] == 'Y'):
            num_y += 1
    
    if(num_p == num_y):
        return True
    else:
        return False
    