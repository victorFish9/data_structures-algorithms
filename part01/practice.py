a = [5, 4, 1, 7, 9, 6]

def count_even(numbers):
    return sum(x % 2 == 0 for x in numbers)

print(count_even([5, 4, 1, 7, 9, 6]))
print(count_even([1,2,3]))
print(count_even([2, 2, 2, 2, 9, 6]))