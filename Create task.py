# Claire Delavan
# CSCI 101 Section F
# Create Project
# References: Caitlin giving me ideas on how to make it easier from a user end and Maggie for suggesting that i could just use turtle instead of worrying about pygame
# Time: idk like 2 minutes probably

import turtle

# Make the board
# each of the lower varable is a single, traditional board. each middle is a board full of boards. and the upper board is the master board
# additionally, the "Board" things are for testing for wins because it will be a lot easier to do it this way
lowerUpleftUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpleftLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleUpleft = [lowerUpleftUpleft, lowerUpleftUpmid, lowerUpleftUpright, lowerUpleftMidleft, lowerUpleftMidmid, lowerUpleftMidright, lowerUpleftLowleft, lowerUpleftLowmid, lowerUpleftLowright]
middleUpleftBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerUpmidUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUpmidLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleUpmid = [lowerUpmidUpleft, lowerUpmidUpmid, lowerUpmidUpright, lowerUpmidMidleft, lowerUpmidMidmid, lowerUpmidMidright, lowerUpmidLowleft, lowerUpmidLowmid, lowerUpmidLowright]
middleUpmidBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerUprightUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerUprightLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleUpright = [lowerUprightUpleft, lowerUprightUpmid, lowerUprightUpright, lowerUprightMidleft, lowerUprightMidmid, lowerUprightMidright, lowerUprightLowleft, lowerUprightLowmid, lowerUprightLowright]
middleUprightBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerMidleftUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidleftLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleMidleft = [lowerMidleftUpleft, lowerMidleftUpmid, lowerMidleftUpright, lowerMidleftMidleft, lowerMidleftMidmid, lowerMidleftMidright, lowerMidleftLowleft, lowerMidleftLowmid, lowerMidleftLowright]
middleMidleftBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerMidmidUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidmidLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleMidmid = [lowerMidmidUpleft, lowerMidmidUpmid, lowerMidmidUpright, lowerMidmidMidleft, lowerMidmidMidmid, lowerMidmidMidright, lowerMidmidLowleft, lowerMidmidLowmid, lowerMidmidLowright]
middleMidmidBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerMidrightUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerMidrightLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleMidright = [lowerMidrightUpleft, lowerMidrightUpmid, lowerMidrightUpright, lowerMidrightMidleft, lowerMidrightMidmid, lowerMidrightMidright, lowerMidrightLowleft, lowerMidrightLowmid, lowerMidrightLowright]
middleMidrightBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerLowleftUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowleftLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleLowleft = [lowerLowleftUpleft, lowerLowleftUpmid, lowerLowleftUpright, lowerLowleftMidleft, lowerLowleftMidmid, lowerLowleftMidright, lowerLowleftLowleft, lowerLowleftLowmid, lowerLowleftLowright]
middleLowleftBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerLowmidUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowmidLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleLowmid = [lowerLowmidUpleft, lowerLowmidUpmid, lowerLowmidUpright, lowerLowmidMidleft, lowerLowmidMidmid, lowerLowmidMidright, lowerLowmidLowleft, lowerLowmidLowmid, lowerLowmidLowright]
middleLowmidBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

lowerLowrightUpleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightUpmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightUpright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightMidleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightMidmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightMidright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightLowleft = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightLowmid = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
lowerLowrightLowright = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

middleLowright = [lowerLowrightUpleft, lowerLowrightUpmid, lowerLowrightUpright, lowerLowrightMidleft, lowerLowrightMidmid, lowerLowrightMidright, lowerLowrightLowleft, lowerLowrightLowmid, lowerLowrightLowright]
middleLowrightBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

upper = [middleUpleft, middleUpmid, middleUpright, middleMidleft, middleMidmid, middleMidright, middleLowleft, middleLowmid, middleLowright]
upperBoard = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

print("Welcome to Ultimate Ultimate Tic Tac Toe!")
while True:
	print("If you don't know how to play this game or have never heard of it, input \"R\" to see the rules.")
	print("If you are ready to play, input \"P\".")
	selection = input("Input: ")
	selection = selection.lower()
	if selection == "p" or selection == "r":
		break
	else:
		print("Please input one of the chioces.")
if selection == "r":
	print("\nRules:")
	print("If you have ever played Ultimate Tic Tac Toe you might be able to get the gist of what Ultimate Ultimate Tic Tac Toe is. However, for the uninitiated, it is easier to explain what Ultimate Tic Tac Toe is first:")
	print("\nIn Ultimate Tic Tac Toe there is essentially 2 layers of Tic Tac Toe boards. A larger one, and a board inside each square of that larger board. To win, you must create a line on the large board and you do that by winning 3 of the smaller boards. When you win a smaller board, your icon (X or O) goes up a layer, being placed in the square that that board you just won was on. However, there is another rule to Ultimate Tic Tac Toe that makes the board layers interact with eachother. Lets say you start the game by placing an X in the top middle space in the inner board and in the board that is in the middle space of the upper board. The other player would then be required to play in the board that is on the upper middle square of the upper layer board. The only times you aren't held to that rule is the first move of the game and when the redirection would bring you to a square that either has been won, or ended in a cat game. In either of those events, you my choose any open square to play in.")
	print("\nNow, the step to Ultimate Ultimate Tic Tac Toe is fairly simple to understand. There is an Ultimate Tic Tac Toe board put into each square of another higher layer board. The last nuance to understand with this jump is how this new layer can be interacted with from the lower layers. The low layer can only effect the middle layer, and the middle layer can effect the upper layer (in terms of which square will be played in next).")
	print("\nI hope you enjoy the game experience!")
	print("\nNow, input \"P\" once you are ready to play!")
	while True:
		selection = input("Input: ")
		selection = selection.lower()
		if selection == "p":
			break
		else:
			print("Please input \"P\" when ready.")
# build board
# Preliminaries
window = turtle.Screen()
window.setup(648,648) # (6**4)/2 so it is "small" but easily divisible by 2 and 3 a lot
window.bgcolor("white")
window.title("Ultimate Ultimate Tik Tac Toe")
t = turtle.Turtle()
t.speed(0) # speeeeeeeeeeeeed

# basically defines the parameters of a tic tac toe board
def board(tlCornerX, tlCornerY, length, size):
    t.ht()
    t.width(size)
    # uses the size variable to decide what color to make the line (darker for wider)
    if size == 1:
        t.pencolor("darkgrey")
    elif size == 3:
        t.pencolor("slategrey")
    else:
        t.pencolor("black")
    # draws the 2 horizontal lines
    for i in range(1,3):
        t.up()
        t.goto(tlCornerX, tlCornerY - (i * length)/3)
        t.down()
        t.forward(length)
    t.right(90) # prepares for other directio
    # draws the 2 vertical lines
    for i in range(1,3):
        t.up()
        t.goto(tlCornerX + (i * length)/3, tlCornerY)
        t.down()
        t.forward(length)
    t.left(90) # sets the rotation back to starting

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

# accept input
# make button turtle
b = turtle.Turtle()
b.speed(0)
b.up()
b.shape('square')
b.shapesize(288, 288) # more than twice the size of the screen so you can always click on either side of the board
b.fillcolor('') # makes it clear so it's just a mask above the board. kinda like just making it a touch screen

boo = True # turn tracker (boo for boolean)

def click(x, y): # I think this will have to be like, the rest of my code. because ideally it does all of the checking and logic right after the click and I don't know how to do that with like, being in the mainloop thing.
    global boo # apparently, you can actually use global variables in functions
	# makes each coordinate in the 1st quadrent but stores it's sign to reapply later
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
	# the c variables are for testing the distance between round and actual
    yc = 400
    xc = 400
	# what will be eventually used as the final round variables
    fy = 0
    fx = 0
    for ycoord in range(312, -1, -24): # highest center, lowest center -1 (so it can count 0), size of square
        y = abs(storey - ycoord) # distance from click
        if y < yc: # if it is lower, it has improved
            yc = y # store new best
            fy = ycoord # store new most correct rounded value
	# basically the same but for x
    for xcoord in range(312, -1, -24):
        x = abs(storex - xcoord)
        if x < xc:
            xc = x
            fx = xcoord
	# "o" will be first in my game because i believe on a spiritual level that it should be first
    fx = fx * xSign
    fy = fy * ySign
    # find where it is in terms of the array
    help = [] # where i will be storing a ton of helpful values that will be used later down the line
    for i in range(-13, 14):
        if fx // 24 == i:
            i += 13 # so it is indexed 0-26
            help.append(i) # x coordinate indexed 0-26
            break
    for i in range(-13, 14):
        if fy // 24 == i:
            i = abs(i - 13) # if i added 13 my (0,0) corner would be bottom left and i want it to be top left so i do it like this
            help.append(i) # y coordinate indexed 0-26
            break
    for i in range(3):
        if 9 * i <= help[0] <= (9 * (i+1)) - 1:
            help.append(i) # x coordinate indexed 0-2
            for k in range(3):
                if 9 * k <= help[1] <= (9 * (k+1)) - 1:
                    help.append(k) # y coordinate indexed 0-2
                    help.append(help[2] + (help[3] * 3)) # index in upper board (variable upper) that the click is in aka which mid board it is in
    for i in range(9):
        if 3 * i <= help[0] <= (3 * (i+1)) - 1:
            help.append(i) # x coordinate indexed 0-8
            for k in range(9):
                if 3 * k <= help[1] <= (3 * (k+1)) - 1:
                    help.append(k) # y coordinate indexed 0-8
                    help.append(((help[5] % 3) + (help[6] * 3)) % 9) # index of mid board aka which lower board it is in
    help.append(((help[0] % 3) + (help[1] * 3)) % 9) # index of the lower board (all the way down to the correct square in array form! woo!)
    ### need to fix the fact that you can click again. will need to happen after can read from array correctly ### (done but keeping here until done with lower thing)
    ### will need to do that for each layer but instead of being able to draw for upper layers, not being able to send there ###
    if upper[help[4]][help[7]][help[8]] == "-":
        if boo:
            upper[help[4]][help[7]][help[8]] = "o"
            b.goto(fx + 1, fy - 15) # goes to confirmed best place (the +1 and -15 are just what i found to be the actual correct center in terms of how the letter is "typed")
            b.write("o", align="center", font=("Arial", 30, "bold")) # prints character
            boo = False # filps turn
        # same for "x"
        else:
            upper[help[4]][help[7]][help[8]] = "x"
            b.goto(fx + 1, fy - 15)
            b.write("x", align="center", font=("Arial", 30, "bold"))
            boo = True
    # check if checking for a win is needed


b.onclick(click)

turtle.mainloop() # i think this is some sort of a loop for turtle. whatever, it works
# Then it will check if there are 3 characters in that board
	# if so, check each combination for a win
		# if there is a win, fill the square
		# also, check if there are 3 squares on that layer of board
			# if there are, check for win
				# if there is a win, fill the square
				# check if there are 3 squares on the upper board
					# if there are, check for win
					# if there is win, exit and make a new turtle window displaying winner information
	# else, continue
# Now, do logic defining where the next player will have to play
# Do this by taking the index of the lower board that was played on and sending the other player to that index on the middle board
# if that isn't an acceptable square, send user to middle level and accept 2 inputs
	# if that isn't an acceptable square, send to upper layer and accept 3 inputs (which, this goes for all layers, there needs to be a check for if the layer selected is allowed)
# examples on unplayable boards are either boards that are won or boards that ended in a cat game
    # also, just to be sure, also don't want someone to be able to play on a board lower than a board that has been won. just as redundancy
