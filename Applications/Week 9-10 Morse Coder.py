#Week 9-10 Morse Coder

from tkinter import *

class MorseCoder:

    morseCode = {'A':'.-',
                'B':'-...',
                'C':'-.-.',
                'D':'-..',
                'E':'.',
                'F':'..-.',
                'G':'--.',
                'H':'....',
                'I':'..',
                'J':'.---',
                'K':'-.-',
                'L':'.-..',
                'M':'--',
                'N':'-.',
                'O':'---',
                'P':'.--.',
                'Q':'--.-',
                'R':'.-.',
                'S':'...',
                'T':'-',
                'U':'..-',
                'V':'...-',
                'W':'.--',
                'X':'-..-',
                'Y':'-.--',
                'Z':'--..',
                '1':'.----',
                '2':'..---',
                '3':'...--',
                '4':'....-',
                '5':'.....',
                '6':'-....',
                '7':'--...',
                '8':'---..',
                '9':'----.',
                '0':'-----',
                ' ': ' '}
    morse = ''
    
    #Converts text to morse code
    #textToMorse = {v: k for k,v in morseCode.items()}
        

    def __init__(self,parent):
        self.frame1 = Frame(parent)
        self.frame1.pack()

        self.inputTextLabel = Label(self.frame1,text="Input Text: ")
        self.inputTextLabel.pack(side=TOP)

        self.inputText = Text(self.frame1,width=50,height=10)
        self.inputText.pack(side=LEFT)

        self.frame2 = Frame(parent)
        self.frame2.pack()

        self.submitButton = Button(self.frame2,text="Text into morse code")
        self.submitButton.pack(side=BOTTOM)

        self.submitButton.bind("<Button-1>", self.submit_click)

        self.outputTextLabel = Label(self.frame2,text="Morse Code: ")
        self.outputTextLabel.pack(side=TOP)

        self.outputText = Text(self.frame2,width=50,height=10)
        self.outputText.pack(side=LEFT)
    

    def morserer(self):
        for x in self.textUpper:
            self.morse += str(self.morseCode.get(x)) + ' '

    def clearOutput(self):
        self.morse = ''
        self.outputText.delete("1.0","end")

    #Event handler for when SUBMIT -button is clicked
    # GEts inputed text and Turns users text into morse code
    def submit_click(self,event):
        print("Button clicked")
        self.clearOutput()
        self.text = self.inputText.get("1.0","end-1c")
        self.textUpper = self.text.upper()
        #for x in self.textUpper:
        #    self.morse += str(self.morseCode.get(x)) + ' '
        self.morserer()
        self.outputText.insert(END,self.morse)
    
    
        

root = Tk()
root.title("Morse Coder")
root.geometry("500x450")
morsecoder = MorseCoder(root)
root.mainloop()