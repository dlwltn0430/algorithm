def solution(s):
    stack = []
    
    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    
    if not stack:
        return 1
    else:
        return 0
