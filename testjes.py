print("hahaha", end="\ntest")
print("blalal")

print("haha" * (10 > 1) + "nope" * (10 > 1))

spaces = 5 * " "
print(f"{spaces}spaties")

n = "haha.uhndiue.udniudad.ndaie"
n = n.split(".")
print(n)
print("".join(n))


def is_true(a: bool):
    return a == True


if __name__ == "__main__":
    assert is_true(True), f"fail"
