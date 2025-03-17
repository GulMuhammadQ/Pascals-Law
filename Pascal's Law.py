from tkinter import *

## Building main application class 
class MainApplication(Tk):

    ## Initial function for building window
    def __init__(self, *args, **kwargs):

        ## Starting Tk Window
        Tk.__init__(self, *args, **kwargs)
        self.resizable(0, 0)
        self.title("'' The Pascal's Law ''")
        self.geometry("1100x700")

        ## Building a cointainer to store all pages
        theMainContainer=Frame(self)
        theMainContainer.pack(side="top", fill="both", expand=True)

        ## A dictionary to store all frame
        self.allFrames={}
        for frameName in (Main_Menu, Definition_Page, Quiz_Page, Calculation_Page):
            frame=frameName(theMainContainer, self)
            self.allFrames[frameName]=frame
            frame.grid(row=0, column=0, sticky="nsew")

        ## Bring up the first page and starting the window
        self.show_Frame(Calculation_Page)
        self.mainloop()


    ## Function for showing the specific window
    def show_Frame(self, frameName):
        frameNow=self.allFrames[frameName]
        frameNow.tkraise()



## Class for Main Menu
class Main_Menu(Frame):
    exec(open("C:\Users\User\Documents\CSFY-1A-Group-Coding-main\Main menu.py").read())


        
## Class for Quiz page
class Quiz_Page(Frame):
    exec(open("C:\Users\User\Documents\CSFY-1A-Group-Coding-main\Quiz Page.py").read())



## The definition page
class Definition_Page(Frame):
    exec(open("C:\Users\User\Documents\CSFY-1A-Group-Coding-main\Definition Page.py").read())
        


## Class for Calculation Page
class Calculation_Page(Frame):
    exec(open("C:\Users\User\Documents\CSFY-1A-Group-Coding-main\Calculation Page.py").read())



MainApplication()
