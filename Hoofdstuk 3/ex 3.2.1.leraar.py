def right_justify(txt: str) -> str:
    return ((80 - len(txt)) * " """) + txt

print (right_justify("monty"))