# !/usr/bin/env python3
# -*- coding: utf-8 -*-


# @Author: dong
# @Date: 2018-07-05 19:37:42
# @Env: python 3.6
# @Github: https://github.com/PerpetualSmile


# Modified by [Your Name] [Your SID]
# Submit Time:[]
# For assignment of ELEG4701 CUHK


'''

TODO: change this doraemon into origin version(with ears, yellow skin)

* Besides, you can do everything you want, such as change the pose, add decorations,
  or even draw another anime character, and you will get a higher score.

'''

'''
You Need to Know:
codes like '#ffffff' are hexadecimal color codes,
usually used to represent colors in html.
In the RGB model of computer, every two digits in #rrggbb represents a number. 
Each number is in hexadecimal(0~F)
#000000 represents pure black
#FFFFFF represents pure white
'''

'''
If you donot know what is a function stand for
Please search it in google. Eg: 'python turtle seth'
or you can use help(seth)
'''

from turtle import *

body_color = "#FCB420" #'#00a0de'

def my_goto(x, y):
    penup()
    goto(x, y)
    pendown()


def eyes():
    fillcolor("#ffffff")
    begin_fill()

    tracer(False)
    a = 2.5
    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a -= 0.05
            lt(3)
            fd(a)
        else:
            a += 0.05
            lt(3)
            fd(a)
    tracer(True)
    end_fill()


def beard():
    my_goto(-32, 135)
    seth(165)
    fd(60)

    my_goto(-32, 125)
    seth(180)
    fd(60)

    my_goto(-32, 115)
    seth(193)
    fd(60)

    my_goto(37, 135)
    seth(15)
    fd(60)

    my_goto(37, 125)
    seth(0)
    fd(60)

    my_goto(37, 115)
    seth(-13)
    fd(60)


def mouth():
    my_goto(5, 148)
    seth(270)
    fd(100)
    seth(0)
    circle(120, 50)
    seth(230)
    circle(-120, 100)


def scarf():
    fillcolor('#e70010')
    begin_fill()
    seth(0)
    fd(200)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    fd(207)
    circle(-5, 90)
    fd(10)
    circle(-5, 90)
    end_fill()


def nose():
    my_goto(-10, 158)
    seth(315)
    fillcolor('#e70010')
    begin_fill()
    circle(20)
    end_fill()


def wink():
    seth(0)
    my_goto(-20, 195)
    fillcolor('#000000')
    begin_fill()
    circle(13)
    end_fill()

    pensize(6)
    my_goto(20, 205)
    seth(75)
    circle(-10, 150)
    pensize(3)

    my_goto(-17, 200)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    circle(5)
    end_fill()
    my_goto(0, 0)


def face():
    fd(183)
    lt(45)
    fillcolor('#ffffff')
    begin_fill()
    circle(120, 100)
    seth(180)
    # print(pos())
    fd(121)
    pendown()
    seth(215)
    circle(120, 100)
    end_fill()
    my_goto(63.56, 218.24)
    seth(90)
    eyes()
    seth(180)
    penup()
    fd(60)
    pendown()
    seth(90)
    eyes()
    penup()
    seth(180)
    fd(64)


def head():
    penup()
    circle(150, 40)
    pendown()
    fillcolor(body_color)
    begin_fill()
    circle(150, 280)
    end_fill()

def body_handsup():
    my_goto(0, 0)
    seth(0)
    penup()
    circle(150, 50)
    pendown()
    seth(30)
    fd(40)
    seth(70)
    circle(-30, 270)

    fillcolor(body_color)
    begin_fill()

    seth(230)
    fd(80)
    seth(90)
    circle(1000, 1)
    seth(-89)
    circle(-1000, 10)

    seth(180)
    fd(70)
    seth(90)
    circle(30, 180)
    seth(180)
    fd(70)

    seth(100)
    circle(-1000, 9)

    seth(-86)
    circle(1000, 2)
    seth(230)
    fd(40)

    circle(-30, 230)
    seth(45)
    fd(81)
    seth(0)
    fd(203)
    circle(5, 90)
    fd(10)
    circle(5, 90)
    fd(7)
    seth(40)
    circle(150, 10)
    seth(30)
    fd(40)
    end_fill()
    

    seth(70)
    fillcolor('#ffffff')
    begin_fill()
    circle(-30)
    end_fill()

    
    my_goto(-133.97, -91.81)
    seth(50)
    fillcolor('#ffffff')
    begin_fill()
    circle(30)
    end_fill()


def foot():
    
    my_goto(103.74, -182.59)
    seth(0)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(-15, 180)
    fd(90)
    circle(-15, 180)
    fd(10)
    end_fill()

    my_goto(-96.26, -182.59)
    seth(180)
    fillcolor('#ffffff')
    begin_fill()
    fd(15)
    circle(15, 180)
    fd(90)
    circle(15, 180)
    fd(10)
    end_fill()

def bag():
    
    fillcolor('#ffffff')

    my_goto(-103.42, 15.09)
    seth(0)
    fd(38)
    seth(230)
    begin_fill()
    circle(90, 260)
    end_fill()

    my_goto(5, -40)
    seth(0)
    fd(70)
    seth(-90)
    circle(-70, 180)
    seth(0)
    fd(70)

    my_goto(-103.42, 15.09)
    fd(90)
    seth(70)

def bell():
    fillcolor('#ffd200')
    # print(pos())
    begin_fill()
    circle(-20)
    end_fill()
    seth(170)
    fillcolor('#ffd200')
    begin_fill()
    circle(-2, 180)
    seth(10)
    circle(-100, 22)
    circle(-2, 180)
    seth(180 - 10)
    circle(100, 22)
    end_fill()
    goto(-13.42, 15.09)
    seth(250)
    circle(20, 110)
    seth(90)
    fd(15)
    dot(10)
    my_goto(0, -150)

def body():
    body_handsup()
    foot()
    bag()
    bell()


def ear(earCenter=[-10,10], angle=0):
    import numpy as np
    fillcolor(body_color)
    seth(angle)
    my_goto(earCenter[0], earCenter[1])
    begin_fill()
    ew = 50
    el = 80
    fd(ew//2)
    ca = (el * el + ew * ew - el * el)/(2*el*ew)
    a = np.rad2deg(np.arccos(ca))
    b = 180 - 2 * a
    lt(180-a)
    fd(el)
    lt(180-b)
    fd(el)
    lt(180-a)
    fd(ew//2)
    end_fill()




def Doraemon():
    head()
    scarf()
    face()
    nose()
    mouth()
    beard()
    body()
    wink()
    #
    ear([110, 250], -45)
    ear([-110, 250], 45)


if __name__ == '__main__':
    screensize(800, 600, "#f0f0f0")
    pensize(3)  
    speed(900) # speed of painting

    Doraemon()

    #draw your name
    my_goto(0, -300)
    write('Answer',\
         font=("Bradley Hand ITC", 30, "bold"))
    mainloop()