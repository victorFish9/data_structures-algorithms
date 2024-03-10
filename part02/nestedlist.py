def count(t):
    to_count = 0
    for item in t:
        if isinstance(item, list):
            to_count += count(item)
        elif isinstance(item, int):
            to_count += 1
    return to_count

# ANSWER

def count(t):
    result = 0
    for x in t:
        if type(x) == list:
            result += count(x)
        else:
            result += 1
    return result




if __name__ == "__main__":
    print(count([1,2,3])) # 3
    print(count([1,[2,3],4,5,[6]])) # 6
    print(count([1,[1,[1,[1]]]])) # 4
    print(count([[1,2,[3,4]],5,[[6,[7],8]]])) # 8