def count(a, b):
    result = 0
    a_index = {a[i]: i for i in range(len(a))}
    if a == b:
        return 0
    
    for x in range(len(a)):
        curr_element = b[x]

        if a_index[curr_element] < x:
            result += 1

    return result

if __name__ == "__main__":
    print(count([2,3,4,1], [1,2,3,4])) # 3
    print(count([1,2,3,4], [1,2,3,4])) # 0
    print(count([4,7,3,1,6,2,5], [5,6,1,2,4,3,7])) # 3
    print(count([5,4,9,1,8,3,2,6,7], [6,2,8,4,9,1,5,7,3])) # 5