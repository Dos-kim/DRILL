import turtle

count = 0

while(count <6):
    turtle.goto(500,100*count)
    turtle.penup()
    count += 1
    turtle.goto(0,100*count)
    turtle.pendown()

turtle.penup()
turtle.home()
turtle.pendown()

count = 0

while(count<6):
    turtle.goto(100*count,500)
    turtle.penup()
    count +=1
    turtle.goto(100*count,0)
    turtle.pendown()


turtle.exitonclick()
