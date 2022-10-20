def right_justify(s):
    return f"{' ' * (70 - len(s))}{s}"


print(right_justify('monty'))
