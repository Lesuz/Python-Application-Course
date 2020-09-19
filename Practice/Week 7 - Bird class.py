# 3 Class Bird and migratory

class Bird():
    
    def __init__(self,name,eggs,country,month):
        self.name = name
        self.eggs = eggs
        self.country = country
        self.month = month

name = input("Give name: ")
eggs = 0
while eggs < 1 or eggs > 10:
    eggs = int(input("Give amount of eggs: "))

country = "a"
count = 2
while country[0].islower() or count < 5 or count > 20:
    country = input("Give name of the country: ")
    count = len(country)

month = 0
while month < 1 or month > 12:
    month = int(input("Give migratory month: "))
        