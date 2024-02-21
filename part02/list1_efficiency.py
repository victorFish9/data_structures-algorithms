import random
import time

numbers = []

def addNum(a):
    numbers.append(a)
    return numbers

def removeNum():
    for _ in range(n):
        if numbers:
            numbers.pop()
    return numbers

n = 10**5
print('n: ', n)

random.seed(1337)
a = [random.randint(1, n) for _ in range(n)]

start_time = time.time()
result = addNum(a)
end_time = time.time()

print("result: ", numbers)
print(start_time, end_time)
print("Adding numbers time: ", round(end_time - start_time, 7), "s")


start_time = time.time()
result = removeNum()
end_time = time.time()

print("result: ", result)
print("Removing numbers time: ", round(end_time - start_time, 5), "s")

# if __name__ == "__main__": 
#     print(addNum(2))
