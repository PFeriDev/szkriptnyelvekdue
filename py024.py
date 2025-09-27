import turtle

def csillag(meret):
    turtle.hideturtle()
    turtle.color("yellow")
    turtle.pensize(5)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()

    for i in range(5):
        turtle.forward(meret)
        turtle.right(144)

def main():
    ablak = turtle.Screen()
    ablak.setup(600, 600)
    ablak.bgcolor("black")
    turtle.speed(5)

    turtle.listen()
    turtle.onkey(lambda: csillag(150), "h")
    turtle.onkey(turtle.bye, "q")

    ablak.mainloop()

if __name__ == "__main__":
    main()
