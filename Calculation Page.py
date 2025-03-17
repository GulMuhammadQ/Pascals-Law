from tkinter import *

def __init__(self, parent, controller):

    ## Variable Initialize
    self.input_Force=IntVar()
    self.input_Surface_Area=IntVar()
    self.output_Surface_Area=IntVar()

    ## Frame Initialize 
    Frame.__init__(self, parent)
    
    ## Different Section Frame Building
    animation_Frame=Frame(self, width=700, height=400)
    input_Frame=Frame(self, width=250, height=600)
    describe_Frame=Frame(self, width=700, height=100, background='#f9cb9c')

    animation_Frame.grid(column=0, row=0, sticky='nesw', pady=50, padx=50)
    input_Frame.grid(column=1, row=0, sticky='nesw', pady=50, rowspan=2)
    describe_Frame.grid(column=0, row=1, sticky='new', padx=50)

    ## Section Frame Configure
    input_Frame.grid_propagate(False)
    describe_Frame.grid_propagate(False)


    ## Input Frame Building
    input_Frame_Title=Label(input_Frame, text='Hydraulic Lift Adjuster', font=("Lato", 20, 'bold'), relief="sunken", border=4, wraplength=200)

    input_Force_1=Label(input_Frame, text='Input Force, F     ( Newton, N )', font=("Lato", 12))
    input_Force_2=Label(input_Frame, text='1', font=("Lato", 9))
    input_Force_Scale=Scale(input_Frame, variable=self.input_Force, orient=HORIZONTAL, from_=10, to=500, resolution=10)
    
    input_Surface_Area_1=Label(input_Frame, text='Input Surface Area, A', font=("Lato", 12))
    input_Surface_Area_2=Label(input_Frame, text='1', font=("Lato", 9))
    input_Surface_Area_3=Label(input_Frame, text='( Meter Square , m^2 )', font=("Lato", 12))
    input_Surface_Area_Scale=Scale(input_Frame, variable=self.input_Surface_Area, orient=HORIZONTAL, from_=1, to=50, resolution=1)
    
    output_Surface_Area_1=Label(input_Frame, text='Output Surface Area, A', font=("Lato", 12))
    output_Surface_Area_2=Label(input_Frame, text='2', font=("Lato", 9))
    output_Surface_Area_3=Label(input_Frame, text='( Meter Square , m^2 )', font=("Lato", 12))
    output_Surface_Area_Scale=Scale(input_Frame, variable=self.output_Surface_Area, orient=HORIZONTAL, from_=50, to=500, resolution=10)

    calculate_Button=Button(input_Frame, text="Press Me to Calculate!!", font=("Lato", 10, 'bold'), command=lambda:self.calculate_Page(calculate_Button))


    ## Input Frame Packing
    input_Frame_Title.grid(column=0, row=0, ipady=5, ipadx=5, sticky='nesw', pady=50)

    input_Force_1.grid(column=0, row=1, sticky='w')
    input_Force_2.place(x=97, y=189)
    input_Force_Scale.grid(column=0, row=3, sticky='nesw')

    input_Surface_Area_1.grid(column=0, row=4, sticky='w', pady=(30, 0))
    input_Surface_Area_2.place(x=151, y=285)
    input_Surface_Area_3.grid(column=0, row=5, sticky='w')
    input_Surface_Area_Scale.grid(column=0, row=6, sticky='nesw')

    output_Surface_Area_1.grid(column=0, row=7, sticky='w', pady=(30, 0))
    output_Surface_Area_2.place(x=163, y=404)
    output_Surface_Area_3.grid(column=0, row=8, sticky='w')
    output_Surface_Area_Scale.grid(column=0, row=9, sticky='nesw')

    calculate_Button.grid(column=0, row=10, pady=50)


    ## Animation Section
    exec(open("Calculation Page Animation.py").read())



    ## Describe Section Building


    ## Back button (Temp)
    mainButton=Button(self, text="Back to Main Menu", command=lambda:controller.show_Frame(Main_Menu))
    mainButton.grid(column=0, row=1)




## Calculation Function ( Popup Result )
def calculate_Page(self, button):

    ## Popup Window and Frame Building
    result_Popup_Window=Toplevel(self, )
    result_Popup_Window.title('Result')
    result_Popup_Window.resizable(0, 0)
    result_Frame=Frame(result_Popup_Window, width=800, height=400)
    result_Frame.grid_propagate(False)
    result_Frame.columnconfigure(0, weight=3)
    result_Frame.columnconfigure(1, weight=1)
    result_Frame.columnconfigure(2, weight=3)
    result_Frame.columnconfigure(3, weight=1)
    result_Frame.pack(fill='both', padx=20)

    button['state']=DISABLED
    result_Popup_Window.protocol("WM_DELETE_WINDOW", lambda:self.reset_Calculate_Button(button, result_Popup_Window))

    ## Other Result Calculation
    self.output_Force=self.input_Force.get()/self.input_Surface_Area.get()*self.output_Surface_Area.get()
    self.pressure=self.input_Force.get()/self.input_Surface_Area.get()
    self.force_Ratio=self.output_Force/self.input_Force.get()

    ## Popup Window Content Building
    result_Title=Label(result_Frame, text="Results", font=("Lato", 24, 'bold', 'underline'))
    result_Input_Force_1=Label(result_Frame, text="Input Force, F", font=("Lato", 14))
    result_Input_Force_2=Label(result_Frame, text="1", font=("Lato", 10))
    result_Input_Force_Answer=Label(result_Frame, text=str(self.input_Force.get())+" N", font=("Lato", 14))
    result_Input_Surface_Area_1=Label(result_Frame, text="Input Surface Area, A", font=("Lato", 14))
    result_Input_Surface_Area_2=Label(result_Frame, text="1", font=("Lato", 10))
    result_Input_Surface_Area_Answer=Label(result_Frame, text=str(self.input_Surface_Area.get())+" m^2", font=("Lato", 14))
    result_Pressure=Label(result_Frame, text='Pressure, P', font=("Lato", 14))
    result_Pressure_Answer=Label(result_Frame, text=str(int(self.pressure))+" Pa", font=("Lato", 14))
    result_Output_Force_1=Label(result_Frame, text="Output Force, F", font=("Lato", 14))
    result_Output_Force_2=Label(result_Frame, text="2", font=("Lato", 10))
    result_Output_Force_Answer=Label(result_Frame, text=str(int(self.output_Force))+" N", font=("Lato", 14))
    result_Output_Surface_Area_1=Label(result_Frame, text="Output Surface Area, A", font=("Lato", 14))
    result_Output_Surface_Area_2=Label(result_Frame, text="2", font=("Lato", 10))
    result_Output_Surface_Area_Answer=Label(result_Frame, text=str(self.output_Surface_Area.get())+" m^2", font=("Lato", 14))
    result_Force_Ratio_1=Label(result_Frame, text='Ratio, F   : F', font=("Lato", 14))
    result_Force_Ratio_2=Label(result_Frame, text="1", font=("Lato", 10))
    result_Force_Ratio_3=Label(result_Frame, text="2", font=("Lato", 10))
    result_Force_Ratio_Answer=Label(result_Frame, text="1 : "+str(int(self.force_Ratio)), font=("Lato", 14))
    
    ## Popup Window Content Packing
    result_Title.grid(column=0, row=0, padx=40, pady=40, sticky='w')
    result_Input_Force_1.grid(column=0, row=1, padx=(40, 0), pady=10, sticky='w')
    result_Input_Force_2.place(x=152, y=137)
    result_Input_Force_Answer.grid(column=1, row=1, padx=(0, 50), sticky='e')
    result_Input_Surface_Area_1.grid(column=0, row=2, padx=(40, 0), pady=10, sticky='w')
    result_Input_Surface_Area_2.place(x=207, y=185)
    result_Input_Surface_Area_Answer.grid(column=1, row=2, padx=(0, 50), sticky='e')
    result_Pressure.grid(column=0, row=3, padx=(40, 0), pady=10, sticky='w')
    result_Pressure_Answer.grid(column=1, row=3, padx=(0, 50), sticky='e') 
    result_Output_Force_1.grid(column=2, row=1, sticky='w')
    result_Output_Force_2.place(x=537, y=137)
    result_Output_Force_Answer.grid(column=3, row=1, padx=(0, 50), sticky='e')
    result_Output_Surface_Area_1.grid(column=2, row=2, pady=10, sticky='w')
    result_Output_Surface_Area_2.place(x=592, y=185)
    result_Output_Surface_Area_Answer.grid(column=3, row=2, padx=(0, 50), sticky='e')
    result_Force_Ratio_1.grid(column=2, row=3, pady=10, sticky='w')
    result_Force_Ratio_2.place(x=477, y=232)
    result_Force_Ratio_3.place(x=512, y=232)
    result_Force_Ratio_Answer.grid(column=3, row=3, padx=(0, 50), sticky='e')
    

## Animation Function by Using Canvas
def animation_Part(self):
    print("heh")


## Window Close Detect ( Avoid Spamming Result )
def reset_Calculate_Button(self, button, result_Popup_Window):
    button['state']=ACTIVE
    result_Popup_Window.destroy()
