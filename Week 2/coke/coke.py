def main():
    due = 50
    owed = 0
    while True:
        print("Amount Due:", due)
        n = get_coin(input("Insert coin: "))
        due = due - n
        if (due <= 0):
            print("Change Owed:", abs(due))
            break

def get_coin(str):
    if str.isdigit():
        n = int(str)
        if (n == 25 or n == 10 or n == 5):
            return n
    return 0

main()
