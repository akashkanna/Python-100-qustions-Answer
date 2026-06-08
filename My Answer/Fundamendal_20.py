# Module 1: Python Programming Fundamentals (20 Questions)

# 1.	Print "Hello World" on screen. 
print("Hello World")

# 2.	Take user name input and print a welcome message. 
name =input("Enter your name: ")
print(f"Welcome {name}")

# 3.	Add two numbers entered by the user. 
num1 = int(input("enter the num1: "))
num2 = int(input("enter the num2: "))
print("the Add number is",num1+num2)

# 4.	Find the area of a rectangle. 

l =int(input("Enter the length of the rectangle: "))
w =int(input("Enter the width of the rectangle: "))
area = l * w
print("The area of the rectangle is:", area)

# 5.	Convert Celsius to Fahrenheit.

cel =int(input("enter the Cel"))
fah = (cel*9/5)+32
print(f"the Fah {cel}is {fah}")


#6.	Swap two variables using a third variable.

a = int(input("enter the value a"))
b = int(input("enter the valeu b"))
c = a
a = b
b = c
print(f"After swapping, a = {a} and b = {b}")

#7.	Swap two variables without using a third variable. 

a = int(input("enter the value a"))
b = int(input("enter the valeu b"))
a = a + b
b = a - b
a = a - b
print(f"After swapping, a = {a} and b = {b}")

#8.	Find the square and cube of a number. 
num = int(input("enter the number"))
square = num ** 2
cube = num ** 3
print(f"The square of {num} is {square} and the cube is {cube}")

# 9.	Check the data type of a variable. 
var = input("Enter a value: ")
print(f"The data type of {var} is {type(var)}")

# 10.	Convert string input into integer and float. 
str_num = input("Enter a number: ")
int_num = int(str_num)
float_num = float(str_num)
print(f"The integer value of {str_num} is {int_num}")
print(f"The float value of {str_num} is {float_num}")

# 11.	Calculate simple interest. 
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))     
time = float(input("Enter the time period: "))
interest = (principal * rate * time) / 100
print(f"The simple interest is: {interest}")

# 12.	Calculate BMI from height and weight. 
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")

# 13.	Find the largest of two numbers. 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if num1 > num2:
    print(f"The largest number is: {num1}")
else:
    print(f"The largest number is: {num2}")

# 14.	Find the remainder when two numbers are divided. 
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
remainder = num1 % num2
print(f"The remainder when {num1} is divided by {num2} is: {remainder}" )

# 15.	Calculate the average of three numbers. 
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print(f"The average of the three numbers is: {average}")

# 16.	Concatenate first name and last name. 
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name    
print(f"Your full name is: {full_name}")

# 17.	Count the number of characters in a string. 
string = input("Enter a string: ")
char_count = len(string)
print(f"The number of characters in the string is: {char_count}")

# 18.	Convert a string to uppercase and lowercase.
string = input("Enter a string: ")
upper = string.upper()
lower = string.lower()
print(f"The uppercase of the string is: {upper}")
print(f"The lowercase of the string is: {lower}")

# 19.	Check whether a number is even or odd. 
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")

# 20.	Find the ASCII value of a character. 
char = input("Enter a character: ")
ascii_value = ord(char)
print(f"The ASCII value of {char} is: {ascii_value}")
