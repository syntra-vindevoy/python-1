def right_justify(txt: str) -> None:
    print(((80 - len(txt)) * " ") + txt)


right_justify("Monty")
right_justify("Python")
