from tkinter import *

## Page initialize
def __init__(self, parent, controller):

    ## Frame initilize
    Frame.__init__(self, parent)

    Label(self, text="Temporary Main Menu", font=("Lato", 20, 'bold')).pack()
    temporary_Button_Definition=Button(self, text="Temporary Definition Page", command=lambda:controller.show_Frame(Definition_Page)).pack()
    temporary_Button_Quiz=Button(self, text="Temporary Quiz Page", command=lambda:controller.show_Frame(Quiz_Page)).pack()
    temporary_Button_Calculation=Button(self, text="Temporary Calculation Page", command=lambda:controller.show_Frame(Calculation_Page)).pack()
