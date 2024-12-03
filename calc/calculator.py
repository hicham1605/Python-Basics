def Sum(x, y):
    return x + y

def Subtract(x, y):
    return x - y

def Multiply(x, y):
    return x * y

def Squard(x, y):
    return x ** y

def Divide(x, y):
    if y == 0:
        return "Cannot divide by ZERO"
    else:
        return x / y

def CAlculator():
    print("Select an operation: ")
    print("1: Sum")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Squard")
    print("5: Divide")

    choice = input("Enter number of your operation: ")
    if choice in ['1', '2', '3', '4', '5']:
        times = int(input("how many times you want to do your operation: "))
    else:
        print("Please enter number of your operation exact.")


    for y in range (0, times):
        a = int(input("Enter the first number: "))
        b = int(input("Enter the second number: "))
        if choice == '1':
            print(f"{a} + {b} = {Sum(a, b)}")
        elif choice == '2':
            print(f"{a} - {b} = {Subtract(a, b)}")
        elif choice == '3':
            print(f"{a} * {b} = {Multiply(a, b)}")
        elif choice == '4':
            print(f"{a} ** {b} = {Squard(a, b)}")
        elif choice == '5':
            print(f"{a} / {b} = {Divide(a, b)}")
        else:
            print("Invalid input")

CAlculator()