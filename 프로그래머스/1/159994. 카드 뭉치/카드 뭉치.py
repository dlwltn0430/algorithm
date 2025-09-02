def solution(cards1, cards2, goal):
    answer = "Yes"
    c1 = []
    c2 = []
    
    for word in goal:
        if (word in cards1):
            idx_c1 = cards1.index(word)
            c1.append(idx_c1)
        elif (word in cards2):
            idx_c2 = cards2.index(word)
            c2.append(idx_c2)

    if (sorted(c1) != c1):
        answer = "No"
    elif (sorted(c2) != c2):
        answer = "No"
    elif 0 not in c1 or 0 not in c2:
        answer = "No"
    
    for i in range(len(c1) - 1):
        if c1[i+1] - c1[i] != 1:
            return "No"
        
    for i in range(len(c2) - 1):
        if c2[i+1] - c2[i] != 1:
            return "No" 
        
    return answer