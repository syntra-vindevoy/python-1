def int_to_bin(integer):
        binary = format(integer, 'b')
        print(binary)
        return binary

assert int_to_bin(3) == "11"
assert int_to_bin(50) == "110010"

