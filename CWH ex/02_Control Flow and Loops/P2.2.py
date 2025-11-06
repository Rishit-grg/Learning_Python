a = int(input("Enter First Number: "))
op = input("Enter the operation: ")
b = int(input("Enter Second Number: "))

match op:
    case ("+") :
        print(a+b)
    case ("-") :
        print(a-b)
    case ("*") :
        print(a*b)
    case ("/") :
        if b != 0:
            print(a/b)
        else:
            print("Error: Division by zero")
    case _ :
        print("Invalid Operation")
