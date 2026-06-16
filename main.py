
welcomeMessgae = "\n ------------------------------------- \n\t SIMPLE CALCULATOR \n ------------------------------------- \n "

listValue = "  ______________________________________   \n | 1. Press 1 for addition (+)          |\n | 2. Press 2 for subtraction (-)       |\n | 3. Press 3 for division  (/)         |\n | 4. Press 4 for multiplication (x)    |\n | 5. Press 5 for exponent              |\n | 6. Press 6 for square root           |\n | 7. Press q for quit                  |\n  --------------------------------------  "

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

def exponent():
    numberFirst = float(input("Enter first number: "))
    numberSecond = float(input("Enter second number: "))

    if numberSecond % 1 != 0:
        print("Point number can't be power!")
        exponent()

    if numberFirst % 1 == 0:
        numberFirst = int(numberFirst)
    
    numberSecond = int(numberSecond)

    result = ""
    for i in range(numberSecond):
        result = result + str(numberFirst)

        if i < numberSecond -1:
            result = result + " x "
    
    resultNumber = numberFirst ** numberSecond

    print(f"{result} = {numberFirst} ^ {numberSecond} = {resultNumber} \n")

def squareRoot():
    number = float(input("Enter a number: "))

    i=0
    while i * i <= number:
        if i * i == number:
            resultNumber = i

            if number % 1 ==0:
                print(f"Square root of {int(number)} = {resultNumber} \n")
                return
            else:
                print(f"Square root of {number} = {resultNumber} \n")
                return

        i = i + 1

    print(f"{number} is not a perfect sqaure. \n")
    squareRoot()

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
    
    elif userSelection == '5':
        print("You selected exponentation \n")
        exponent()
        main()

    elif userSelection == '6':
        print("You selected square root")
        squareRoot()
        main()

    elif userSelection == 'q':
        print("______________________________ \n")

    else:
        print("Invalid Input!")
        main()

print(welcomeMessgae)
main()