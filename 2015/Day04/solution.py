import hashlib


def find_num(str2hash):
    range_num = range(99999999999)
    for num in range_num:
        string = str2hash + str(num)
        print(string)
        result = hashlib.md5(string.encode())

        if result.hexdigest()[0:6] == '000000':
            print(result.hexdigest())
            return num


res = find_num("iwrupvqb")
print("found:", res)
