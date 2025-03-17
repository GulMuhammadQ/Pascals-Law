from tkinter import *

animation_Frame = Tk()
animation_Frame.geometry("700x400")

main_Canvas = Canvas(animation_Frame, width=700, height=400, bg="#999999")
main_Canvas.grid()

x2=100
x1=25

land_Fill = main_Canvas.create_rectangle(0, 225, 700, 400, fill="#873600")
land_Line = main_Canvas.create_line(0,225, 700, 225, fill="#008000", width=3)

base_Pipe_Coordinate = [(350, 300), (500, 300), (500, 200), (500+x2, 200), (500+x2, 325), (200-x1, 325), (200-x1, 200), (200, 200), (200, 300)]
base_Pipe = main_Canvas.create_polygon(base_Pipe_Coordinate, fill="#00AAFF", outline="#000000", width=3)
output_Plate = main_Canvas.create_rectangle(500-x2*0.3, 200, 500+x2*1.3, 225, fill="#222222", outline="#000000", width=3)
input_Plate_1 = main_Canvas.create_rectangle(200-x1, 200, 200, 210, fill="#222222", outline="#000000", width=3)
input_Plate_2 = main_Canvas.create_rectangle(200-x1, 175, 200, 180, fill="#222222", outline="#000000", width=3)
input_Plate_3 = main_Canvas.create_rectangle(200-x1*0.4, 180, 200-x1*0.6, 200, fill="#222222", outline="#000000", width=3)



animation_Frame.mainloop()