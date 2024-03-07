def convert(str):
    return (str.replace(':)', '🙂').replace(':(', '🙁'))

def main():
    str = input("")
    print(convert(str))

main()
