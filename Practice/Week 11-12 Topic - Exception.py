# Week 11-12 Topic - Exception

#class ZeroYearImpossible(Exception):
#    pass


class TryException:


    #def __init__(self):
    try:
        x = int(input("Enter a year: "))
        print ("Year : " + str(x))

        #if self.x == 0:
        #    raise ZeroYearImpossible
    except ValueError:
        print ("You must enter an integer!")
    except KeyboardInterrupt:
        print("Running of code interrupted by ctrl + c")
    except:
        print("Unexcepted error! Try again!")
        #except ZeroYearImpossible:
        #    print ("Year 0 not possible.")


