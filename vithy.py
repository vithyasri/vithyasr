def countOccurrences (s, K): 
    n = len(s) 
    c1 = 0
    c2 = 0
    C = 0
    for i in range(n): 
        if s[i] == 'a': 
            c1+= 1 # Count of 'a's 
        if s[i] == 'b': 
            c2+= 1 # Count of 'b's 
        
            C += c1  
 
    return C * K + (K * (K - 1) / 2) * c1 * c2 

S = "abcb"
k = 2
print (countOccurrences(S, k)) 
  
