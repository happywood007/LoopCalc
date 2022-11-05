# Program make a simple calculator
import os
import CalcFunc
import EtcFunc

f = open("C:/Users/he981/OneDrive/바탕 화면/2022학년도 2학기/오픈소스소프트웨어개발/중간과제/log/log.txt", 'a')

#This function return NextCalcYes or NextCalcNo
def NextCalc ():
    next_calculation = input("Let's do next calculation? (yes/no): ")
    indexNum = EtcFunc.YesOrNo (next_calculation)
    if (indexNum == 2):
        data = "Input only yes/no"
        print(data)
        f.write(data + "\n")
        return NextCalc ()
    elif indexNum:
        return ReCheck ()
    else:
        return 1

#This function return ReCheckYes or ReCheckNo
def ReCheck ():
    next_calculation = input("Are you sure? (yes/no): ")
    indexNum = EtcFunc.YesOrNo (next_calculation)
    if (indexNum == 2):
        data = "Input only yes/no"
        print(data)
        f.write(data + "\n")
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
            data = str(num1) + " + " + str(num2) + " = " + str(CalcFunc.add(num1, num2))
            print(data)
            f.write(data + "\n")

        elif choice == '2':
            data = str(num1) + " - " + str(num2) + " = " + str(CalcFunc.subtract(num1, num2))
            print(data)
            f.write(data + "\n")

        elif choice == '3':
            data = str(num1) + " * " + str(num2) + " = " + str(CalcFunc.multiply(num1, num2))
            print(data)
            f.write(data + "\n")

        elif choice == '4':
            num = CalcFunc.divide(num1, num2)
            if not num:
                data = "Error! Divided by zero!"
                print(data)
                f.write(data + "\n")
            else:
                data = str(num1) + " / " + str(num2) + " = " + str(num)
                print(data)
                f.write(data + "\n") 

        # check if user wants another calculation
        # break the while loop if answer is no

        endIndex = NextCalc ()
        if not endIndex:
            break

    else:
        data = "Invalid Input"
        print(data)
        f.write(data + "\n")

f.close