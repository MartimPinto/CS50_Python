answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
answer = answer.lower().replace(" ", "")
match answer:
    case "42" | "forty-two" | "fortytwo":
        print ("Yes")
    case _:
        print ("No")