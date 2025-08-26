def solution(n):
    l = list(str(n))
    l = list(map(int, l))
    l.sort(reverse=True)
    l = map(str, l)
    l = "".join(l)
    
    return int(l)