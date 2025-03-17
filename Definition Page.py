from tkinter import *

## Page initialize
def __init__(self, parent, controller):

    ## Frame initialize
    Frame.__init__(self, parent)
    
    # Title label
    title=Label(self, text="Pascal's Principle", font=("Helvetica", 16, "bold"))
    title.pack(pady=10)

    # Explanation text
    explanation_Text = """Pascal's Principle, states that a change in pressure at any point in an enclosed fluid at rest is transmitted without loss to all points
in the fluid. This principle forms the basis for many engineering applications, particularly in hydraulics.

One of the most common applications of Pascal's Principle is in hydraulic systems, where a small force applied to a
small area is converted into a larger force on a larger area by means of an enclosed fluid. This allows for the
amplification of force, enabling the operation of heavy machinery, lifts, and brakes. """

    explanation_Label=Label(self, text=explanation_Text, wraplength=500, justify="left")
    explanation_Label.pack(pady=10, padx=10)

    # Change page button
    close_Button=Button(self, text="Back to Main Menu", command=lambda:controller.show_Frame(Main_Menu))
    close_Button.pack(pady=10)