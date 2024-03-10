import math

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        # print(list[high])
        if guess == item:
            return mid
        if guess > item:
            high= mid - 1
        else:
            low = mid + 1
    return None

numbers = [1, 3, 5, 7, 9]

n = 4
print(math.log2(n))

# if __name__ == "__main__":
#     print(binary_search(numbers, 3))
#     print(binary_search(numbers, -1))