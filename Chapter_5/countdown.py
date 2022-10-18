start = 10


def count_down(n):
    if n == 0:
        print("Blast off")
    else:
        print(n)
        count_down(n - 1)


if __name__ == "__main__":
    prompt = "Aftellen begint vanaf: \n"
    start = int(input(prompt))
    count_down(start)


