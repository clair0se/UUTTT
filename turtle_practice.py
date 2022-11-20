import turtle

window = turtle.Screen()
window.setup(648,648)
window.bgcolor("white")
window.title("Turtle")
t = turtle.Turtle()
t.speed(10)

def board(tlCornerX, tlCornerY, len, size):
    t.ht()
    t.width(size)
    if size == 1:
        t.pencolor("darkgrey")
    elif size == 3:
        t.pencolor("slategrey")
    else:
        t.pencolor("black")
    for i in range(1,3):
        t.up()
        t.goto(tlCornerX, tlCornerY - (i * len)/3)
        t.down()
        t.forward(len)
    t.right(90)
    for i in range(1,3):
        t.up()
        t.goto(tlCornerX + (i * len)/3, tlCornerY)
        t.down()
        t.forward(len)
    t.left(90)
tlCornerX = -324
tlCornerY = 324
len = 72
size = 1
flip = True
for i in range(9):
    for k in range(9):
        board(tlCornerX, tlCornerY, len, size)
        if flip:
            tlCornerX += len
        else:
            tlCornerX -= len
    tlCornerY -= len
    flip = not(flip)
    if flip:
            tlCornerX += len
    else:
        tlCornerX -= len

board(108, -108, 216, 3)
board(-108, -108, 216, 3)
board(-324, -108, 216, 3)
board(-324, 108, 216, 3)
board(-108, 108, 216, 3)
board(108, 108, 216, 3)
board(108, 324, 216, 3)
board(-108, 324, 216, 3)
board(-324, 324, 216, 3)
board(-324, 324, 648, 5)
turtle.done()