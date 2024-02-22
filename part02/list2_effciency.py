import random
import time

n = 10 ** 5

numbers = []

def addNum():
    for i in range(1, n + 1):
        numbers.append(i)
    return numbers

def removeNum():
    for i in range(1, n + 1):
        numbers.pop(i)
    return numbers


print(addNum())

random.seed(1337)


start_time = time.time()
result = addNum()
end_time = time.time()

# print("result: ", result)
print(start_time, end_time)
print("Adding numbers time: ", round(end_time - start_time, 7), "s")

start_time = time.time()
result = removeNum()
end_time = time.time()

# print("result: ", result)
print("Removing numbers time: ", round(end_time - start_time, 5), "s")

