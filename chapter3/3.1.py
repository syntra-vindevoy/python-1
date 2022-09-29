def right_justify(var_str):
    return " " * (70 - len(var_str)) + var_str


print(right_justify('monty'))
