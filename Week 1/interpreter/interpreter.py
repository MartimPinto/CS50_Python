def main():
    expression = input("Expression: ")
    if expression.count(" ") == 2:
        x, y, z = expression.split(" ")
    else:
        print("Expression must be: value [space] operation [space] value")
        return 1
    if (x.isdigit() == False or z.isdigit() == False):
        print("Only use numerical values in the first and last field")
        return 1
    if (y == "+"):
        result = float(x) + float(z)
        print(f"{result:.1f}")
    elif (y == "-"):
        result = float(x) - float(z)
        print(f"{result:.1f}")
    elif (y == "*"):
        result = float(x) * float(z)
        print(f"{result:.1f}")
    elif (y == "/"):
        if z == "0":
            print("Error: do not divide by zero")
            return 1
        result = float(x) / float(z)
        print(f"{result:.1f}")
    else:
        print("Expression must be: value [space] operation [space] value")
    return (0)

main()