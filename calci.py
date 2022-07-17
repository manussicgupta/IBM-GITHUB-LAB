def calculetor():
    print("\nWellcome to Calc: This is Developed by Manu Gupta")
    operation = input('''
    Please type in the math operation you would like to complete:
    + for addition
    - for subtraction
    * for multiplication
    / for division
    ** for power
    % for modulo

    Enter Your Choise:
    ''')

    num1 = int(input("Enter first Number: "))
    num2 = int(input("Enter second Number: "))

    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        print(f"{num1} / {num2} = {num1 / num2}")
    elif operation == '**':
        print(f"{num1} ** {num2} = {num1 ** num2}")
    elif operation == '%':
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("You Press a Invalid Key")
    again()


def again():
    cal_again = input('''
    Do you want to calculate again?
    Please type y for YES or n for NO.
    ''')

    if cal_again == 'y':
        calculetor()
    elif cal_again == 'n':
        print("Thank You! for using, See You Later")
    else:
        again()


calculetor()
