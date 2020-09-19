# Week 8 Author - Book association

class Author():

    def __init__ (self,Fname,Sname,DofB):
        self.Fname = Fname
        self.Sname = Sname
        self.DofB = DofB
    
    def getFname(self):
        return self.Fname

    def getSname(self):
        return self.Sname
    
    def getDofB(self):
        return self.DofB

    
class Book():

    def __init__(self,Title,Author,Pages,Publisher):
        self.title = Title
        self.author = Author
        self.pages = Pages
        self.publisher = Publisher

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getPages(self):
        return self.pages

    def getPublisher(self):
        return self.publisher

    
Fname = input("First name of the author: ")
Sname = input("Last name of the author: ")
DofB = input("Give date of birth of author(DD.MM.YYYY): ")

myAuthor = Author(Fname,Sname,DofB)

Title = input("Title of the book: ")
Pages = int(input("How many pages does the book have: "))
Publisher = input("Publisher: ")

myBook = Book(Title,myAuthor,Pages,Publisher)

print ()
print ("Book: " + str(myBook.getTitle()) +"\nAuthor: " + str(myBook.getAuthor().getSname()) + " " + str(myBook.getAuthor().getFname()) + "\nPages: " + str(myBook.getPages()) + "\nPublisher: " + str(myBook.getPublisher()))



    


