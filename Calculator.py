#These are the fuctions I defined for basic arithmetic operations
def addition(numb1,numb2):
    return numb1 + numb2
def subtraction(numb1,numb2):
    return numb1 - numb2
def multiplication(numb1,numb2):
    return numb1 * numb2
def division(numb1,numb2):
    return numb1 / numb2


print("Lets do some math!")
option = input("Select an option 1-4.\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")

if option in ("1", "2", "3", "4"):
    x = float(input("Pick your first number: "))
    y = float(input("Pick your second number: "))

    if option == "1":
        print("The sum is", addition(x,y))

    elif option == '2':
        print("The difference is", subtraction(x,y))

    elif option == '3':
        print("The product is", multiplication(x,y))

    elif option == '4':
        print("The quotient is", division(x,y))

else:
    print("You didn't select a number 1-4. Try again.")