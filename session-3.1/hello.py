# Calculator

# take two integers from user
num1 = int(input("Enter first integer:"))

num2 = int(input("Enter second integer:"))


# ask for operator
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Division")
print("Press 4 for remainder")
print("Press 5 for square")
print("Press 6 for multiplication")
operator = input("<")

if operator =="1":
    print(num1 + num2)

if operator =="2":
    print(num1 - num2)

if operator =="3":
     print(num1 / num2)

if operator =="4":
     print(num1 % num2)

if operator == "5":
     print(num1 ** num2)

if operator =="6":
     print(num1 * num2)
