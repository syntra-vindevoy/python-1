def right_justify(s: str):
    print((70 - len(s)) * " " + s)


if __name__ == "__main__":
    right_justify("test")
    right_justify("python")
    right_justify("hahaahahah")
    right_justify(__name__)
