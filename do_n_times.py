def do_n_times(f, n):
    for i in range(n):
        f()


def hallo():
    print("hallo")



if __name__ == "__main__":
    do_n_times(hallo, 3)


