import turtle

# Preliminaries
window = turtle.Screen()
window.setup(648,648) # (6**4)/2 so it is "small" but easily divisible by 2 and 3
window.bgcolor("white")
window.title("Ultimate Ultimate Tik Tac Toe")
t = turtle.Turtle()
t.speed(0)

# basically defines the parameters of a tic tac toe board
def board(tlCornerX, tlCornerY, length, size):
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
        t.goto(tlCornerX, tlCornerY - (i * length)/3)
        t.down()
        t.forward(length)
    t.right(90)
    for i in range(1,3):
        t.up()
        t.goto(tlCornerX + (i * length)/3, tlCornerY)
        t.down()
        t.forward(length)
    t.left(90)

# small boards
tlCornerX = -324
tlCornerY = 324
length = 72
size = 1
flip = True
for i in range(9):
    for k in range(9):
        board(tlCornerX, tlCornerY, length, size)
        if flip:
            tlCornerX += length
        else:
            tlCornerX -= length
    tlCornerY -= length
    flip = not(flip)
    if flip:
            tlCornerX += length
    else:
        tlCornerX -= length

# medium boards (i can't be bothered putting this in a for loop because it would be more lines. sue me)
board(108, -108, 216, 3)
board(-108, -108, 216, 3)
board(-324, -108, 216, 3)
board(-324, 108, 216, 3)
board(-108, 108, 216, 3)
board(108, 108, 216, 3)
board(108, 324, 216, 3)
board(-108, 324, 216, 3)
board(-324, 324, 216, 3)

# big board
board(-324, 324, 648, 5)

b = turtle.Turtle()
b.speed(0)
b.up()
b.shape('square')
b.shapesize(288, 288)
b.fillcolor('')

boo = True

def click(x, y):
    global boo
    if x >= 0:
        storex = x
        xSign = 1
    else:
        storex = -1 * x
        xSign = -1
    if y >= 0:
        storey = y
        ySign = 1
    else:
        storey = -1 * y
        ySign = -1
    yc = 400
    xc = 400
    fy = 0
    fx = 0
    for ycoord in range(312, -1, -24):
        y = abs(storey - ycoord) # y = distance between round and actual
        # if that distance between is smaller than prev best distance between
            # set as new best distance between and set current round as final y
        if y < yc:
            yc = y
            fy = ycoord
    for xcoord in range(312, -1, -24):
        x = abs(storex - xcoord)
        if x < xc:
            xc = x
            fx = xcoord
    if boo:
        b.goto((fx * xSign) + 1, (fy * ySign) - 15)
        b.write("o", align="center", font=("Arial", 30, "bold"))
        boo = False
    else:
        b.goto((fx * xSign) + 1, (fy * ySign) - 15)
        b.write("x", align="center", font=("Arial", 30, "bold"))
        boo = True
        

b.onclick(click)

turtle.mainloop()