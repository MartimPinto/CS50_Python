import random


def main():
    try:
        while True:
            level = input("Level: ")
            if level.isdigit() and int(level) > 0:
                break
        number = random.randint(1, int(level))
        while True:
            guess = input("Guess: ")
            if guess.isdigit():
                guess = int(guess)
                if guess == number:
                    print("Just right!")
                    break
                elif guess < number:
                    print("Too small!")
                elif guess > number:
                    print("Too large!")

    except:
        pass


if __name__ == "__main__":
    main()
