def count(t):
    result = 0
    n = len(t)
    for x in range(n - 1):
        print("x is :", x)
        for y in range(x + 1, n):
            print("y is :", y)
            if t[x] > t[y]:
                result += 1
    return result
if __name__ == "__main__":
    print(count([1,3,2])) # 1
    print(count([1])) # 0
    print(count([4,3,2,1])) # 6
    print(count([1,8,2,7,3,6,4,5])) # 12