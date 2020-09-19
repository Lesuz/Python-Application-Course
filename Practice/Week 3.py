# 1 Is value over 100
value = int(input("Give a whole number: "))
if value > 100:
    print ("The value is bigger than 100!")
else:
    print ("The value is not bigger than 100!")
print ()


# 2 Weekday number
weekdaynumber = int(input("Give a weekday number: "))
if weekdaynumber == 1:
    print ("Monday")
elif weekdaynumber == 2:
    print ("Tuesday")
elif weekdaynumber == 3:
    print ("Wednesday")
elif weekdaynumber == 4:
    print ("Thursday")
elif weekdaynumber == 5:
    print ("Friday")
elif weekdaynumber == 6:
    print ("Saturday")
elif weekdaynumber == 7:
    print ("Sunday")
else:
    print("There are only 7 days in a week!")
print ()

# 3 BMI calculator plus text
weight = float(input("Give weight in kilograms: "))
height = float(input("Give height in centimeters: "))
BMI = weight / ((height / 100) * (height / 100))
print ('The BMI is {:.1f}'.format(BMI))

if BMI < 18.5:
    print ("Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print ("Healthy weight")
elif BMI >= 25 and BMI <= 29.9:
    print ("Overweight")
elif BMI >= 30:
    print ("Obese")
else:
    print ("The BMI is not realistic.")
print ()

# 4 Number of days in a month
monthnumber = int(input("Give a month(in number): "))
if monthnumber == 1:
    print ("January has 31 days.")
elif monthnumber == 2:
    print ("February has 28 days unless it is a leap-year. Leap-year has 29 days in february. ")
elif monthnumber == 3:
    print ("March has 31 days.")
elif monthnumber == 4:
    print ("April has 30 days.")
elif monthnumber == 5:
    print ("May has 31 days.")
elif monthnumber == 6:
    print ("June has 30 days.")
elif monthnumber == 7:
    print ("July has 31 days.")
elif monthnumber == 8:
    print ("August has 31 days.")
elif monthnumber == 9:
    print ("September has 30 days.")
elif monthnumber == 10:
    print ("October has 31 days.")
elif monthnumber == 11:
    print ("November has 30 days.")
elif monthnumber == 12:
    print ("December has 31 days.")
else:
    print("There are only 12 months in a year!")
print ()

# 5 Triangles
side1 = float(input("Give the lenght of the first side: "))
side2 = float(input("Give the lenght of the second side: "))
side3 = float(input("Give the lenght of the third side: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    if side1 == side2 == side3:
        print ("The triangle is an equilateral triangle.")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        print ("The triangle is an isosceles triangle.")
    elif side1**2 + side2**2 == side3**2 or side2**2 + side3**2 == side1**2 or side1**2 + side3**2 == side2**2:
        print ("The triangle is a right angle triangle.")
    else:
        print ("All I can tell is that it is a triangle.")
else:
    print ("The lenghts given don't make up a triangle.")

print ()

# 6 Finding the biggest value way1, using if else and logical operators

valueA = int(input("Give the value a =  "))
valueB = int(input("Give the value b = "))
valueC = int(input("Give the value c = "))

if valueA > valueB and valueA > valueC:
    print ("Value a = " + str(valueA) + " is the biggest value given.")
elif valueB > valueA and valueB > valueC:
    print ("Value b = " + str(valueB) + " is the biggest value given.")
elif valueC > valueA and valueC > valueB:
    print ("Value c = " + str(valueC) + " is the biggest value given.")
else:
    print ("There is not one value that is bigger than the two others")
print ()

# 6 Finding the biggest value way2, using only if else

A = int(input("Give the value a = "))
B = int(input("Give the value b = "))
C = int(input("Give the value c = "))

if A > B:
    if A > C:
        print ("Value A = " + str(A) + " is the biggest value found.")
    elif C > A:
        print ("Value C = " + str(C) + " is the biggest value found.")
    else:
        print ("There is no biggest found value that is bigger than the two others.")
elif B > C:
    print ("Value B = " + str(B) + " is the biggest value found.")
elif C > B:
    print ("Value C = " + str(C) + " is the biggest value found.")
else:
    print ("There is not one value found that is bigger than the two others.")
print ()

# 6 Finding the biggest value way3, using if else and logical operators in a different way

a = int(input("Give the value a = "))
b = int(input("Give the value b = "))
c = int(input("Give the value c = "))

if a<b<c or b<a<c:
    print ("Value c = " + str(c) + " is the biggest value found.")
elif a<c<b or c<a<b:
    print ("Value b = " + str(b) + " is the biggest value found.")
elif c<b<a or b<c<a:
    print ("Value a = " + str(a) + " is the biggest value found.")
else:
    print ("There is not one value found that is bigger than the two others.")
print ()
