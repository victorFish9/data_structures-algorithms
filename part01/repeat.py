def find(s):
    numbers = len(s)
    for x in range(1, numbers + 1):
        if numbers % x == 0:
            string = s[:x]
            if string * (numbers // x) == s:
                return x

if __name__ == "__main__":
    print(find("aaa")) # 1
    print(find("abcd")) # 4
    print(find("abcabcabcabc")) # 3
    print(find("aybabtuaybabtu")) # 7
    print(find("abcabca")) # 7