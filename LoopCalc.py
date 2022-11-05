# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

#This function divide two numbers
def divide (x, y):
    if(y == 0):
        return 0
    else:
        return x / y

#This function return yes or no input String
def YesOrNo (str):
    newStr = str.upper()
    if(newStr == "YES"):
        return 0
    elif(newStr == "NO"):
        return 1
    else:
        print("Input only yes/no")
        return 2

#This function return NextCalcYes or NextCalcNo
def NextCalc ():
    next_calculation = input("Let's do next calculation? (yes/no): ")
    indexNum = YesOrNo (next_calculation)
    if (indexNum == 2):
        return NextCalc ()
    elif indexNum:
        return ReCheck ()
    else:
        return 1

#This function return ReCheckYes or ReCheckNo
def ReCheck ():
    next_calculation = input("Are you sure? (yes/no): ")
    indexNum = YesOrNo (next_calculation)
    if (indexNum == 2):
        return ReCheck ()
    elif indexNum:
        return 1
    else:
        return 0


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            num = divide(num1, num2)
            # except Divided by zero
            if not num:
                print("Error! Divided by zero!")
            else:
                print(num1, "/", num2, "=", num)

        # break the while loop if answer is no

        endIndex = NextCalc ()
        if not endIndex:
            break

    else:
        print("Invalid Input")