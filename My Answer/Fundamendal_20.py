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

#
