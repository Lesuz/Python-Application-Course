# Week 11-12 Topic - Testing and debugging - BMI calculator
from tkinter import *
from tkinter import font as tkFont

class BMI:

    def __init__(self, parent):

        fontText = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')

        self.BMIanswer = ""
        self.BMIdescript = ""

        self.frame = Frame(parent)
        self.frame.grid()

        self.weightLabel = Label(text = "Weight in kg:")
        self.weightLabel.grid(row = 1, column = 1, sticky = "w", pady = 5)

        self.weightEntry = Entry()
        self.weightEntry.grid(row = 2, column = 1)

        self.heightLabel = Label(text = "Height in cm:")
        self.heightLabel.grid(row = 3, column = 1, sticky = "w", pady = 5)

        self.heightEntry = Entry()
        self.heightEntry.grid(row = 4, column = 1)

        self.Button = Button(text = "Calculate")
        self.Button.grid(row = 5, column = 1, pady = 5)
        self.Button.bind("<Button-1>", self.buttonClick)

        self.BMIresult = Label(text = str(self.BMIanswer), font = fontText)
        self.BMIresult.grid(row = 1, column = 2, rowspan = 5, padx = 40)

        self.BMIdescription = Label(text = self.BMIdescript)
        self.BMIdescription.grid(row = 2, column = 2)


    def BMICalculate(self):
        self.weightstr = self.weightEntry.get()
        self.heightstr = self.heightEntry.get()
        self.weight = float(self.weightstr)
        self.height = float(self.heightstr)
        if self.height <= 0 or self.weight <= 0:
            # self.BMIresult.config("Not possible, try again")
            return 0
        else:
            self.BMIanswer = self.weight / ((self.height / 100) * (self.height / 100))
            return self.BMIanswer

    def buttonClick (self, event):
        fontT = tkFont.Font(family = 'Helvetica', size = 10, weight = 'bold')
        self.realBMIAnswer = self.BMICalculate()
        if self.realBMIAnswer == 0:
            self.BMIresult.config(text = 'Try again!', font = fontT)
        else:
            self.BMIresult.config(text = '{:.1f}'.format((self.realBMIAnswer)))
            if self.realBMIAnswer < 18.5:
                self.BMIdescription.config(text = "Underweight")
            elif self.realBMIAnswer >= 18.5 and self.realBMIAnswer <= 24.9:
                self.BMIdescription.config(text = "Healthy weight")
            elif self.realBMIAnswer >= 25 and self.realBMIAnswer <= 29.9:
                self.BMIdescription.config(text = "Overweight")
            elif self.realBMIAnswer >= 30:
                self.BMIdescription.config(text = "Obese")
            else:
                self.BMIdescription.config(text = "BMI not realistic")



root = Tk()
root.title("BMI Calculator")
root.geometry("270x150")
calculator = BMI(root)
root.mainloop()