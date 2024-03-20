def main():
    str = input("Input: ")
    print("Output: ", end="")
    for c in str:
        check_vowel(c)
        if (check_vowel(c) == False):
            print(c, end="")
    print()

def check_vowel(c):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for i in vowels:
        if i == c:
            return True
    return False

main()
