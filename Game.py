import turtle as t
import pygame
import random as r

pygame.mixer.init()
bgsound = pygame.mixer.Sound("sound/antarctic.mp3")

img = 'image/penguin2.gif'
fish = 'image/fish2.gif'
shelter = 'image/shelter2.gif'
t.setup(700, 700)
t.title("북극탐험")

t.addshape(img)
t.addshape(fish)
t.addshape(shelter)

t.up()
t.hideturtle()

def draw_rect(x, y, w, h, color):
    bg = t.Turtle()
    bg.speed(0)
    bg.up()
    bg.goto(x, y)
    bg.down()
    bg.color(color)
    bg.begin_fill()
    bg.forward(w)
    bg.setheading(90)
    bg.forward(h)
    bg.setheading(180)
    bg.forward(w)
    bg.setheading(270)
    bg.forward(h)
    bg.end_fill()
    bg.hideturtle()
    del bg

def draw_triangle(x, y, w):
    bg = t.Turtle()
    bg.speed(0)
    bg.up()
    bg.goto(x, y)
    bg.down()
    bg.color("blue")
    bg.begin_fill()
    bg.forward(w)
    bg.setheading(240)
    bg.forward(2*w)
    bg.setheading(90)
    bg.forward(1.733*w)
    bg.end_fill()
    del bg
    
def draw_circle(x, y, r):
    bg = t.Turtle()
    bg.speed(0)
    bg.up()
    bg.goto(x, y)
    bg.down()
    bg.color("white")
    bg.begin_fill()
    bg.circle(r)
    bg.end_fill()
    bg.hideturtle()
    del bg

draw_rect(-350, 120, 700, 230, 'skyblue')
draw_triangle(-350, 120, 230)
draw_rect(-330, 120, 180, 20, 'white')

for x in range(7):
    draw_rect(130+25*x, 80-50*x, 200, 30, 'lightgray')

def draw_cloud(x, y):
    for i in range(5):
        draw_circle(x+15*i, y, 10)
    
draw_cloud(240, 270)
draw_cloud(40, 300)
draw_cloud(-250, 240)

tc = t.Turtle()
tc.hideturtle()
tc.shape(shelter)

playing = False
score = 0
clear = 0

penguin = t.Turtle()
penguin.hideturtle()
penguin.shape(img)

penguin.up()
penguin.goto(0, -250)
penguin.showturtle()

def moveL():
    if penguin.pos() == (0, -250):
        penguin.goto(-180, -250)
    if penguin.pos() == (180, -250):
        penguin.goto(0, -250)
def moveR():
    if penguin.pos() == (0, -250):
        penguin.goto(180, -250)
    if penguin.pos() == (-180, -250):
        penguin.goto(0, -250)
    
def play():
    global playing
    global score
    global clear
    global tc
    
    tc.hideturtle()
    
    loop = True
    
    idx = r.randint(1, 9)
    if idx == 1 or idx == 2:
        te = t.Turtle()
        te.hideturtle()
        te.shape('circle')
        te.color('dimgray')
        te.speed(2)
        te.up()
        te.goto(-50,100)
        te.showturtle() 
        te.setheading(250)
        for x in range(7):
            te.shapesize(x+1, x+1, 1)
            for x in range(8):
                te.forward(10)
                if penguin.distance(te)<30:
                    showmsg("Game Over", "score : " + str(score))
                    playing = False
                    bgsound.stop()
                    score = 0
                    clear = 0
                    loop = False
                    break
            if loop == False:
                break
        score += 1
        clear += 1
        te.hideturtle()
        del te
        
    if idx == 3 or idx == 4:
        te = t.Turtle()
        te.hideturtle()
        te.shape('circle')
        te.color('dimgray')
        te.speed(2)
        te.up()
        te.goto(0,100)
        te.showturtle()
        te.setheading(270)
        for x in range(7):
            te.shapesize(x+1, x+1, 1)
            for x in range(8):
                te.forward(10)
                if penguin.distance(te)<30:
                    showmsg("Game Over", "score : " + str(score))
                    playing = False
                    bgsound.stop()
                    score = 0
                    clear = 0
                    loop = False
                    break
            if loop == False:
                break
        score += 1
        clear += 1
        te.hideturtle()
        del te
        
    if idx == 5 or idx == 6:
        te = t.Turtle()
        te.hideturtle()
        te.shape('circle')
        te.color('dimgray')
        te.speed(2)
        te.up()
        te.goto(50,100)
        te.showturtle()
        te.setheading(290)
        for x in range(7):
            te.shapesize(x+1, x+1, 1)
            for x in range(8):
                te.forward(10)
                if penguin.distance(te)<30:
                    showmsg("Game Over", "score : " + str(score))
                    playing = False
                    bgsound.stop()
                    score = 0
                    clear = 0
                    loop = False
                    break
            if loop == False:
                break
        score += 1
        clear += 1
        te.hideturtle()
        del te
    
    if idx == 7:
        te = t.Turtle()
        te.hideturtle()
        te.shape(fish)
        te.speed(2)
        te.up()
        te.goto(-50,100)
        te.showturtle()
        te.setheading(250)
        for x in range(7):
            te.shapesize(x+1, x+1, 1)
            for x in range(8):
                te.forward(10)
                if penguin.distance(te)<26:
                    score += 1
                    te.hideturtle()
        clear += 1
        del te
        
    if idx == 8:
        te = t.Turtle()
        te.hideturtle()
        te.shape(fish)
        te.speed(2)
        te.up()
        te.goto(0,100)
        te.showturtle()
        te.setheading(270)
        for x in range(7):
            te.shapesize(x+1, x+1, 1)
            for x in range(8):
                te.forward(10)
                if penguin.distance(te)<30:
                    score += 1
                    te.hideturtle()
        clear += 1
        del te
    
    if idx == 9:
        te = t.Turtle()
        te.hideturtle()
        te.shape(fish)
        te.speed(2)
        te.up()
        te.goto(50,100)
        te.showturtle()
        te.setheading(290)
        for x in range(7):
            te.shapesize(x+1, x+1, 1)
            for x in range(8):
                te.forward(10)
                if penguin.distance(te)<26:
                    score += 1
                    te.hideturtle()
        clear += 1
        del te
    
    if clear == 20:
        tc.speed(2)
        tc.up()
        tc.goto(20,130)
        tc.showturtle()
        showmsg("Clear", "score : " + str(score))
        playing = False
        bgsound.stop()
        score = 0
        clear = 0
        
    if playing:
        t.ontimer(play, 100)

def showmsg(msg1, msg2):
    t.clear()
    t.goto(0, 200)
    t.write(msg1, False, "center", ("", 30, "bold"))
    t.goto(0, -150)
    t.write(msg2, False, "center", ("", 20))
    t.home()

def start():
    global playing
    if playing == False:
        playing = True
        t.clear()
        bgsound.play()
        play()

t.onkeypress(start, "space")
t.onkeypress(moveL, "Left")
t.onkeypress(moveR, "Right")
t.listen()
showmsg("북극탐험", "[ Space for Start ]")

t.done()