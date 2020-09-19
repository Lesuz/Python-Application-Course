import random
# 1 Returning the average of 2 integers
def intaverage (in1,int2):
    average = (int1+int2)/2
    return average

# Call
int1 = int(input("Give the first value: "))
int2 = int(input("Give the seciond value: "))

resultint = intaverage(int1,int2)
print ("The average of the values is :", resultint)
print ()

# 2 Returning the average of 4 floating point values
def floataverage (f1,f2,f3,f4):
    faverage = (f1+f2+f3+f4)/4
    return faverage

# Call
print ("Give 4 float values.(Use dot instead of comma)")
f1 = float(input("First value: "))
f2 = float(input("Second value: "))
f3 = float(input("Third value: "))
f4= float(input("Fourth value: "))

resultfloat = floataverage(f1,f2,f3,f4)
print ("The average of the values is :", resultfloat)
print ()


# 3 Return the sum of an array
array =[1,2,3,4,5]
print (array)
sum = 0
def arraysum (sum,array):
    for i in range(0, len(array)):
        sum = sum + array[i]
    return sum

# Call
sumresult = arraysum(sum,array)
print ("The sum of the arrays is : ", sumresult)
print ()

# 4 Return the factorial
def factorial (z):
    factorial = 1
    for x in range(1, z+1):
        factorial = factorial * x
    return factorial

# Call
n = int(input("Give a value: "))
factorialn = factorial(n)
print ("The factorial of ",n," is: ", factorialn)
print ()

# 5 Returns the biggest of 3 integers
def biggest(valueA,valueB,valueC):
        if valueA > valueB and valueA > valueC:
            return valueA
        elif valueB > valueA and valueB > valueC:
            return valueB
        elif valueC > valueA and valueC > valueB:
            return valueC
        elif valueA == valueB or valueA == valueC or valueB == valueC:
            return 'There is not one value that is bigger than the two others'

#Call
valueA = int(input("Give the value a =  "))
valueB = int(input("Give the value b = "))
valueC = int(input("Give the value c = "))

biggestvalue = biggest(valueA,valueB,valueC)
print ("The biggest value is: ", biggestvalue)
print ()

# 6 Returns the BMI
def BMI(weight, height):
    bmi = weight / ((height / 100) * (height / 100))
    return bmi

#Call
weight = float(input("Give weight in kilograms: "))
height = float(input("Give height in centimeters: "))
BMIresult = BMI(weight,height)
print ("The BMI is {:.2f}".format(BMIresult))
print ()

# 7 Function returns the biggest of 5 integers
def biggestint(arrayint):
    arrayint.sort()
    return arrayint[len(arrayint)-1]

#Call
arrayint = []
for i in range(5):
    arrayint.append(random.randint(0,10))
print ("Randomized values in an array: ",arrayint)
print ("Biggest int of 5 is: ",biggestint(arrayint))
print()


# 8 Calculating amount of combinations
def combination (n,r):
    combinations = (factorial(r)/ (factorial(n) * (factorial(r-n))))
    return combinations

# Call
n = int(input("How many values per combination: "))
r = int(input("How many values in all: "))
combis = combination(n,r)
print (combis)
print ()

# 9 Calculates the standard deviation
def deviation(list,sum,squaredSum):
    for i in range(len(list)):
        sum = sum + list[i]
    meanOfList = sum/len(list)

    for x in range(len(list)):
        squaredSum = squaredSum + (list[x] - meanOfList)**2
    #squaredMean = squaredSum/(len(list)-1)
    standDeviation = (squaredSum/(len(list)-1))**0.5
    return standDeviation
#Call

list = [9,2,5,4,12,7]
sum = 0
squaredSum = 0
standard_deviation = deviation(list,sum,squaredSum)
print ("The standard deviation of ",list," is {:.2f}".format(standard_deviation))
print ()    

# 10 Searches for a value in an array
def findingvalue(value,array):
    result = "Value not found."
    for i in range(len(array)):
     if array[i] == value:
         result = "Found in index " + str(i)
         break;
    return result
#Call
import random

array = []
for x in range(15):
    array.append(random.randint(0,100))
print (array)

value = int(input("What value are you looking for?: "))

foundvalue = findingvalue(value,array)
print (foundvalue)
print()


# 11 Calculates the square root of value 2
def squareroot():
    i = 1
    while(True):
        if i**2>2:
            break;
        i += 0.000001
    return i
        
#Call
print ("{:.5f}".format(squareroot()))

