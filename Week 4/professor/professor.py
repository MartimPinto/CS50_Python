import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        while True:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    score += 1
                    break
                else:
                    tries += 1
                    print("EEE")
                if tries == 3:
                    print(f"{x} + {y} = {x + y}")
                    break
            except:
                pass
    print("Score:", score)


def get_level():
    try:
        while True:
            n = input("Level: ")
            if n.isdigit() and 1 <= int(n) <= 3:
                return int(n)
    except:
        pass


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    elif level == 3:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()
