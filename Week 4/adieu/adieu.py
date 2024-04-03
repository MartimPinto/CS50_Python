import inflect


def main():
    mylist = []
    try:
        while True:
            name = input("Name: ")
            if not name:
                break
            mylist.append(name)
    except EOFError:
        mylist = inflect.engine().join(mylist)
        print("Adieu, adieu, to", mylist)


if __name__ == "__main__":
    main()
