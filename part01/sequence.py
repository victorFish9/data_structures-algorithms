def generate(n):
    if n < 1 or n > 1000:
        return "Virhe: n tulee olla välillä 1-1000"

    count = 0
    current_num = 0

    while count < n:
        current_num += 1
        str_num = str(current_num)
        if str_num == str_num[::-1] and str_num[0] != '0':
            count += 1

    return current_num

if __name__ == "__main__":
    print(generate(1))   # odotettu vastaus on 1
    print(generate(2))   # odotettu vastaus on 2
    print(generate(3))   # odotettu vastaus on 3
    print(generate(10))  # odotettu vastaus on 11
    print(generate(123)) # odotettu vastaus on 1141
