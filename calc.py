while True:
    try:
        oper = input("Welcome! Please choose an operation: + - * / or quit with q: ")

        if oper == "q":
            break
        elif oper == "+":
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            result = str(x+y)
            print("Result: " + result)

        elif oper == "-":
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            result = str(x-y)
            print("Result: " + result)

        elif oper == "*":
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            result = str(x*y)
            print("Result: " + result)

        elif oper == "/":
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            result = str(x/y)
            print("Result: " + result)
        else:
            ("Unknown operation!")
    except ZeroDivisionError:
        print("Cannot devide by 0!")
    except (ValueError, TypeError):
        print("Error!")
