def get_operation():
    print("1. + (add)")
    print("2. - (subtract)")
    print("3. * (multiply)")
    print("4. / (divide)")
    print("5. END (stop calculator)")
    print()

    return input("Please give the operation: ")


def get_value():
    return input("Please enter the value: ")


def main():
    operation = 0
    calculated = 0

    while operation != 5:
        operation = get_operation()

        if operation == "5":
            break

        value = float(get_value())

        if operation == "1":
            calculated += value
        elif operation == "2":
            calculated -= value
        elif operation == "3":
            calculated *= value
        else:
            calculated /= value

        print()
        print(f"Intermediate result: {calculated}")
        print()

    print(f"Final result: {calculated}")


if __name__ == "__main__":
    main()
