
def main():
    name = input("camelCase: ")
    print("snake_case: ", end="")
    for c in name:
        if c.isupper():
            c = c.lower()
            print("_", end="")
        print(c, end="")
    print()

main()
