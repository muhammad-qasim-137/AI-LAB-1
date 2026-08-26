# simple calculator - no '+' sign used, only 3 variables

num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))
choice = input("choose operation (+, -, *, /): ")

if choice == '+':
    # addition done without using a '+' sign
    print("result:", num1 - (-num2))
elif choice == '-':
    print("result:", num1 - num2)
elif choice == '*':
    print("result:", num1 * num2)
elif choice == '/':
    if num2 != 0:
        print("result:", num1 / num2)
    else:
        print("error: division by zero")
else:
    print("invalid operation")
