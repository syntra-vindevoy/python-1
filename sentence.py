import string


def min_max_sentence(sentence: str):
    min_char = max_char = None

    for char in sentence:
        if char in string.ascii_letters:
            if min_char is None:
                min_char = max_char = char
                continue

            if char < min_char:
                min_char = char
                continue

            if char > max_char:
                max_char = char

    return min_char, max_char


def min_max_sentence_2(sentence, ignore_case: bool = True):
    min_char = max_char = None
    min_pos = max_pos = pos = -1

    if ignore_case:
        investigate = sentence.lower()
    else:
        investigate = sentence

    for char in investigate:
        pos += 1

        if char in string.ascii_letters:
            if min_char is None:
                min_char = max_char = char
                continue

            if char < min_char:
                min_char = char
                min_pos = pos
                continue

            if char > max_char:
                max_char = char
                max_pos = pos

    return sentence[min_pos], sentence[max_pos]


def main():
    assert min_max_sentence("Yves") == ("Y", "v")
    assert min_max_sentence("mijn zoon woont in sint-truiden") == ("d", "z")
    assert min_max_sentence("'Godverdomme', zei de leraar") == ("G", "z")

    assert min_max_sentence_2("Mijn zoon woont in sint-truiden", ignore_case=True) == ("d", "z")


if __name__ == "__main__":
    main()
