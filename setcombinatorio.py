def comb(n:list, k:int) -> list: 
    #Casos base: 
    if not n:
        return []
    if k == 0: 
        return []
    if len(n) == k:
        return []

n = [1,2,3,4,5]
k = 2
print(comb(n,k))
