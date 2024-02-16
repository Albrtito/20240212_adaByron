def n_combinatorio(n, k):
    # print(f"n: {n}, k:{k}")
    if k == 0:
        return 1
    if n == 0:
        return 0
    return n_combinatorio(n - 1, k) + n_combinatorio(n - 1, k - 1)

def comb(n:list, k:int) -> list:
    if not n:
        return []
    if k==0:
        return []
    
    resultado = []
    for index, item in enumerate(n):
        if index > (len(n) - k):
            break
        sub = comb(n[1+index:], k-1)
        if not sub:
            resultado.append([item])
        else:
            for icomb in sub:
                resultado.append([item] + icomb)
    return resultado
if __name__ == "__main__":
    resultado = comb([1,2,3,4,5], 3)
    print("Resultado:", resultado)
    print("Longitud:", len(resultado))
