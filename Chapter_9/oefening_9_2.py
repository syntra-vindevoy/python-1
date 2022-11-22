def has_no_e(a: str):
    for i in a:
        if i == "e":
            return False
    return True


if __name__ == "__main__":

    with open("words.txt", "r") as input_file:
        lines = input_file.readlines()

    count = 0

    for line in lines:
        word = line.strip()
        if has_no_e(word):
            print(word)
            count += 1

    print(count / len(lines))
    print(count)
    print(len(lines))
