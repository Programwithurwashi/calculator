def addition(first,second):
    return first+second
def Substraction(first,second):
    return first-second
def Multiplication(first,second):
    return first*second
def division(first,second):
    return first/second

print('''Enter the operation to be performed:
       1>  Addition
       2>  Subtraction
       3>  Multiplication
       4>  Division''')

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
choice=input("Enter the Operator")
       
if choice == '+':
    print(first, "+", second, "=", addition(first,second))

elif choice == '-':
    print(first, "-", second, "=", Substraction(first,second))

elif choice == '*':
    print(first, "*", second, "=", Multiplication(first,second))

elif choice == '/':
    print(first, "/", second, "=", division(first,second))

else:
    print("Invalid Input")