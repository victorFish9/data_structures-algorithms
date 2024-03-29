def count(s):
    n = len(s)
    result = 0
    consecutive_count = 1

    for i in range(1, n):
        if s[i] == s[i - 1]:
            consecutive_count += 1
        else:
            result += consecutive_count * (consecutive_count + 1) // 2
            consecutive_count = 1
    result += consecutive_count * (consecutive_count + 1) // 2
    return result

if __name__ == "__main__":
    # print(count("aaa")) # 6
    print(count("abbbcaa")) # 11
    # print(count("abcde")) # 5