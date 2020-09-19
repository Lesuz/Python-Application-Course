# Week 11-12 Topic: Files 1, reading a file and adding information to it.

from tkinter import *

class Countries:

    filename = "c:/Users/lsusa/Tietojenkäsittely/Python Application/countries.txt"


    def __init__(self,parent):

        self.line = ""
        self.biggestCountry = ""

        self.frame = Frame(parent)
        self.frame.grid()

        self.ListName = Label(text = "Countries and their population:")
        self.ListName.grid(column = 1, sticky = "n", pady = 10)

        self.countryList = Text(width = 30, height = 17)
        self.countryList.grid(row = 1, column = 1,rowspan = 6, pady = 30, padx = 10)

        with open(self.filename, 'r+') as self.f:
            self.countryList.insert(END,self.f.read())   

        self.searchBar = Entry(width = 35)
        self.searchBar.grid(row = 1, column = 2, pady = 2, padx = 5)

        self.searchButton = Button(text = "Search")
        self.searchButton.grid(row = 1, column = 2, sticky = "e")
        self.searchButton.bind("<Button-1>", self.searchingButton)

        self.outprintresult = Label( text = self.line)
        self.outprintresult.grid(row = 2, column = 2)

        self.addNameLabel = Label(text = "Name of country:")
        self.addNameLabel.grid(row = 3, column = 2, sticky = "n")

        self.addingNameBar = Entry(width = 35)
        self.addingNameBar.grid(row = 3, column = 2)

        self.addPopulationLabel = Label(text = "Population of country:")
        self.addPopulationLabel.grid(row = 4, column = 2, sticky = "n")

        self.addingPopulationBar = Entry(width = 35)
        self.addingPopulationBar.grid(row = 4, column = 2)

        self.addingButton = Button(text = " Add  ")
        self.addingButton.grid(row = 5, column = 2, sticky = "e")
        self.addingButton.bind("<Button-1>", self.addButton)

        self.mostPopulationTitle = Label(text = "Country with biggest population:")
        self.mostPopulationTitle.grid(row = 6, column = 2, sticky = "n")

        self.findLargestPopulation()

        self.mostPopulation = Label(width = 45, text = self.biggestCountry)
        self.mostPopulation.grid(row = 6, column = 2)
    
    def addButton (self, event):
        self.nameText = self.addingNameBar.get()
        self.populationText = self.addingPopulationBar.get().replace(' ', '')
        with open(self.filename, "a") as self.f:
            self.f.write(self.nameText)
            self.f.write("\n")
            self.f.write(self.populationText)
            self.f.write("\n")
        self.countryList.delete('1.0', END)
        with open(self.filename, 'r+') as self.f:
            self.countryList.insert(END,self.f.read())  
        self.findLargestPopulation()
        self.mostPopulation.config(text = self.biggestCountry)

    def searchingButton(self, event):
        self.outprintresult.config(text = "")
        self.inputtedText = str(self.searchBar.get()) + "\n"
        # Reading file line by line until searched country found
        with open(self.filename, "r") as self.f:
            while True:
                self.line = self.f.readline()

                if not self.line:
                    break

                if self.line == self.inputtedText:
                    self.line = self.f.readline()
                    self.outprintresult.config(text = self.line)
                else:
                    self.line = self.f.readline()

    def findLargestPopulation(self):
        self.biggestPopulation = 0
        self.population = 0
        self.country = ""
        with open(self.filename, "r") as self.f:
            self.biggestCountry = self.f.readline()
            self.biggestPopulation = int(self.f.readline())

            while True:
                self.country = self.f.readline()
                if self.country == '':
                    break
                self.populationstring = self.f.readline().rstrip('\n')
                self.population = int(self.populationstring)
                #if not self.population:
                #    break
                if self.population > self.biggestPopulation:
                    self.biggestPopulation = self.population
                    self.biggestCountry = self.country


        
        



        
        

root = Tk()
root.title("File reader")    
root.geometry("600x350")
countries = Countries(root)
root.mainloop()