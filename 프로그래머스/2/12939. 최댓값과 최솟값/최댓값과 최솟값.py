def solution(s):
    ans = []
    s = list(map(int, s.split(" ")))
    ans.append(min(s))
    ans.append(max(s))
    ans = list(map(str, ans))
    ans = " ".join(ans)
    
    return ans