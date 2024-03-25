def main():
    list = {}
    while True:
        try:
            item = input().upper().strip()
            if not item:
                continue
            if item in list:
                list[item] = list[item] + 1
            else:
                list[item] = 1
        except EOFError:
            sorted_list = sorted(list.items())
            print()
            for n, items in sorted_list:
                print(f"{items} {n}")
            break

main()

