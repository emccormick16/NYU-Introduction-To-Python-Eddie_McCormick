grade = int(input("What's your grade?\n"))
if grade > 100:
    print("That's not possible!")
if grade > 89:
    print("A")
elif grade > 79:
    print("B")
elif grade > 69:
    print("C")
elif grade > 59:
    print("D")
elif grade > -1:
    print("F")
else:
    print("Not good!")
