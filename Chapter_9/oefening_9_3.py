def avoids(a: str, forbidden: str):
    for i in forbidden:
        for j in a:
            if i == j:
                return False
    return True


if __name__ == "__main__":
    prompt = input("Please enter a string of forbidden letters")

    with open("words.txt", "r") as input_file:
        lines = input_file.readlines()

    count = 0

    for line in lines:
        word = line.strip()
        if avoids(word, prompt):
            count += 1

    print(count)


