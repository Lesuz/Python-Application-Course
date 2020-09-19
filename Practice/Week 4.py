#1 Calculating sum of values 1-5
sum = 0
for x in range(6):
    sum = sum + x

print (sum)
print ()

#2 Calculating the sum of even numbers between 2-40
sum = 0
for x in range(2,42, 2):
    sum = sum + x

print (sum)
print()

#3 Calculating sum between 5-100 every five number
sum = 0
for x in range(5,105, 5):
    sum = sum + x

print (sum)
print()

# 4 Throwing dice 100 times and calculating the values
import random

num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

for x in range(100):
    r = random.randint(1,6)

    if r == 1:
        num1 += 1
    elif r == 2:
        num2 += 1
    elif r == 3:
        num3 += 1
    elif r == 4:
        num4 += 1
    elif r == 5:
        num5 += 1
    elif r == 6:
        num6 += 1
print ("Amounts of different values: ")
print ("There are " + str(num1) + " of number 1.")
print ("There are " + str(num2) + " of number 2.")
print ("There are " + str(num3) + " of number 3.")
print ("There are " + str(num4) + " of number 4.")
print ("There are " + str(num5) + " of number 5.")
print ("There are " + str(num5) + " of number 6.")
print ()

# 5 Account manager with menu
value = 0
saldo = 0
while ( value != 4 ):
    print ("Select operation:")
    print ("1 = deposit")
    print ("2 = withdrawal")
    print ("3 = check balance")
    print ("4 = quit")

    value = int(input("What do you want to do? "))

    if value == 1:
        deposit = float(input("Amount: "))
        saldo = saldo + deposit
        print ()
    elif value == 2:
        withdrawal = float(input("Amount: "))
        saldo = saldo - withdrawal
        print ()
    elif value == 3:
        print (saldo)
        print()
    elif value == 4:
        print()
    else:
        print ("Illegal input")
print()


# 6 Solving an equation

x = 0
y = 0
rounds = 0
while True:
    y = 3*x**3-4*x**2+9*x+5
    if y > -0.001 and y < 0.001:
        break
    x -= 0.0001
    rounds += 1
print (x, " is the root of the equation.")
print (rounds, " rounds needed to find solution.")
 

# 7 Semipyramid
rows = 5
for x in range(0, rows+1):
    print ("m" * x)
print()

# 8 Calculating the factorial of n
n = int(input("Give a value: "))

factorial = 1

for x in range(1, n+1):
    factorial = factorial * x
    
print("The factorial of " + str(n) + " is " + str(factorial))
print()

# 9 Calcualting the exponential value
base = float(input("Give a base number(can be a real number): "))
exponent = int(input("Give a whole number as an exponent: "))
result = base

if exponent == 0:
    print("The exponential value of ",base,"^",exponent," = 1.")
else:
    for i in range(1, exponent):
        result = result * base
    print("The exponential value of ", base,"^",exponent," = ", result)    
                 

