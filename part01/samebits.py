def count(s):
    zero = s.count("0")
    one = s.count("1")
    if zero > one:
        return one
    else:
        return zero
    
def count2(s):
    return min(s.count("0"), s.count("1"))
    
if __name__ == "__main__":
    print(count2("01101")) # 2
    print(count2("1111")) # 0
    print(count2("101111")) # 1
    print(count2("00001111")) # 4
    print(count2("100001000")) # 4
