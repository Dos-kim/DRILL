import turtle
import random


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1920, 1080)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()



def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))



def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())




def draw_curve_3_points(p1, p2, p3):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3

    for i in range(0, 100, 2):
        t = i / 100
        x = (2 * t ** 2 - 3 * t + 1) * x1 + (-4 * t ** 2 + 4 * t) * x2 + (2 * t ** 2 - t) * x3
        y = (2 * t ** 2 - 3 * t + 1) * y1 + (-4 * t ** 2 + 4 * t) * y2 + (2 * t ** 2 - t) * y3
        draw_point((x, y))
    draw_point(p3)


def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        draw_point((x, y))
    draw_point(p4)

def draw_line(p1,p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1,y1 = p1; x2,y2 =p2

    for i in range(-100,100, 2):
        t = i/100
        x= (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        draw_point((x,y))


    draw_point(p2)


def p_grap(p1,p2,p3,p4,p5):

    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4; x5,y5 = p5


 # draw p1 - p2
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*x4 + (3*t**3 - 5*t**2 + 2)*x1 + (-3*t**3 + 4*t**2 + t)*x2 + (t**3 - t**2)*x3)/2
        y = ((-t**3 + 2*t**2 - t)*y4 + (3*t**3 - 5*t**2 + 2)*y1 + (-3*t**3 + 4*t**2 + t)*y2 + (t**3 - t**2)*y3)/2
        draw_point((x, y))
    draw_point(p2)

    # draw p2 - p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*x1 + (3*t**3 - 5*t**2 + 2)*x2 + (-3*t**3 + 4*t**2 + t)*x3 + (t**3 - t**2)*x4)/2
        y = ((-t**3 + 2*t**2 - t)*y1 + (3*t**3 - 5*t**2 + 2)*y2 + (-3*t**3 + 4*t**2 + t)*y3 + (t**3 - t**2)*y4)/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3 - p4
    for i in range(50, 100, 2):
        t = i / 100
        x = ((2*t**2-3*t+1)*x2 + (-4*t**2+4*t)*x3 + (2*t**2-t)*x4 + (2 * t ** 2 - 3 * t + 1) * x2 + (-4 * t ** 2 + 4 * t) * x3 + (2 * t ** 2 - t) * x4)/2
        y = ((2*t**2-3*t+1)*y2 + (-4*t**2+4*t)*y3 + (2*t**2-t)*y4 + (2 * t ** 2 - 3 * t + 1) * y2 + (-4 * t ** 2 + 4 * t) * y3 + (2 * t ** 2 - t) * y4)/2
        draw_point((x, y))
    draw_point(p4)

    # draw p4 - p5
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*x3 + (3*t**3 - 5*t**2 + 2)*x4 + (-3*t**3 + 4*t**2 + t)*x5 + (t**3 - t**2)*x2)/2
        y = ((-t**3 + 2*t**2 - t)*y3 + (3*t**3 - 5*t**2 + 2)*y4 + (-3*t**3 + 4*t**2 + t)*y5 + (t**3 - t**2)*y2)/2
        draw_point((x,y))
    draw_point(p5)
prepare_turtle_canvas()

p1 = x1, y1 = (100,100)
p2 = x2, y2 = (-50,400)
p3 = x3, y3 = (-200, -200)
p4 = x4, y4 = (400, -50)


# draw_line(p1,p2)

p_grap(p1,p2,p3,p4,p1)
p_grap(p1,p2,p3,p4,p1)
















turtle.done()
