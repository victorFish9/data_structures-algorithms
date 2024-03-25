def create(n, k):
    lista = [i + 1 for i in range(n)]
    for i in range(n - 1, 0, -1):
        if k <= 0:
            break
        j = min(k, n-i)
        if i + j < n:
            lista[i], lista[i+j] = lista[i + j], lista[i]
        k -= j
    return lista
 
if __name__ == "__main__":
    print(create(3, 0))
    print(create(3, 1))
    print(create(3, 2))