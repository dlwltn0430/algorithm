def swap(i, j):
    tmp = i
    i = j
    j = tmp
    
    return [i, j]

def solution(sizes):
    w = []
    h = []
    
    for i in range(len(sizes)):
        if (sizes[i][0] < sizes[i][1]):
            sizes[i] = swap(sizes[i][0], sizes[i][1])
        w.append(sizes[i][0])
        h.append(sizes[i][1])
        
    return max(w) * max(h)