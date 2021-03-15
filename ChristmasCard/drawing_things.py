b_code = ['#7a5230','#614126','#49311c','#302013','#181009']
g_code_key = ['#004000','#003300','#002600','#001900','#004c00']

import turtle
from random import randint


def sky_things():
    sky = turtle.Turtle()
    sky.color('#e5e5ff')
    sky.pensize(100)
    sky.speed(0)
    sky.hideturtle()
    sky.penup()
    sky.goto(-200, -200)
    sky.pendown()

    skycol = ['add8e6', 'b5d8e5', 'bdd8e4', 'c5d8e3', 'cdd8e3', 'd6d8e2', 'ded8e1', 'e6d8e1', 'eed8e0', 'f6d8df',
              'ffd9df']
    for i in skycol:
        temp = '#' + i
        sky.color(temp)
        sky.forward(500)
        sky.left(90)
        sky.forward(20)
        sky.left(90)

        sky.color(temp)
        sky.forward(500)
        sky.right(90)
        sky.forward(20)
        sky.right(90)


def mountains():
    mountain = turtle.Turtle()
    mountain.pensize()
    mountain.color('#a9a9a9')
    mountain.speed(0)
    mountain.hideturtle()

    mountain.penup()
    mountain.goto(-300, -100)
    mountain.pendown()
    mountain.begin_fill()
    for i in range(10):
        templen = randint(20, 200)

        tempang = randint(45, 80)

        mountain.left(tempang)
        mountain.forward(templen)
        mountain.right(2 * tempang)
        mountain.forward(templen)
        mountain.setheading(0)

    mountain.goto(300, -400)
    mountain.goto(-300, -400)
    mountain.end_fill()

    mountain.color('#d3d3d3')
    mountain.penup()
    mountain.goto(-300, -150)
    mountain.pendown()
    mountain.begin_fill()

    for i in range(10):
        templen = randint(20, 200)

        tempang = randint(20, 30)

        mountain.left(tempang)
        mountain.forward(templen)
        mountain.right(2 * tempang)
        mountain.forward(templen)
        mountain.setheading(0)

    mountain.goto(300, -400)
    mountain.goto(-300, -400)
    mountain.end_fill()

    mountain.color('#6d8383')
    mountain.penup()
    mountain.goto(-300, -165)
    mountain.pendown()
    mountain.begin_fill()
    for i in range(10):
        templen = randint(20, 200)

        tempang = randint(10, 20)

        mountain.left(tempang)
        mountain.forward(templen)
        mountain.right(2 * tempang)
        mountain.forward(templen)
        mountain.setheading(0)

    mountain.goto(300, -400)
    mountain.goto(-300, -400)
    mountain.end_fill()


def cloudthingy():
    cloud = turtle.Turtle()
    cloud.color('white')
    cloud.speed(0)
    cloud.hideturtle()

    def randloc():
        location = randint(-250, 250), randint(0, 270)
        return location

    def brushstroke(randloc, leng):
        cloud.penup()
        cloud.goto(randloc)
        cloud.pendown()
        cloud.pensize(randint(3, 5))
        cloud.forward(leng)

    def singlecloud():
        temp = randloc()
        temp2 = temp[1]
        temp3 = temp[0]
        leng = 30

        for i in range(20):
            temp4 = (temp3, temp2)
            brushstroke(temp4, leng)
            temp2 += 1
            temp3 += randint(-10, 10)
            leng += randint(-40, 40)

    for i in range(4):
        singlecloud()


def lilypads(amount):
    lily = turtle.Turtle()
    lily.speed(0)
    lily.hideturtle()
    for i in range(amount):
        lily.color(g_code_key[randint(0, 4)])
        lily.penup()
        lily.goto(randint(0, 200), randint(-300, -175))
        lily.pendown()
        for i in range(2, 7):
            lily.forward(2)
            lily.pensize(i)
        for i in range(0, 7):
            lily.forward(2)
            lily.pensize(7 - i)


def grass_things(amount, locx, locy):
    tuft = turtle.Turtle()
    tuft.color('#004000')
    tuft.hideturtle()

    def tuftdraw(size):
        if randint(0, 1) == 1:
            size = -size
        tuft.color(g_code_key[randint(0, 4)])
        tuft.penup()
        tuft.goto(locx + size, locy + size)
        tuft.pendown()
        tuft.goto(locx + 5 + size, locy + 10 + size)
        tuft.goto(locx + size, locy + size)
        tuft.goto(locx - 5 + size, locy + 10 + size)
        tuft.goto(locx - 1 + size, locy - 1 + size)
        tuft.goto(locx + 3 + size, locy + 6 + size)
        tuft.goto(locx + 1 + size, locy - 1 + size)
        tuft.goto(locx - 2 + size, locy + 5 + size)

    for i in range(amount):
        for i in range(randint(1, 4)):
            tuftdraw(i * 3)


def green_things():
    grass = turtle.Turtle()
    grass.color('#007b0c')
    grass.speed(0)
    grass.hideturtle()

    trees = turtle.Turtle()
    trees.pensize(5)
    trees.color('#654321')
    trees.speed(0)
    trees.hideturtle()

    def grassdraw():
        grass.penup()
        grass.goto(randint(-160, -150), randint(-240, -190))

        grass.pendown()
        grass.begin_fill()
        for i in range(200):
            grass.color(g_code_key[randint(0, 4)])
            grass.goto(randint(-300, -50), randint(-200, -150))

        grass.end_fill()

    def greentree():
        temppos = trees.pos()
        trees.color(g_code_key[randint(0, 4)])
        trees.pensize(1)

        trees.setheading(90)
        trees.begin_fill()
        trees.forward(40)
        trees.right(160)
        trees.forward(50)
        trees.end_fill()

        trees.setheading(90)
        trees.goto(temppos)
        trees.begin_fill()
        trees.forward(40)
        trees.left(160)
        trees.forward(50)
        trees.end_fill()

        trees.goto(temppos)
        trees.setheading(90)  # part 2
        trees.begin_fill()
        trees.forward(50)
        trees.right(160)
        trees.forward(50)
        trees.end_fill()

        trees.setheading(90)
        trees.goto(temppos)
        trees.begin_fill()
        trees.forward(50)
        trees.left(160)
        trees.forward(50)
        trees.end_fill()

        trees.goto(temppos)
        trees.setheading(90)  # part 3
        trees.begin_fill()
        trees.forward(60)
        trees.right(160)
        trees.forward(50)
        trees.end_fill()

        trees.setheading(90)
        trees.goto(temppos)
        trees.begin_fill()
        trees.forward(60)
        trees.left(160)
        trees.forward(50)
        trees.end_fill()

    grassdraw()

    trees.speed(0)

    def treees(treeheight):
        trees.color(b_code[randint(0, 4)])
        trees.pensize(randint(2, 4))
        trees.penup()

        trees.goto(treeheight)  # goes to random location and draws random length
        trees.pendown()
        trees.setheading(90)
        trees.forward(randint(20, 30))

        greentree()

        trees.left(270)  # turns back to the normal direction

    for i in range(10):
        temph = randint(-270, -80), randint(-180, -170)
        treees(temph)
    for i in range(10):
        temph = randint(-270, -80), randint(-200, -190)
        treees(temph)


def lake_stuff():
    lake = turtle.Turtle()
    lake.speed(0)
    lake.hideturtle()
    blues = ['00004c', '000066', '000099', '0000b2', '0000cc', '0000e5', '0000ff']

    lake.penup()
    lake.goto(randint(-50, 50), randint(-170, -150))
    temp = turtle.Turtle()
    temp.penup()
    temp.hideturtle()
    temp.goto(lake.pos())
    lake.pendown()

    lake.begin_fill()

    lake.pensize(5)
    for i in range(50):
        lake.color("#" + blues[randint(0, 6)])
        lake.forward(5)
        lake.right(randint(0, 5) / 10)
        if randint(0, 2) == 2:
            grass_things(5, lake.pos()[0], lake.pos()[1])
    while lake.heading() > 185:
        lake.color("#" + blues[randint(0, 6)])
        lake.forward(2)
        lake.right(randint(-2, 8))
    for i in range(50):
        lake.color("#" + blues[randint(0, 6)])
        lake.forward(5)
        lake.left(randint(0, 2) / 10)
    for i in range(100):
        lake.color("#" + blues[randint(0, 6)])
        lake.forward(5)
        lake.right(randint(0, 8) / 10)

    lake.color("#" + blues[1])
    lake.goto(temp.pos())
    lake.end_fill()


def cutthepic():
    cut = turtle.Turtle()
    cut.speed(0)
    cut.penup()
    cut.hideturtle()

    cut.color('black')
    cut.pensize(30)
    cut.goto(-275, 300)
    cut.pendown()
    cut.goto(275, 300)
    cut.goto(275, -300)
    cut.goto(-275, -300)
    cut.goto(-275, 300)

    cut.penup()
    cut.speed(9)
    cut.color('white')
    cut.pensize(200)
    cut.goto(-370, 395)
    cut.pendown()
    cut.goto(370, 395)
    cut.goto(370, -395)
    cut.goto(-370, -395)
    cut.goto(-370, 395)


def add_text(long_text):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    y = 200
    text.goto(-55, y)
    text.pendown()
    text.color('black')
    style = ('Comic Sans MS', 20, 'normal')
    for i in long_text:
        text.write(i, font=style, align='center')

        y -= 30
        text.penup()
        text.goto(-55, y)

        text.pendown()
    style = ('Comic Sans MS', 20, 'italic')
    text.penup()
    text.goto(-55, y - 20)
    text.pendown()
    text.write("Have a merry merry Christmas and a great new year !!", font=style, align='center')
