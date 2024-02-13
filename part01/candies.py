def count(a, b, c):
    max_amount = 0

    for i in range(c // a + 1):
        j = (c - i * a) // b
        max_amount = max(max_amount, i + j)

    return max_amount

def count2(a, b, c):
    return c // min(a, b)

if __name__ == "__main__":
    # print(count2(3, 4, 11))  #3
    print(count2(5, 1, 100)) #100
    # print(count2(2, 3, 1))   #0
    # print(count2(2, 3, 9))   #4