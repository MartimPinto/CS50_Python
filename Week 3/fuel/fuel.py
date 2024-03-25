def main():
    while True:
        try:
            x = get_fraction("Fraction: ")
            x = get_value(x)
            print(x)
            break
        except (ValueError, ZeroDivisionError):
             pass


def get_fraction(prompt):
        fraction = input(prompt)
        x, y = fraction.split("/")
        if int(y) <= 0:
             raise ZeroDivisionError
        if not x.isdigit() or not y.isdigit() or int(x) > int(y):
             raise ValueError
        return (round((int(x) / int (y)) * 100))

def get_value(x):
     if x <= 1:
          return "E"
     elif x >= 99:
          return "F"
     else:
          return (str(x) + "%")

main()
