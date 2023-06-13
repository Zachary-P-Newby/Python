# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing, draw_vertical_gradient
from random import randint


def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    draw_sky(canvas)
    draw_random_clouds(canvas)
    draw_ground(canvas)
    draw_random_rocks(canvas)
    draw_tree_1(canvas)
    draw_tree_2(canvas)
    draw_rocks(canvas)
    draw_bird(canvas)
    
    for num in range(0,randint(0,5)):
        draw_flower(canvas, randint(20, 780),randint(10,150))
    
    
    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Define your functions such as
# draw_sky and draw_ground here.
def draw_sky(canvas):
    draw_vertical_gradient(canvas, x0 = 0, y0 =200, x1 =800, y1 = 500, color0= [128,191,255], color1= [25,140,255])

    
def draw_ground(canvas):
    draw_vertical_gradient(canvas, x0 = 0, y0 =0, x1 =800, y1 = 200, color0= (25,194,81), color1=(33,255,107))

def draw_tree_1(canvas):
    draw_rectangle(canvas, 175, 150, 225, 400, fill="sienna4", width=0)
    draw_oval(canvas, 50, 305, 350, 450, fill="green4", width = 0)
    draw_oval(canvas, 200, 280, 400, 380, fill="green", width = 0)
    draw_polygon(canvas, 125, 151, 175, 151, 175, 160, fill="sienna4", outline = 'sienna4', width= 0)
    draw_polygon(canvas, 225, 151, 240, 151, 225, 160, fill="sienna4", outline = 'sienna4', width= 0)
    draw_polygon(canvas, 200, 145, 210, 145, 205, 155, fill="tan4",  outline ="tan4", width= 2)

def draw_tree_2(canvas):
    draw_rectangle(canvas, 645, 75, 685, 350, fill="saddleBrown", width=0)
    draw_oval(canvas, 600, 250, 730, 400, fill="forestgreen", width = 0)
    draw_oval(canvas, 550, 240, 680, 340, fill="green4", width = 0)
    draw_oval(canvas, 650, 240, 780, 340, fill="green", width = 0)
    draw_oval(canvas, 600, 200, 780, 300, fill="darkGreen", width = 0)
    draw_polygon(canvas, 636, 75, 645, 75, 645, 160, fill="saddleBrown", outline = 'saddleBrown', width= 0)

def draw_rocks(canvas):
    draw_polygon(canvas, 234, 34, 254, 34, 238, 45, fill="ivory4", outline = 'ivory4', width= 0)
    draw_oval(canvas, 35, 47, 46, 52, fill="gray67", outline= "gray67")

def draw_random_rocks(canvas):
    for num in range(1, randint(0,12)):
        x = randint(0, 770)
        y = randint(0, 190)
        draw_oval(canvas, x, y, x + randint(5, 30), y + randint(5, 15),fill="gray54", outline= "gray54")

def draw_random_clouds(canvas):
    
    for num in range(0, randint(0,6)):
        xa = randint(10,790)
        ya = randint(300,490)
        xb = xa + randint(10,200)
        yb = ya + randint(10,75)
        
        draw_oval(canvas, xa, ya, xb, yb, fill="mintCream", outline= "mintCream")

def draw_bird(canvas):
    #legs
    draw_line(canvas = canvas, x0=517, y0=95, x1=514, y1=78, fill= "gray9")
    draw_line(canvas = canvas, x0=514, y0=78, x1=519, y1=78, fill= "gray9")

    draw_line(canvas = canvas, x0=522, y0=95, x1=519, y1=80, fill= "gray9")
    draw_line(canvas = canvas, x0=519, y0=80, x1=524, y1=80, fill= "gray9")
    #body
    draw_oval(canvas, x0= 510, y0 = 90, x1= 540, y1 = 110, width = 1, outline= "brown2", fill="brown2")
    #head
    draw_oval(canvas, x0= 530, y0 = 100, x1= 548, y1 = 118, width = 1, outline= "brown2", fill="brown2")
    #tail
    draw_polygon(canvas, x0=495, y0=110, x1=508, y1= 115, x2=515, y2=95, fill="coral4", outline="coral4")
    #eye
    draw_oval(canvas, x0= 540, y0 = 110, x1= 541, y1 = 115, width = 5, outline= "gray5", fill="gray5")
    #wing
    draw_oval(canvas, x0= 505, y0 = 88, x1= 530, y1 = 105, fill= "brown4", outline= "brown4", width=2)
    #beak
    draw_polygon(canvas, x0= 547.5, y0 = 105, x1 = 547.5, y1=115, x2= 560, y2= 110, fill="orange", outline="orange")

def draw_flower(canvas, xa, ya):
    #stem
    draw_arc(canvas, x0=xa-3, y0=ya-29, x1=xa+7, y1=ya+1, outline="forestGreen", fill="forestGreen", width=3, start=270, extent=-180)
    draw_oval(canvas, x0 = xa-3, y0 = ya - 9, x1= xa - 15, y1 = ya - 14, outline="forestGreen", fill="forestGreen")
    #petals
    draw_oval(canvas, x0=xa, y0=ya, x1=xa -10, y1=ya + 10, fill='violetRed1', outline="violetRed1")
    draw_oval(canvas, x0=xa, y0=ya, x1=xa + 10, y1=ya + 10, fill='violetRed3', outline="violetRed3")
    draw_oval(canvas, x0=xa, y0=ya, x1=xa -10, y1=ya -10, fill='violetRed3', outline="violetRed3")
    draw_oval(canvas, x0=xa, y0=ya, x1=xa + 10, y1=ya -10, fill='violetRed1', outline="violetRed1")
    #bud
    draw_oval(canvas, x0=xa-5, y0=ya-5, x1=xa+5, y1=ya+5, fill="yellow1", outline="yellow1")


# Call the main function so that
# this program will start executing.
main()