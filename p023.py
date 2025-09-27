import turtle
import math

def haromszog(szar):
    turtle.hideturtle()
    turtle.penup()
    magassag = math.sqrt(szar**2 - (szar/2)**2)
    turtle.goto(-szar/2, -magassag/2)
    turtle.pendown()
    turtle.color("red")        # piros szín
    turtle.pensize(5)

    # Rajzolás
    for i in range(3):
        turtle.forward(szar)
        turtle.left(120)

def main():
    ablak = turtle.Screen()
    ablak.setup(600, 600)
    ablak.bgcolor("gray")
    turtle.speed(0)

    # Billentyűfigyelő események
    turtle.listen()
    turtle.onkey(lambda: haromszog(150), "h")
    turtle.onkey(turtle.bye, "q")

    ablak.mainloop()

if __name__ == "__main__":
    main()
