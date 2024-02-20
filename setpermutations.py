def perm(n:list) -> list:
    result = []
    for n in range(len(n)-1): 
        nivel = []
        if n == 0: 
            nivel.append(n)

            
def permR(n:list, k: int) -> list: 
    result = []
    for i , el in enumerate(n):
        if k == 1: 
            result.append([el])
        else: 
            rest = n[:i]+n[i+1:]
            for p in perm(rest, k-1):
                result.append([el]+p)

            return result
        
