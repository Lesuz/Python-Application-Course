# Week 9-10 Mini Calculator
from tkinter import *
from tkinter import font as tkFont

class MiniCalculator:

    def __init__(self,parent):

        fontButton = tkFont.Font(family = 'Helvetica ',size = 15 ,weight = 'bold')
        fontText = tkFont.Font(family = 'Helvetica', size = 20, weight = 'bold')

        self.frame1 = Frame(parent)
        self.frame1.pack()

        self.resultTextBox = Text(self.frame1, width = 60,height = 3,font = fontText)
        self.resultTextBox.grid(row = 0, sticky = N)

        self.frame2 = Frame(parent)
        self.frame2.pack()

        self.Button7 = Button(self.frame2, width = 3,height = 3, text = "7",font = fontButton, bg = '#bfbfbf')
        self.Button7.grid(row = 1, column = 1, pady = 2, padx = 10)
        self.Button7.bind("<Button-1>", self.Button_7)

        self.Button8 = Button(self.frame2, width = 3,height = 3, text = "8",font = fontButton,bg = '#bfbfbf')
        self.Button8.grid(row = 1, column = 2, pady = 2, padx = 10)
        self.Button8.bind("<Button-1>", self.Button_8)

        self.Button9 = Button(self.frame2, width = 3,height = 3, text = "9",font = fontButton,bg = '#bfbfbf')
        self.Button9.grid(row = 1, column = 3, pady = 2, padx = 10)
        self.Button9.bind("<Button-1>", self.Button_9)

        self.ButtonAdd = Button(self.frame2, width = 3,height = 3, text = "+",font = fontButton,bg = '#8c8c8c')
        self.ButtonAdd.grid(row = 1, column = 4, pady = 2, padx = 10)
        self.ButtonAdd.bind("<Button-1>", self.Button_Add)

        self.Button4 = Button(self.frame2, width = 3,height = 3, text = "4",font = fontButton,bg = '#bfbfbf')
        self.Button4.grid(row = 2, column = 1, pady = 2, padx = 10)
        self.Button4.bind("<Button-1>", self.Button_4)

        self.Button5 = Button(self.frame2, width = 3,height = 3, text = "5",font = fontButton,bg = '#bfbfbf')
        self.Button5.grid(row = 2, column = 2, pady = 2, padx = 10)
        self.Button5.bind("<Button-1>", self.Button_5)

        self.Button6 = Button(self.frame2, width = 3,height = 3, text = "6",font = fontButton,bg = '#bfbfbf')
        self.Button6.grid(row = 2, column = 3, pady = 2, padx = 10)
        self.Button6.bind("<Button-1>", self.Button_6)

        self.ButtonMinus = Button(self.frame2, width = 3,height = 3, text = "-",font = fontButton,bg = '#8c8c8c')
        self.ButtonMinus.grid(row = 2, column = 4, pady = 2, padx = 10)
        self.ButtonMinus.bind("<Button-1>", self.Button_Minus)

        self.Button1 = Button(self.frame2, width = 3,height = 3, text = "1",font = fontButton,bg = '#bfbfbf')
        self.Button1.grid(row = 3, column = 1, pady = 2, padx = 10)
        self.Button1.bind("<Button-1>", self.Button_1)

        self.Button2 = Button(self.frame2, width = 3,height = 3, text = "2",font = fontButton,bg = '#bfbfbf')
        self.Button2.grid(row = 3, column = 2, pady = 2, padx = 10)
        self.Button2.bind("<Button-1>", self.Button_2)

        self.Button3 = Button(self.frame2, width = 3,height = 3, text = "3",font = fontButton,bg = '#bfbfbf')
        self.Button3.grid(row = 3, column = 3, pady = 2, padx = 10)
        self.Button3.bind("<Button-1>", self.Button_3)

        self.ButtonDivide = Button(self.frame2, width = 3,height = 3, text = "/",font = fontButton,bg = '#8c8c8c')
        self.ButtonDivide.grid(row = 3, column = 4, pady = 2, padx = 10)
        self.ButtonDivide.bind("<Button-1>", self.Button_Divide)
    
        self.ButtonClear = Button(self.frame2, width = 3,height = 3, text = "C",font = fontButton, bg = '#ff3333')
        self.ButtonClear.grid(row = 4, column = 1, pady = 2, padx = 10)
        self.ButtonClear.bind("<Button-1>", self.Button_Clear)

        self.Button0 = Button(self.frame2, width = 3,height = 3, text = "0",font = fontButton,bg = '#bfbfbf')
        self.Button0.grid(row = 4, column = 2, pady = 2, padx = 10)
        self.Button0.bind("<Button-1>", self.Button_0)

        self.ButtonSum = Button(self.frame2, width = 3,height = 3, text = "=",font = fontButton,bg = '#00cc66')
        self.ButtonSum.grid(row = 4, column = 3, pady = 2, padx = 10)
        self.ButtonSum.bind("<Button-1>", self.Button_Sum)

        self.ButtonTime = Button(self.frame2, width = 3,height = 3, text = "*",font = fontButton,bg = '#8c8c8c')
        self.ButtonTime.grid(row = 4, column = 4, pady = 2, padx = 10)
        self.ButtonTime.bind("<Button-1>", self.Button_Time)

    # Mehods that put the number into the text box
    def Button_Clear (self,event):
        self.resultTextBox.delete("1.0","end")
    
    def Button_0 (self,event):
        self.resultTextBox.insert(END,"0")

    def Button_1 (self,event):
        self.resultTextBox.insert(END,"1")

    def Button_2 (self,event):
        self.resultTextBox.insert(END,"2")

    def Button_3 (self,event):
        self.resultTextBox.insert(END,"3")

    def Button_4 (self,event):
        self.resultTextBox.insert(END,"4")

    def Button_5 (self,event):
        self.resultTextBox.insert(END,"5")
    
    def Button_6 (self,event):
        self.resultTextBox.insert(END,"6")
    
    def Button_7 (self,event):
        self.resultTextBox.insert(END,"7")

    def Button_8 (self,event):
        self.resultTextBox.insert(END,"8")

    def Button_9 (self,event):
        self.resultTextBox.insert(END,"9")
    
    def Button_Add(self,event):
        self.resultTextBox.insert(END,"+")
    
    def Button_Minus(self,event):
        self.resultTextBox.insert(END,"-")
    
    def Button_Divide(self,event):
        self.resultTextBox.insert(END, "/")
    
    def Button_Time(self,event):
        self.resultTextBox.insert(END,"*")

    # Calculates inputed math equation
    def Button_Sum(self,event):
        self.text = self.resultTextBox.get("1.0","end")
        self.resultTextBox.delete("1.0","end")
        self.result = eval(self.text)
        self.resultTextBox.insert(END,self.result)

root = Tk()
root.title("Mini Calculator")
root.geometry("270x500")
miniCalculator = MiniCalculator(root)
root.mainloop()
