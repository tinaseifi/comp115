import turtle
import random
import time

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("midnight blue")
screen.title("Stars Moon Mountains")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

def jump(x, y):
    t.penup()
    t.goto(x, y)

def filled_circle(cx, cy, r, fill, outline=None):
    jump(cx, cy - r)
    t.pencolor(outline if outline else fill)
    t.fillcolor(fill)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()
    t.penup()

def dot_at(x, y, size, color):
    jump(x, y)
    t.dot(size, color)

def sparkle_at(x, y, size, color):
    jump(x, y)
    t.pencolor(color)
    t.pensize(max(1, size // 6))
    t.pendown()
    for k in range(4):
        t.setheading(90 * k)
        t.forward(size)
        t.backward(size)
    t.penup()

def draw_stars():
    for i in range(260):
        x = random.randint(-440, 440)
        y = random.randint(-290, 290)
        size = random.randint(2, 4)
        color = random.choice(["white", "white", "white", "light yellow", "lemon chiffon"])
        dot_at(x, y, size, color)
        if i % 14 == 0:
            screen.update()
            time.sleep(0.01)

    for i in range(40):
        x = random.randint(-430, 430)
        y = random.randint(-280, 280)
        size = random.randint(8, 14)
        color = random.choice(["white", "lemon chiffon", "light yellow"])
        sparkle_at(x, y, size, color)
        if i % 4 == 0:
            screen.update()
            time.sleep(0.01)

def draw_crescent_moon(cx, cy, r):
    filled_circle(cx, cy, r, "white", "white")
    filled_circle(cx - int(r * 0.45), cy + int(r * 0.10), int(r * 0.95), "midnight blue", "midnight blue")
    for _ in range(10):
        x = cx + random.randint(0, r - 6)
        y = cy + random.randint(-r + 6, r - 6)
        s = random.randint(4, 9)
        dot_at(x, y, s, "gainsboro")

def draw_mountains():
    t.fillcolor("dark slate gray")
    t.pencolor("dark slate gray")
    jump(-450, -150)
    t.pendown()
    t.begin_fill()
    points = [
        (-450, -150),
        (-350, -50),
        (-250, -150),
        (-150, -60),
        (-50, -150),
        (50, -40),
        (150, -150),
        (250, -70),
        (350, -150),
        (450, -90),
        (450, -300),
        (-450, -300)
    ]
    for x, y in points:
        t.goto(x, y)
    t.end_fill()
    t.penup()

    t.fillcolor("black")
    t.pencolor("black")
    jump(-450, -180)
    t.pendown()
    t.begin_fill()
    points2 = [
        (-450, -180),
        (-300, -120),
        (-150, -180),
        (0, -110),
        (150, -180),
        (300, -130),
        (450, -180),
        (450, -300),
        (-450, -300)
    ]
    for x, y in points2:
        t.goto(x, y)
    t.end_fill()
    t.penup()

screen.tracer(1, 0)
draw_stars()
draw_crescent_moon(280, 200, 85)
draw_mountains()
screen.mainloop()

author: Tina_Seifi