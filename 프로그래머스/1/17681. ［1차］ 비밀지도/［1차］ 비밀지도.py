def dec_to_bin(n, dec):
    binary = []
    
    while (dec != 0):
        binary.append(dec % 2)
        dec = dec // 2
    
    if (len(binary) < n):
        for i in range(n - len(binary)):
            binary.append(0)
            
    binary.reverse()
    
    return binary

def solution(n, arr1, arr2):
    answer = []
    
    for i in range(n):
        row = []
        for j in range(n):
            if dec_to_bin(n, arr1[i])[j] == 1 or dec_to_bin(n, arr2[i])[j] == 1:
                row.append("#")
            else: 
                row.append(" ")
        answer.append("".join(row))
        
    return answer
    #return dec_to_bin(5, 3)