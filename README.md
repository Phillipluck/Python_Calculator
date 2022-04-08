# Python_Calculator
Written on 4/7/2022  

I have essentially zero coding experience, so I decided to start teaching myself Python on April 4th, 2022.  The following is a write-up of my progress thus far.  
  
I started out by watching some youtube videos about some of the most basic concepts.  
In no particular order, I learned about:
* Variables
* if/else statements
* Functions
* Operators

This was the result of about an hour of videos and some practice: [first_script.py](https://github.com/Phillipluck/Python_Calculator/blob/main/first_script.py)
```python
# Playing around with some things I've learned.


first_name = "Phillip"
last_name = "Luckiewicz"
age = 28
new_student = True

if new_student:
    new_student = " is a new student. "
else:
    new_student = " is not a new student. "

print(first_name, last_name + str(new_student) + "He is " + str(age) + " years old.")
print("This was a test script.")
print("Hello")
print("testing auto save")
```  
For my next script, I followed along with a youtube video, but I did learn some cool things about floats, integer and receiving user input.  
See here: [Addition calculator.py](https://github.com/Phillipluck/Python_Calculator/blob/main/Addition%20calculator.py)  
```python
# int = whole numbers
# float = decimals


print("Lets develop a simple addition calculator!")
first_number = float(input("What is your first number? "))
second_number = float(input("What is your second number? "))
sum = first_number + second_number
print("sum: " +str(sum))
```  
Next, I wanted to make a basic arithmetic calculator, just to see if I can! I tried my best to not use google or watch any youtube videos for help, though I did refer to a cheatsheet to figure out how to define my own functions.  
Check it out here: [Calculator.py](https://github.com/Phillipluck/Python_Calculator/blob/main/Calculator.py)  
```python
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
```  

All in all, I'm pretty happy with my progress. Coding is making me think in a way that I never have before...  A much more logical, top/down way of thinking.  Still so much to learn, but I'm having fun!  I wish I had started learning sooner.
