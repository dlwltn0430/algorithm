def solution(s):
    idx = len(s) // 2
    print(len(s))
    if (len(s) % 2 == 0):
        return s[idx - 1:idx + 1]
    else:
        return s[idx]