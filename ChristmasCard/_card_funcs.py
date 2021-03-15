from _drawing_things import *
import time


def duel_hp(long_text):

    wn = turtle.Screen()
    wn.setup(600, 600)
    turtle.tracer(0, 0)
    sky_things()
    cloudthingy()
    mountains()
    lake_stuff()
    lily_thing()
    green_things()
    snowflakes()
    cutthepic()
    turtle.update()

    time.sleep(3)
    turtle.clear()

    wn.clear()
    wn.setup()
    add_text(long_text)
    wn.exitonclick()


def se_prof(long_text):
    wn = turtle.Screen()
    wn.setup(650, 650)
    turtle.tracer(0, 0)
    sky_things()
    cloudthingy()
    mountains()
    lake_stuff()
    lily_thing()
    green_things()
    cutthepic()
    turtle.update()
    snm_p_text = turtle.Turtle()
    snm_p_text.hideturtle()
    snm_p_text.color("brown")
    snm_p_text.penup()
    snm_p_text.setposition(-100, 170)
    snm_p_text.write("Happy Holidays!", font=("Apple Chancery", 30, "bold"), align="center")
    update_effect(wn)
    turtle.clear()
    wn.clear()
    wn.setup()
    add_text(long_text)
    wn.exitonclick()


def diplomatic_comm_guide(long_text):
    wn = turtle.Screen()
    wn.setup(500, 500)
    turtle.tracer(0, 0)
    wn.bgcolor("blue")
    count = 0

    def update():
        update_color()
        update_loc()
        wn.ontimer(update, BB.timer_val)

    nsky_stars()
    nsky_moon()
    sm_person()
    update()

    while True:
        if count == 150:
            break
        bb_draw()
        wn.update()
        count += 1

    wn.clear()
    wn.setup()
    add_text(long_text)
    wn.exitonclick()



def sisyphus_lives_on(long_text):
    wn = turtle.Screen()
    wn.setup(600, 600)
    wn.bgcolor("sky blue")
    sm_person()
    wn.title("Happy Holidays")
    update_effect(wn)
    turtle.clear()
    wn.clear()
    wn.setup()
    add_text(long_text)
    wn.exitonclick()
