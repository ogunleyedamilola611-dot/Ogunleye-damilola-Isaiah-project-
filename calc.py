while True:
    print("\n ===== Mathematical calculator=====")

    print("+, -, *, /, ^, %")
    print ("c = CLEAR")
    print(" OFF = Exit")

    operation = input("Enter operation: ").upper()

    if operation == "OFF":
        print("Calculator closed.")

        break
    if operation == "C":
        print("Screen Cleared!")
        continue
    if operation not in ["+", "-", "*", "/", "^", "%"]:
        print("invalid operation!")

        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        print("Answer =", num1+num2)
        
    elif operation == "-":
        print("Answer =", num1-num2)

    elif operation == "*":
        print("Answer =", num1*num2)

    elif operation == "/":
        if num2 == 0:
            print("Error Cannot be devided by )")
        else:
             print("Answer =", num1/num2)

    elif operation == "^":
        print("Answer =", num1^num2)

    elif operation == "%":
        print("Answer =", num1%num2)