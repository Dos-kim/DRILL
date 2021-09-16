from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# fill here

x = 10
y = 90

# square

def r_move():
    global x,y
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x += 2

        delay(0.001)

def u_move():
    global x,y
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
            
        y += 2

        delay(0.001)

def l_move():
    global x,y
    while x > 10:
        
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        x -= 2

        delay(0.001)


def d_move():
    global x,y
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)

        y -= 2

        delay(0.001)
    


# circle

r = 0



def c_move():
    global r
    while(r < 360):
        c_x =  400 + 210 * math.sin( r / 360 * 2 * math.pi)
        c_y=   300 + 210 * math.cos( r / 360 * 2 * math.pi)
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(c_x,c_y)

        r += 2
        delay(0.01)





count = 0

while(True):
        r_move()
        u_move()
        l_move()
        d_move()
        c_move()
   



close_canvas()
