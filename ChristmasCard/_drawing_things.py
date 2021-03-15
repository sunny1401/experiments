
import turtle
import colorsys
import random
import time
import math


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


class Snow:
    snb_wdth = snb_hgt = 500
    snb_rate = 10, 20
    snb_size = 5, 15
    wnd_chng = 1, 10
    max_wnd = 6
    lssnb = []

    x_pos = 0
    y_pos = 75, 0, -100
    size = 75

    y_off = 10
    x_sep = 15

    t_delay = 0
    s_time = time.time()
    wind = 0
    w_delay = 5
    w_timer = time.time()
    w_step = 0.1


def circle(t_name, x, y, size, colour):
    t_name.color(colour)
    t_name.penup()
    t_name.setposition(x, y)
    t_name.dot(size)


def snbll():
    snowball = turtle.Turtle()
    snowball.color("white")
    snowball.penup()
    snowball.setposition(random.randint(-2 * Snow.snb_wdth, Snow.snb_wdth / 2), Snow.snb_hgt / 2)
    snowball.hideturtle()
    snowball.size = random.randint(*Snow.snb_size)
    Snow.lssnb.append(snowball)


def move_snowball(t_name, falling_speed=1, wind=0):
    t_name.clear()
    t_name.sety(t_name.ycor() - falling_speed)
    if wind:
        t_name.setx(t_name.xcor() + wind)
    t_name.dot(t_name.size)


def sm_person():
    snman = turtle.Turtle()

    for y in Snow.y_pos:
        circle(snman, Snow.x_pos, y, Snow.size, "white")
        Snow.size = Snow.size * 1.5

    button_seperation = 25
    button_pos = [Snow.y_pos[1] - button_seperation,
                          Snow.y_pos[1],
                          Snow.y_pos[1] + button_seperation]
    for y in button_pos:
        circle(snman, Snow.x_pos, y, 10, "black")



    for x in Snow.x_pos - Snow.x_sep, Snow.x_pos + Snow.x_sep:
        circle(snman, x, Snow.y_pos[0] + Snow.y_off, 20, "green")
        circle(snman, x, Snow.y_pos[0] + Snow.y_off, 10, "black")

    snman.color("orange")
    snman.setposition(Snow.x_pos - 10, Snow.y_pos[0] - Snow.y_off)
    snman.shape("triangle")
    snman.setheading(200)
    snman.turtlesize(0.5, 2.5)

    snman_grass = turtle.Turtle()
    snman_grass.hideturtle()
    snman_grass.speed(0)
    snman_grass.fillcolor("forest green")
    snman_grass.penup()
    snman_grass.setposition(-Snow.snb_wdth / 2, -Snow.snb_hgt / 2)
    snman_grass.begin_fill()
    for _ in range(2):
        snman_grass.forward(Snow.snb_wdth)
        snman_grass.left(90)
        snman_grass.forward(70)
        snman_grass.left(90)
    snman_grass.end_fill()

    ground = turtle.Turtle()
    ground.hideturtle()
    turtle.tracer(0, 0)
    for x in range(int(-Snow.snb_wdth / 2), int(Snow.snb_wdth / 2), int(Snow.snb_wdth / 200)):
        circle(ground, x, -180, random.randint(5, 20), "white")
    turtle.update()

    snm_p_text = turtle.Turtle()
    snm_p_text.hideturtle()
    snm_p_text.color("red")
    snm_p_text.penup()
    snm_p_text.setposition(-100, 170)
    snm_p_text.write("Happy Holidays!", font=("Apple Chancery", 30, "bold"), align="center")


def update_effect(wn):

    count = 0
    while True:
        if count == 30:
            break
        snbll()
        Snow.s_time = time.time()
        Snow.t_delay = random.randint(*Snow.snb_rate) / 10

        for snowball in Snow.lssnb:
            move_snowball(snowball, wind=Snow.wind)
            if snowball.ycor() < - Snow.snb_hgt / 2:
                snowball.clear()
                Snow.lssnb.remove(snowball)

        if time.time() - Snow.w_timer > Snow.w_delay:
            Snow.wind += Snow.w_step
            if Snow.wind >= Snow.max_wnd:
                Snow.w_step = -Snow.w_step
            elif Snow.wind <= 0:
                Snow.w_step = abs(Snow.w_step)

            Snow.w_timer = time.time()
            Snow.w_delay = random.randint(*Snow.wnd_chng) / 10

        wn.update()
        count += 1


class BB:
    hue_val = 0.22
    dark_idx_max = 0.01
    bright_idxx_max = 1
    refresh_rate = 30
    timer_val = 1000 // refresh_rate
    cycle = 5
    light_band = 1
    speed = 30
    close_e = 16
    n = 100

    v = []
    curr_t = 0
    stars = []
    phase = []
    curr_xpos = []
    curr_ypos = []
    target_xpos = []
    target_ypos = []


def nsky_stars():
    for i in range(BB.n):
        BB.stars.append(turtle.Turtle())
        BB.v.append(BB.dark_idx_max)
        BB.phase.append(random.uniform(0, BB.cycle))
        BB.curr_xpos.append(random.uniform(-500, 500))
        BB.curr_ypos.append(random.uniform(-500, 500))
        BB.target_xpos.append(random.uniform(-500, 500))
        BB.target_ypos.append(random.uniform(-500, 500))

    for star in BB.stars:
        star.hideturtle()
        star.up()


def twinkle(phase):
    if phase < (BB.cycle - BB.light_band):
        temp = BB.dark_idx_max
    elif phase < BB.cycle-BB.light_band/2:
        temp = BB.dark_idx_max + (
                BB.bright_idxx_max-BB.dark_idx_max)*(
                phase-(BB.cycle-BB.light_band))/(BB.light_band/2)
    else:
        temp = BB.bright_idxx_max - (
                BB.bright_idxx_max-BB.dark_idx_max)*(
                phase-(BB.cycle-BB.light_band/2))/(BB.light_band/2)
    return temp


def update_color():

    for i in range(BB.n):
        BB.phase[i] += BB.timer_val / 1000  # increase the phase by time passed
        if BB.phase[i] > BB.cycle:  # phase passed CYCLE
            BB.phase[i] -= BB.cycle  # make sure phase stays within CYCLE
        BB.v[i] = twinkle(BB.phase[i])


def update_loc():
    for i in range(BB.n):
        angle_to_target = math.atan2(BB.target_ypos[i] - BB.curr_ypos[i], BB.target_xpos[i] - BB.curr_xpos[i])
        BB.curr_xpos[i] += BB.speed / BB.refresh_rate * math.cos(angle_to_target)
        BB.curr_ypos[i] += BB.speed / BB.refresh_rate * math.sin(angle_to_target)
        dist_to_target_squared = (BB.curr_xpos[i] - BB.target_xpos[i]) ** 2 + (
                BB.curr_ypos[i] - BB.target_ypos[i]
        ) ** 2
        if dist_to_target_squared < BB.close_e:
            BB.target_xpos[i] = random.randint(-500, 500)
            BB.target_ypos[i] = random.randint(-500, 500)


def bb_draw():
    for i in range(BB.n):
        BB.stars[i].clear()
        color = colorsys.hsv_to_rgb(BB.hue_val, 1, BB.v[i])
        BB.stars[i].color(color)
        BB.stars[i].goto(BB.curr_xpos[i], BB.curr_ypos[i])
        BB.stars[i].dot(10)


b_code = ('#7a5230', '#614126', '#49311c', '#302013', '#181009')
g_code_key = ('#004000', '#003300', '#002600', '#001900', '#004c00')


def sky_things():
    s1 = turtle.Turtle()
    s1.color('#e5e5ff')
    s1.pensize(100)
    s1.speed(0)
    s1.hideturtle()
    s1.penup()
    s1.goto(-200, -200)
    s1.pendown()

    skycol = ['add8e6', 'b5d8e5', 'bdd8e4', 'c5d8e3', 'cdd8e3', 'd6d8e2', 'ded8e1', 'e6d8e1', 'eed8e0', 'f6d8df',
              'ffd9df']
    for i in skycol:
        temp = '#' + i
        s1.color(temp)
        s1.forward(500)
        s1.left(90)
        s1.forward(20)
        s1.left(90)

        s1.color(temp)
        s1.forward(500)
        s1.right(90)
        s1.forward(20)
        s1.right(90)


def mountains():
    m1 = turtle.Turtle()
    m1.pensize()
    m1.color('#a9a9a9')
    m1.speed(0)
    m1.hideturtle()

    m1.penup()
    m1.goto(-300, -100)
    m1.pendown()
    m1.begin_fill()
    for i in range(10):
        templen = random.randint(20, 200)

        tempang = random.randint(45, 80)

        m1.left(tempang)
        m1.forward(templen)
        m1.right(2 * tempang)
        m1.forward(templen)
        m1.setheading(0)

    m1.goto(300, -400)
    m1.goto(-300, -400)
    m1.end_fill()

    m1.color('#d3d3d3')
    m1.penup()
    m1.goto(-300, -150)
    m1.pendown()
    m1.begin_fill()

    for i in range(10):
        templen = random.randint(20, 200)

        tempang = random.randint(20, 30)

        m1.left(tempang)
        m1.forward(templen)
        m1.right(2 * tempang)
        m1.forward(templen)
        m1.setheading(0)

    m1.goto(300, -400)
    m1.goto(-300, -400)
    m1.end_fill()

    m1.color('#6d8383')
    m1.penup()
    m1.goto(-300, -165)
    m1.pendown()
    m1.begin_fill()
    for i in range(10):
        templen = random.randint(20, 200)

        tempang = random.randint(10, 20)

        m1.left(tempang)
        m1.forward(templen)
        m1.right(2 * tempang)
        m1.forward(templen)
        m1.setheading(0)

    m1.goto(300, -400)
    m1.goto(-300, -400)
    m1.end_fill()


def cloudthingy():
    cloud = turtle.Turtle()
    cloud.color('white')
    cloud.speed(0)
    cloud.hideturtle()

    def randloc():
        location = random.randint(-250, 250), random.randint(0, 270)
        return location

    def paintthingy(location, leng):
        cloud.penup()
        cloud.goto(location)
        cloud.pendown()
        cloud.pensize(random.randint(3, 5))
        cloud.forward(leng)

    def lonecloud():
        temp = randloc()
        temp2 = temp[1]
        temp3 = temp[0]
        leng = 30

        for i in range(20):
            temp4 = (temp3, temp2)
            paintthingy(temp4, leng)
            temp2 += 1
            temp3 += random.randint(-10, 10)
            leng += random.randint(-40, 40)

    for _ in range(6):
        lonecloud()


def lily_thing():
    lily = turtle.Turtle()
    lily.speed(0)
    for _ in range(25):
        lily.color(g_code_key[random.randint(0, 4)])
        lily.penup()
        lily.goto(random.randint(0, 200), random.randint(-300, -175))
        lily.pendown()
        for i in range(2, 7):
            lily.forward(2)
            lily.pensize(i)
        for i in range(0, 7):
            lily.forward(2)
            lily.pensize(7 - i)


def grass_things(amount, locx, locy):
    t1 = turtle.Turtle()
    t1.color('#004000')
    t1.hideturtle()

    def t1draw(size):
        if random.randint(0, 1) == 1:
            size = -size
        t1.color(g_code_key[random.randint(0, 4)])
        t1.penup()
        t1.goto(locx + size, locy + size)
        t1.pendown()
        t1.goto(locx + 5 + size, locy + 10 + size)
        t1.goto(locx + size, locy + size)
        t1.goto(locx - 5 + size, locy + 10 + size)
        t1.goto(locx - 1 + size, locy - 1 + size)
        t1.goto(locx + 3 + size, locy + 6 + size)
        t1.goto(locx + 1 + size, locy - 1 + size)
        t1.goto(locx - 2 + size, locy + 5 + size)

    for _ in range(amount):
        for j in range(random.randint(1, 4)):
            t1draw(j * 3)


def green_things():
    grass = turtle.Turtle()
    grass.color('#007b0c')
    grass.speed(0)
    grass.hideturtle()

    t1 = turtle.Turtle()
    t1.pensize(5)
    t1.color('#654321')
    t1.speed(0)
    t1.hideturtle()

    def grassdraw():
        grass.penup()
        grass.goto(random.randint(-160, -150), random.randint(-240, -190))

        grass.pendown()
        grass.begin_fill()
        for _ in range(200):
            grass.color(g_code_key[random.randint(0, 4)])
            grass.goto(random.randint(-300, -50), random.randint(-200, -150))

        grass.end_fill()

    def greentree():
        temppos = t1.pos()
        t1.color(g_code_key[random.randint(0, 4)])
        t1.pensize(1)

        t1.setheading(90)
        t1.begin_fill()
        t1.forward(40)
        t1.right(160)
        t1.forward(50)
        t1.end_fill()

        t1.setheading(90)
        t1.goto(temppos)
        t1.begin_fill()
        t1.forward(40)
        t1.left(160)
        t1.forward(50)
        t1.end_fill()

        t1.goto(temppos)
        t1.setheading(90)  # part 2
        t1.begin_fill()
        t1.forward(50)
        t1.right(160)
        t1.forward(50)
        t1.end_fill()

        t1.setheading(90)
        t1.goto(temppos)
        t1.begin_fill()
        t1.forward(50)
        t1.left(160)
        t1.forward(50)
        t1.end_fill()

        t1.goto(temppos)
        t1.setheading(90)  # part 3
        t1.begin_fill()
        t1.forward(60)
        t1.right(160)
        t1.forward(50)
        t1.end_fill()

        t1.setheading(90)
        t1.goto(temppos)
        t1.begin_fill()
        t1.forward(60)
        t1.left(160)
        t1.forward(50)
        t1.end_fill()

    grassdraw()

    t1.speed(0)

    def trees(treesnb_hgt):
        t1.color(b_code[random.randint(0, 4)])
        t1.pensize(random.randint(2, 4))
        t1.penup()

        t1.goto(treesnb_hgt)  # goes to random location and draws random length
        t1.pendown()
        t1.setheading(90)
        t1.forward(random.randint(20, 30))

        greentree()

        t1.left(270)  # turns back to the normal direction

    for i in range(10):
        temph = random.randint(-270, -80), random.randint(-180, -170)
        trees(temph)
    for i in range(10):
        temph = random.randint(-270, -80), random.randint(-200, -190)
        trees(temph)


def lake_stuff():
    l2 = turtle.Turtle()
    l2.speed(0)
    l2.hideturtle()
    blues = ['00004c', '000066', '000099', '0000b2', '0000cc', '0000e5', '0000ff']

    l2.penup()
    l2.goto(random.randint(-50, 50), random.randint(-170, -150))
    temp = turtle.Turtle()
    temp.penup()
    temp.hideturtle()
    temp.goto(l2.pos())
    l2.pendown()

    l2.begin_fill()

    l2.pensize(5)
    for i in range(50):
        l2.color("#" + blues[random.randint(0, 6)])
        l2.forward(5)
        l2.right(random.randint(0, 5) / 10)
        if random.randint(0, 2) == 2:
            grass_things(5, l2.pos()[0], l2.pos()[1])
    while l2.heading() > 185:
        l2.color("#" + blues[random.randint(0, 6)])
        l2.forward(2)
        l2.right(random.randint(-2, 8))
    for i in range(50):
        l2.color("#" + blues[random.randint(0, 6)])
        l2.forward(5)
        l2.left(random.randint(0, 2) / 10)
    for i in range(100):
        l2.color("#" + blues[random.randint(0, 6)])
        l2.forward(5)
        l2.right(random.randint(0, 8) / 10)

    l2.color("#" + blues[1])
    l2.goto(temp.pos())
    l2.end_fill()


def snowflakes():
    turtle.hideturtle()
    turtle.pensize(2)
    for _ in range(50):
        turtle.pencolor('light blue')
        turtle.penup()
        turtle.setx(random.randint(-350, 350))
        turtle.sety(random.randint(1, 270))

        turtle.pendown()
        dens = random.randint(1, 15)
        snowsize = random.randint(1, 6)
        for j in range(dens):
            turtle.forward(snowsize)
            turtle.backward(snowsize)
            turtle.right(360 / dens)


def nsky_moon():
    mturtle = turtle.Turtle()
    mturtle.up()
    mturtle.goto(160, 140)
    mturtle.down()
    mturtle.color("white")
    mturtle.begin_fill()
    mturtle.circle(90)
    mturtle.end_fill()
    mturtle.hideturtle()
