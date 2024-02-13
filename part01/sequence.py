def generate(n):
    count = 0
    c_number = 1

    while True:
        c_str = str(c_number)
        if c_str == c_str[::-1]:
            count += 1
            if count == n:
                return int(c_str)
        c_number += 1

if __name__ == "__main__":
    print(generate(1)) # 1
    print(generate(2)) # 2
    print(generate(3)) # 3
    print(generate(10)) # 11
    print(generate(123)) # 1141