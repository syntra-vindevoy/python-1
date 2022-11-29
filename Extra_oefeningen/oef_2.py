# converteer een int naar binair

def convert_to_binary(n: int):
    binary = ""
    while n > 0:
        d = n % 2
        binary += str(d)
        n = n // 2
    return binary[::-1]


if __name__ == "__main__":
    assert convert_to_binary(50) == "110010"
    assert convert_to_binary(10) == "1010"
