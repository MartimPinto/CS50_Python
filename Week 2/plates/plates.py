def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False
    for i in s:
        if not i.isalnum():
             return False
    if s[0:2].isdigit():
        return False
    for j in range(2, len(s) - 1):
        if s[j].isdigit() and not s[j + 1].isdigit():
            return False
    if not check_zero(s):
        return False
    else:
        return True

def check_zero(s):
    j = 0
    i = 0
    while (i < len(s)):
        if s[i].isdigit() and s[i] == '0' and j == 0:
            return False
        if s[i].isdigit():
            j += 1
        i += 1
    return True

main()
