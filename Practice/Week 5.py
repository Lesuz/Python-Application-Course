# 1 Array of 30 values and their sum and average
import random

array1 = []
for x in range(30):
    array1.append(random.randint(0,100))
print(array1)

sum = 0
for i in range(0, len(array1)):
    sum = sum + array1[i]

average = sum/len(array1)
print ("The sum of the values in the arrays is " + str(sum) + " and the average of the array is : {:.1f}".format(average))
print ()

# 2 Finding maximun of an array
max = array1[0]
for x in range(1,30):
    if array1[x] > max:
        max = array1[x]
print("Biggest value in the array is " + str(max))
print()

# 3 Searching for a value in an array
value = int(input("What value are you looking for? "))
result = "Value not found."
for i in range(1,30):
     if array1[i] == value:
         result = "Found in position " + str(i)
         break;
print(result)
print ()

# 4 Fillin 2 arrays and calculating sum
array1 = []
for x in range(5):
    array1.append(random.randint(0,100))
array2 = []
for x in range(5):
    array2.append(random.randint(0,100))
print ("Array 1: " + str(array1))
print ("Arrays 2: " + str(array2))

arraysum = []

for i in range (0,5):
    arraysum.append(array1[i] + array2[i])
print ("The sum array is: " + str(arraysum))

print ()

# 5 Generating a lottorow

lottorow = []
for i in range(7):
    num = random.randint(1,40)
    while num in lottorow:
        num = random.randint(1,40)    
    lottorow.append(num)
lottorow.sort()
    
print ("The lottorow is ",lottorow)
print()

# 6 Own example of using methods on python.org
cities = ["Helsinki","Vantaa","Espoo","Joensuu"]
print ("Some cities in Finland: ", cities)
print()
#Using list.append(x)
cities.append("Tampere")
print ("Added Tampere to list of cities in Finland")
print ("Cities: ",cities)
print()

#Using list.extend(iterable)
cities2 = ["Hanko","Iisalmi","Kerava"]
print("Adding more cities to the list from another list.")
cities.extend(cities2)
print (cities)
print ()

#Using list.insert(i,x)
print("Inserting Kotka before Joensuu")
cities.insert(3,"Kotka")
print (cities)
print ()

#Using list.remove(x)
print("Removing Iisalmi from the list.")
cities.remove("Iisalmi")
print (cities)
print ()

#Using lis.pop([i])
remove = cities.pop(2)
print (remove,"removed from list.")
print ("Updated list of cities: ",cities)
print ()

#Using list.clear()
print ("Clearing the second list with cities.")
cities2.clear()
print ("List after clearing it: ",cities2)
print()

#Using list.index()
print ("Inserting Vantaa to the list the second time.")
cities.insert(5,"Vantaa")
print (cities)
print ("Returning the index of the first Vantaa.")
print (cities.index("Vantaa"))
print ("Returning the index of the second Vantaa.")
print (cities.index("Vantaa", 3))
print ()

#Using list.count(x)
print ("Vantaa appears",cities.count("Vantaa"),
       "times in the list and Espoo appears", cities.count("Espoo"), "in the list.")
print()

#Using list.sort()
print ("Sorting the list in an aplhabetical order.")
cities.sort()
print (cities)
print ()
print ("Sorting the list in a reverse order.")
cities.sort(reverse=True)
print (cities)
print ()

#Using list.reverse()
print ("Reversing the order of the list.")
cities.reverse()
print (cities)
print ()

#Using list.copy()
cities3 = cities.copy()
print ("Copied list of cities:", cities3)
print()

# 7 Creating a short dictionary
print ("Finnish to English dictionary: ")
dictionary = [["koira", "dog"], ["kissa", "cat"],["hevonen", "horse"],
              ["koti", "home"],["älypuhelin", "smartphone"], ["papukaija", "parrot"],
              ["koira", "dog"], ["kissa", "cat"]]
for i in range(len(dictionary)):
        print(dictionary[i][0]," - ",dictionary[i][1])
print ()

