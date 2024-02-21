# numbers = [4, 3, 7, 3, 2]

# print(numbers[2])
# numbers[2] = 5
# print(numbers[2]) #O(1)


# print(len(numbers)) #O(1)


# print(3 in numbers)
# print(8 in numbers)

# print(numbers.index(3))
# print(numbers.count(3)) #O(n)

# numbers2 = [1, 2, 3, 4]

# numbers2.append(5) #O(1)
# print(numbers2)

# numbers2.insert(1, 6) #O(n)
# print(numbers2) 

# numbers3 = [1, 2, 3, 4, 5, 6]

# numbers3.pop() #O(1) delete last number 
# print(numbers3) # [1, 2, 3, 4, 5]

# numbers3.pop(1) #O(n) delete number from middle of list
# print(numbers3) # [1, 3, 4, 5]

# numbers4 = [1, 2, 3, 1, 2, 3]

# numbers4.remove(3) #O(n) because method firstly need to find the number and then remove it 
# print(numbers4) # [1, 2, 1, 2, 3]


# a = [1, 2, 3, 4]
# b = a # O(1)
# a.append(5)

# print(a) # [1, 2, 3, 4, 5]
# print(b) # [1, 2, 3, 4, 5]

# a = [1, 2, 3, 4]
# b = a.copy() # O(n)
# a.append(5)

# print(a) # [1, 2, 3, 4, 5]
# print(b) # [1, 2, 3, 4]

def double(numbers):
    result = numbers
    for i in range(len(result)):
        result[i] *= 2
    return result

def double_copy(numbers):
    result = numbers.copy()
    for i in range(len(result)):
        result[i] *= 2
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print(numbers[2:6]) # [3, 4, 5, 6] # O(n), because slice will copy to new list old list content

first = [1, 2, 3, 4]
second = [5, 6, 7, 8]
print(first + second) # [1, 2, 3, 4, 5, 6, 7, 8] # O(n), because operator ->
#-> copies the elements from the list to be combined to the new list

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    print(double_copy(numbers)) # [2, 4, 6, 8]
    print(numbers) # [1, 2, 3, 4]