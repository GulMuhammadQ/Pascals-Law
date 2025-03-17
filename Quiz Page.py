from tkinter import *

## Building main menu frame
def __init__(self, parent, controller):

    self.user_Answer=[IntVar() for _ in range(8)]
    
    ## Frame Initialize
    Frame.__init__(self, parent)

    ## Main label
    title=Label(self, text="QUIZ SECTION", font=("Lato", 14, 'bold'))
    title.pack()
    question_One=Label(self, text="1) Who is Pascal's law named after?", font=("Lato", 10))
    question_One_Radio_Button_One=Radiobutton(self, text="Pedro Pascal", font=("Lato", 10), variable=self.user_Answer[0], value=0)
    question_One_Radio_Button_Two = Radiobutton(self, text="Blaise Pascal", font=("Lato", 10), variable=self.user_Answer[0], value=1)
    question_Two=Label(self, text="2) What is the formula for pressure?", font=("Lato", 10))
    question_Two_Radio_Button_One= Radiobutton(self, text="P=F/A", font=("Lato", 10), variable=self.user_Answer[1], value=0)
    question_Two_Radio_Button_Two = Radiobutton(self, text="P=IV", font=("Lato", 10), variable=self.user_Answer[1], value=1)
    question_Three=Label(self, text="3) What is Pascal's law?", font=("Lato", 10))
    question_Three_Radio_Button_One=Radiobutton(self, text="Fluid pressure is inversely proportional to the volume of the container", font=("Lato", 10), variable=self.user_Answer[2], value=0)
    question_Three_Radio_Button_Two=Radiobutton(self, text="Pressure applied to a fluid is transmitted undiminished in every direction", font=("Lato", 10), variable=self.user_Answer[2], value=1)
    question_Four=Label(self, text="4) Which of the following is an application of Pascal's law?", font=("Lato", 10))
    question_Four_Radio_Button_One=Radiobutton(self, text="Hydraulic lift", font=("Lato", 10), variable=self.user_Answer[3], value=0)
    question_Four_Radio_Button_Two=Radiobutton(self, text="Air pressure in a bicycle tire", font=("Lato", 10), variable=self.user_Answer[3], value=1)
    question_Five=Label(self, text="5) In a hydraulic system based on Pascal's law, if a small force is applied to a small piston, how does the output force compare when exerted by a larger piston?", font=("Lato", 10))
    question_Five_Radio_Button_One=Radiobutton(self, text="Output force is equal", font=("Lato", 10), variable=self.user_Answer[4], value=0)
    question_Five_Radio_Button_Two=Radiobutton(self, text="Output force is larger", font=("Lato", 10), variable=self.user_Answer[4], value=1)
    question_Six=Label(self, text="6) Which of the following is not a requirement for Pascal's law to hold true?", font=("Lato", 10))
    question_Six_Radio_Button_One=Radiobutton(self, text="The pressure must be applied uniformly", font=("Lato", 10), variable=self.user_Answer[5], value=0)
    question_Six_Radio_Button_Two=Radiobutton(self, text="The fluid must be at rest", font=("Lato", 10), variable=self.user_Answer[5], value=1)
    question_Seven=Label(self, text="7) What is the SI unit of pressure, often used to measure the effects described by Pascal's law?", font=("Lato", 10))
    question_Seven_Radio_Button_One=Radiobutton(self, text="Pascal(Pa)", font=("Lato", 10), variable=self.user_Answer[6], value=0)
    question_Seven_Radio_Button_Two=Radiobutton(self, text="Newton(N)", font=("Lato", 10), variable=self.user_Answer[6], value=1)
    question_Eight=Label(self, text="8) Which of the following statements best describes how Pascal's law applies to a hydraulic brake system in a car?", font=("Lato", 10))
    question_Eight_Radio_Button_One = Radiobutton(self, text=" A small force on the brake pedal generates a large force on the brake pads", font=("Lato", 10), variable=self.user_Answer[7], value=0)
    question_Eight_Radio_Button_Two = Radiobutton(self, text="The brake fluid increases in volume when the brakes are applied", font=("Lato", 10), variable=self.user_Answer[7], value=1)
    
    ## Label and radio packing
    question_One.grid(row=1, column=1, columnspan=2)
    question_One_Radio_Button_One.grid(row=2, column=1)
    question_One_Radio_Button_Two.grid(row=2, column=2)
    question_Two.grid(row=3, column=1, columnspan=2)
    question_Two_Radio_Button_One.grid(row=4, column=1)
    question_Two_Radio_Button_Two.grid(row=4, column=2)
    question_Three.grid(row=5, column=1, columnspan=2)
    question_Three_Radio_Button_One.grid(row=6, column=1)
    question_Three_Radio_Button_Two.grid(row=6, column=2)
    question_Four.grid(row=7, column=1, columnspan=2)
    question_Four_Radio_Button_One.grid(row=8, column=1)
    question_Four_Radio_Button_Two.grid(row=8, column=2)
    question_Five.grid(row=1, column=3, columnspan=2)
    question_Five_Radio_Button_One.grid(row=2, column=3)
    question_Five_Radio_Button_Two.grid(row=2, column=4)
    question_Six.grid(row=3, column=3, columnspan=2)
    question_Six_Radio_Button_One.grid(row=4, column=3)
    question_Six_Radio_Button_Two.grid(row=4, column=4)
    question_Seven.grid(row=5, column=3, columnspan=2)
    question_Seven_Radio_Button_One.grid(row=6, column=3)
    question_Seven_Radio_Button_Two.grid(row=6, column=4)
    question_Eight.grid(row=7, column=3, columnspan=2)
    question_Eight_Radio_Button_One.grid(row=8, column=3)
    question_Eight_Radio_Button_Two.grid(row=8, column=4)

    ## Checking button
    check_button = Button(self, text="Check Answers", font=("Lato", 10, 'bold'), command=lambda:self.check_Answer(quiz_Result, home_Button))
    check_button.pack()
    quiz_Result=Label(self, font=("Lato", 10, 'bold'), text="score will appear here")
    quiz_Result.pack()
    home_Button=Button(self, text="Back to Main Menu", font=("Lato", 10, 'bold'), command=lambda:controller.show_Frame(Main_Menu))

## Answer checking function
def check_Answer(self, quiz_Result, home_Button):

    ## Correct answer initialize and checking
    correct_Answer=[1, 0, 1, 0, 1, 1, 0, 0]
    correct_Answer_Count=0
    for i in range(8):
        if self.user_Answer[i].get()==correct_Answer[i]:
            correct_Answer_Count+=1

    ## Quiz result output
    quiz_Result.config(text=f'Correctly answered questions: '+str(correct_Answer_Count)+'/8', font=("Lato", 10, 'bold'))
    home_Button.pack()
