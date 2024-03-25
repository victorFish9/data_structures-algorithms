import random 
#O(n^2)
def best_profit1(prices):
    n = len(prices)
    best = 0
    for i in range(n):
        min_price = min(prices[0:i+1])
        best = max(best, prices[i] - min_price)
    return best
#O(n)
def best_profit2(prices):
    n = len(prices)
    best = 0
    min_price = prices[0]
    for i in range(n):
        min_price = min(min_price, prices[i])
        best = max(best, prices[i] - min_price)
    return best

#O(n^2)
def count_ways1(bits):
    n = len(bits)
    result = 0
    for i in range(n):
        for j in range(i + 1, n):
            if bits[i] == '0' and bits[j] == '1':
                result += 1
    return result

#O(n)
def count_ways2(bits):
    n = len(bits)
    result = 0
    zeros = 0
    for i in range(len(bits)):
        if bits[i] == '0':
            zeros += 1
        if bits[i] == '1':
            result += zeros
    return result

#O(n^2)
def count_splits1(numbers):
    n = len(numbers)
    result = 0
    for i in range(n - 1):
        left_sum = sum(numbers[0:i + 1])
        right_sum = sum(numbers[i + 1:])
        if left_sum == right_sum:
            result += 1
    return result

#O(n^2)
def count_splits2(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum = sum(numbers[i+1:])
        if left_sum == right_sum:
            result += 1
    return result

#O(n)
def count_splits3(numbers):
    n = len(numbers)
    result = 0
    left_sum = 0
    total_sum = sum(numbers)
    for i in range(n - 1):
        left_sum += numbers[i]
        right_sum = total_sum - left_sum
        if left_sum == right_sum:
            result += 1
    return result

def count_lists(numbers):
    n = len(numbers)
    a = b = -1
    result = 0
    for i in range(1, n):
        if numbers[i] != numbers[i - 1]:
            if numbers[i] != numbers[a]:
                b = a
            a = i - 1
        result += a -b
    return result

# while True:
#     n = random.randint(1, 20)
#     prices = [random.randint(1, 10) for _ in range(n)]

#     result_1 = best_profit1(prices)
#     result_2 = best_profit2(prices)

#     print(prices, result_1, result_2)

#     if result_1 != result_2:
#         print("Error")
#         break


if __name__ == "__main__":
    print(best_profit2((3,7,5,1,4,6,2,3)))