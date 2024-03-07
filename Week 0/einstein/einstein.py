def square(n):
    return (n * n)

def main():
    m = int(input("m: "))
    e = m * square(300000000)
    print("E:", e)

main()
