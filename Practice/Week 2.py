# 1 Define suitable variables
a = 999999
print (type (a))

b = 5.55555555555
print (type (b))

c = 'x'
print (type (c))

d = "Kokkola"
print (type (d))

e = 2.33
print (type (e))

f = 10
print (type (f))

g = 300
print (type (g))

h = 9000000000
print (type (h))

i = 3000000000
print (type (i))

print ()


# 2 Calculating resistance
U = float(input("Give the voltage: "))
I = float(input("Give the current: "))
R = U / I
print (R)
print ()

# 3a Calculating time in hours
s = int(input("Give the speed in km/h: "))
d = float(input("Give the distance in km: "))
t = int((d * 1000) / (s / 3.6) / 3600)
print ("Duration: " + str(t) + " hour(s)")
print ()

# 3b Calculating time in hours and minutes
s = int(input("Give the speed in km/h: "))
d = float(input("Give the distance in km: "))
t = int((d * 1000) / (s / 3.6))
hours = t // 3600
t %= 3600
minutes = t // 60
print ("Duration: " + str(hours) + " hour(s) and " + str(minutes) + " minutes.")
print ()

# 4 Calculatig the BMI
weight = float(input("Give weight in kilograms: "))
height = float(input("Give height in centimeters: "))
BMI = weight / ((height / 100) * (height / 100))
print ('The BMI is {:.1f}'.format(BMI))
print ()

# 5 Dollars to Euros converter
dollars = float(input("Dollars: "))
euros = dollars * 0.91
print (str(dollars) + ' in euros is : {:.2f}'.format(euros))
print ()

# 6 Seconds to hours, minutes and seconds converter.
time = int(input("Input the seconds: "))
hours = time// 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print (str(hours) + " hours " + str(minutes) + " minutes " + str(seconds) + " seconds ")
print ()

# 7 Convert euros to bills
value = int(input("Give the amount in euros: "))
bill500 = value // 500
value -= bill500 * 500
bill200 = value // 200
value -= bill200 * 200
bill100 = value // 100
value -= bill100 * 100
bill50 = value // 50
value -= bill50 * 50
bill20 = value // 20
value -= bill20 * 20
bill10 = value // 10
value -= bill10 * 10
bill5 = value // 5
value -= bill5 * 5
print (str(bill500) + " x 500 euro bills")
print (str(bill200) + " x 200 euro bills")
print (str(bill100) + " x 100 euro bills")
print (str(bill50) + " x 50 euro bills")
print (str(bill20) + " x 20 euro bills")
print (str(bill10) + " x 10 euro bills")
print (str(bill5) + " x 5 euro bills")
print (str(value) + " euros in coins.")
print ()

