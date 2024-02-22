def create(t, x):
    n = t.copy()
    for i in range(len(n)):
        n[i] += x
    return n

def create_alternative(t, x):
    return[e + x for e in t]

if __name__ == "__main__":
    print(create_alternative([1,2,3],1)) # [2,3,4]
    print(create([1,1,1,1,1],4)) # [5,5,5,5,5]
    print(create([0],10**9)) # [1000000000]