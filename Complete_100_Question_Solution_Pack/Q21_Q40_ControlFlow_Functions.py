
# Q21-Q40 Control Flow & Functions

# Positive/Negative/Zero
n=int(input())
if n>0: print("Positive")
elif n<0: print("Negative")
else: print("Zero")

# Largest among three
a,b,c=map(int,input().split())
print(max(a,b,c))

# Leap Year
y=int(input())
print((y%400==0) or (y%4==0 and y%100!=0))

# Factorial
n=int(input())
fact=1
for i in range(1,n+1): fact*=i
print(fact)

# Fibonacci
n=int(input())
a,b=0,1
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b

def area_circle(r):
    return 3.14159*r*r

def is_prime(n):
    if n<2:return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:return False
    return True
