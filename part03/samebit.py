"""def count(s):
    count = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                count += 1
    return count"""

def count(s):
    counts = {}
    result = 0
    for bit in s:
        result += counts.get(bit, 0)
        counts[bit] = counts.get(bit, 0) + 1
    return result

if __name__ == "__main__":
    print(count("0101")) # odotettu vastaus 2
    # print(count("000000")) # odotettu vastaus 15
    # print(count("000111")) # odotettu vastaus 6
    # print(count("00100001101100")) # odotettu vastaus 46