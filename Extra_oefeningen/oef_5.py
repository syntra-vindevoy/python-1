def smallest_biggest(a: str):
    kleinste = a[0]
    grootste = a[0]
    for i in a[1:]:
        if i < kleinste:
            kleinste = i
        if i > grootste:
            grootste = i

    print(kleinste, grootste)


if __name__ == "__main__":
    smallest_biggest("bdzhdiao")
