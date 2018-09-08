def calculator():
    while True:
        try:
            operator = input("Welcome! Please choose : + - * / or quit with q: ")
            if operator == "q":
                break
            x = float(input("Enter value of x: "))
            y = float(input("Enter value of y: "))
            if operator == "+":
                result = str(x+y)
            elif operator == "-":
                result = str(x-y)
            elif operator == "*":
                result = str(x*y)
            elif operator == "/":
                result = str(x/y)
            else:
                ("Unknown operatoration!")
            print("Result: " + result)
        except ZeroDivisionError:
            print("Cannot devide by 0!")
        except (ValueError, TypeError):
            print("Error!")


if __name__ == '__main__':
    calculator()
