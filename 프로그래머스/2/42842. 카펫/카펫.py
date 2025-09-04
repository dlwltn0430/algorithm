def solution(brown, yellow):
    ans = []
    
    for w in range(3, brown + yellow):
        h = (brown + yellow) // w
        if (w-2) * (h-2) == yellow:
            ans.append(w)
            ans.append(h)
            break
     
    ans.sort(reverse=True)
    
    return ans