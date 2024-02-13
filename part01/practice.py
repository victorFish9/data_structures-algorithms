import random
import time

def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)

# print(count_even([5, 4, 1, 7, 9, 6]))

def max_diff(numbers):
    result = 0
    for x in numbers:
        for y in numbers:
            result = max(result, abs(x - y))
    return result
    
def max_diff2(numbers):
    numbers = sorted(numbers)
    return numbers[-1] - numbers[0]

def max_diff3(numbers):
    return max(numbers) - min(numbers)

# print(max_diff([3, 2, 6, 5, 8, 5]))
# print(max_diff2([3, 2, 6, 5, 8, 5]))
# print(max_diff3([3, 2, 6, 5, 8, 5]))

n = 10000000
print('n:', n)
random.seed(1337)
numbers = [random.randint(1, 10**6) for _ in range(n)]

start_time = time.time()
restult = max_diff3(numbers)
end_time = time.time()

# print('result: ', restult)
# print('time: ', round(end_time - start_time, 2), "s")

def count_even(numbers):
    restult = 0
    for x in numbers:
        if x % 2 == 0:
            restult += 1
    return restult