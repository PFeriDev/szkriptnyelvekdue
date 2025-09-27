import turtle

'''def teglalap(x, y):
    # a = 5
    # b = 4
    ker = 2 * x + 2 * y
    ter = x * y
    return ker, ter

def negyszog(x, y):
    # a = 5
    # b = 4
    ker = 2 * x + 2 * y
    ter = x * y
    if x == y:
        alakzat = "negyzet"
    else:
        alakzat = "teglalap"
    return ker, ter, alakzat

if __name__ == '__main__':
    a = 2
    b = 2
    eredmeny = negyszog(a, b)
    print(f"A {eredmeny[2]} kerulete: ", eredmeny[0])
    print(f"A {eredmeny[2]} terulete: ", eredmeny[1])
    print("Sajat hivas")'''


#negyzet
def negyzet():
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-50, 50)
    turtle.pendown()

    for i in range(4):
        turtle.forward(100)
        turtle.right(90)



#pontok rajzolasa
def pont(x,y):
    turtle.goto(x, y)
    turtle.dot(10, "black")

#dobas
def dobas():
    import random
    turtle.hideturtle()
    turtle.clear()
    negyzet()
    turtle.pensize(5)
    szam = random.randint(1, 6)
    turtle.penup()

    if szam == 1:
        pont(0, 0)
    elif szam == 2:
        pont(-30, 30)
        pont(30, -30)
    elif szam == 3:
        pont(0,0)
        pont(-30, 30)
        pont(30, -30)
    elif szam == 4:
        pont(-30, 30)
        pont(30, 30)
        pont(-30, -30)
        pont(30, -30)
    elif szam == 5:
        pont(0,0)
        pont(-30, 30)
        pont(30, 30)
        pont(-30, -30)
        pont(30, -30)
    elif szam == 6:
        pont(-30, 30)
        pont(30, 30)
        pont(-30, -30)
        pont(30, -30)
        pont(-30,0)
        pont(30, 0)



#App
ablak = turtle.Screen()

turtle.listen()
turtle.onkey(dobas, "d")
turtle.onkey(turtle.bye, "Escape")
turtle.mainloop()










