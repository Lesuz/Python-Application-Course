# Week 9-10 : Kids math game

from tkinter import *
import random
import time
from threading import Event


class KidsMathGame:

    sleep_time = time.sleep(3)
    # Generating random numbers to put into numberLabels
    def newNumber1 (self):
        self.r1 = random.randint(1,50)
        return self.r1
        

    def newNumber2 (self):
        self.r2 = random.randint(1,50)
        return self.r2
        
    # A method that makes + or - randomly.
    def randomMark (self):
        list = ['+','-']
        self.r = random.choice(list)
        return self.r

    def __init__(self,parent):


        self.r1 = self.newNumber1()
        self.r2 = self.newNumber2()
        self.r = self.randomMark()

        self.frame1 = Frame(parent)
        self.frame1.pack()

        self.firstNumber = Label(self.frame1,text = str(self.r1), background="gray",width=5,height=2,font = 70)
        self.firstNumber.pack(side=LEFT)

        self.calculationMark = Label(self.frame1,text = str(self.r), font = 100)
        self.calculationMark.pack(side=LEFT)

        self.secondNumber = Label(self.frame1,background="gray",text= str(self.r2),width=5,height=2, font = 70)
        self.secondNumber.pack(side=LEFT)

        self.equals = Label(self.frame1,text="=")
        self.equals.pack(side=LEFT)

        self.inputAnswer = Entry(self.frame1)
        self.inputAnswer.pack(side=LEFT)

        self.submitButton = Button(self.frame1,text="SUBMIT")
        self.submitButton.pack(side=LEFT)

        self.submitButton.bind("<Button-1>", self.submit_click)

        self.frame2 = Frame(parent)
        self.frame2.pack()

    #Event handler for when SUBMIT -button is clicked
    #Checks if submited answer is correct or not
    def submit_click(self,event):
        print("Button clicked")
        
        self.answer = int(self.inputAnswer.get())
        # Full path for image given because could not get it working any other way
        if (self.r == "+"):
            if (self.r1 + self.r2 == self.answer):
                self.photo = PhotoImage(file = "c:/Users/lsusa/Tietojenkäsittely/Python Application/right.gif")
                self.picture = Label(self.frame2, image = self.photo)
                self.picture.pack(side=LEFT)
            else:
                self.photo = PhotoImage(file = "c:/Users/lsusa/Tietojenkäsittely/Python Application/fail.gif")
                self.picture = Label(self.frame2, image = self.photo)
                self.picture.pack(side=LEFT)
        else:
            if (self.r1 - self.r2 == self.answer):
                self.photo = PhotoImage(file = "c:/Users/lsusa/Tietojenkäsittely/Python Application/right.gif")
                self.picture = Label(self.frame2, image = self.photo)
                self.picture.pack(side=LEFT)
            else:
                self.photo = PhotoImage(file = "c:/Users/lsusa/Tietojenkäsittely/Python Application/fail.gif")
                self.picture = Label(self.frame2, image = self.photo)
                self.picture.pack(side=LEFT)
        
        
        self.picture.after(2000,self.destroyPic)
        # Clearing entry widget and updating new values into labels
        self.inputAnswer.delete(0, 'end')
        self.firstNumber.config(text = str(self.newNumber1()))
        self.secondNumber.config(text = str(self.newNumber2()))
        self.calculationMark.config(text = str(self.randomMark()))

    def destroyPic(self):
        self.picture.destroy()   


root = Tk()
root.title("Kids Math Game")
kidsmathapp = KidsMathGame(root)
root.mainloop()