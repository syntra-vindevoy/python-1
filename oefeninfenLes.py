def convert_to_integer(test):
    counter = 0
    reverse_counter =-1
    result = 0
    for element in test:
        result += int(test[reverse_counter]) * 2 ** counter
        reverse_counter -= 1
        counter += 1
    print(result)

def convert_to_binary_string(i):
    result =""
    x = int(i)
    while x != 0:
        result += str(x % 2)
        x = (x // 2)
    reversed_answer ="".join(reversed(result))
    print(reversed_answer)
convert_to_integer("11110")
convert_to_binary_string("30")