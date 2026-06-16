
welcomeMessgae = "\t SIMPLE CALCULATOR \n ------------------------------------- \n "

listValue = " 1. Press 1 for addition (+) \n 2. Press 2 for subtraction (-) \n 3. Press 3 for division  (/) \n 4. Press 4 for multiplication (x) \n 5. Press q to quit \n"

def addition():
    numberFirst = float(input("Enter first number: "))
    numberSecond = float(input("Enter second number: "))

    resultNumber = numberFirst + numberSecond

    if resultNumber % 1 == 0:
        print(f"{int(numberFirst)} + {int(numberSecond)} = {int(resultNumber)}\n")
    else:
        print(f"{numberFirst} + {numberSecond} = {resultNumber}\n")

def subraction():
    numberFirst = float(input("Enter first number: "))
    numberSecond = float(input("Enter second number: "))

    resultNumber = numberFirst - numberSecond

    if resultNumber % 1 == 0:
        print(f"{int(numberFirst)} - {int(numberSecond)} = {int(resultNumber)}\n")
    else:
        print(f"{numberFirst} - {numberSecond} = {resultNumber}\n")

def division():
    numberFirst = float(input("Enter first number: "))
    numberSecond = float(input("Enter second number (divisor): "))

    if numberSecond == 0:
        print("Cananot divide with 0 \n")
        division()
    
    else:
        resultNumber = numberFirst / numberSecond

        if resultNumber % 1 == 0:
            print(f"{int(numberFirst)} / {int(numberSecond)} = {int(resultNumber)}\n")
        else:
            print(f"{numberFirst} / {numberSecond} = {resultNumber}\n")

def multiplication():
    numberFirst = float(input("Enter first number: "))
    numberSecond = float(input("Enter second number: "))

    resultNumber = numberFirst * numberSecond

    if resultNumber % 1 == 0:
        print(f"{int(numberFirst)} x {int(numberSecond)} = {int(resultNumber)}\n")
    else:
        print(f"{numberFirst} x {numberSecond} = {resultNumber}\n")

def main():
    print(listValue)

    userSelection = input("Select a Value: ")

    print()

    if userSelection == '1':
        print("You selected addition \n")
        addition()
        main()

    elif userSelection == '2':
        print("You selected subraction  \n")
        subraction()
        main()

    elif userSelection == '3':
        print("You selected division \n")
        division()
        main()

    elif userSelection == '4':
        print("You selected multiplication \n")
        multiplication()
        main()
    
    elif userSelection == 'q':
        print("______________________________ \n")

    else:
        print("Invalid Input!")
        main()

print(welcomeMessgae)
main()