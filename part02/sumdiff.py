def create(n):
    if n == 1:
        return [1]

    result = [2, 1]
    

    for i in range(3, n + 1):
        current_sum = 0
        current_sum += i
        if i % 2 == 1:
            result.insert(i, current_sum)
        else:
            result.append(current_sum)

    return result


if __name__ == "__main__":
    print(create(6)) # [3, 1, 6, 2, 4, 5] -> 4, 7, 8, 6, 9
    # print(create(10)) # [7, 10, 3, 1, 5, 4, 8, 6, 9, 2] -> 17, 13, 4, 6, 9, 12, 14, 15, 11
    # print(create(15)) # [9, 4, 6, 14, 15, 13, 12, 11, 5, 2, 3, 8, 1, 7, 10] -> 13, 10, 20, 
