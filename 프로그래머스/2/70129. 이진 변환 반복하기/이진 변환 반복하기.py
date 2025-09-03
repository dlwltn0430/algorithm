def dec_to_bin(n):
    binary = []
    
    while(n != 0):
        binary.append(n % 2)
        n = n // 2
        
    binary.reverse()
    binary = list(map(str, binary))
    binary_str = "".join(binary)
    return binary_str   

def solution(s):
    removed = 0
    cnt = 0
    
    while(s != "1"):
        str = s.replace("0", "")
        removed += len(s) - len(str)
        s = dec_to_bin(len(str))
        cnt +=1 

    return [cnt, removed]