# Claire Delavan
# etc

import turtle

# Make the board
# each of the lower varable is a single, traditional board. each middle is a board full of boards. and the upper board is the master board
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

upper = [middleUpleft, middleUpmid, middleUpright, middleMidleft, middleMidmid, middleMidright, middleLowleft, middleLowmid, middleLowright]

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
    help = []
    for i in range(-13, 14):
        if fx // 24 == i:
            i += 13 # so it is indexed 0-26
            help.append(i)
            break
    for i in range(-13, 14):
        if fy // 24 == i:
            i = abs(i - 13)
            help.append(i)
            break
    if 0 <= help[0] <= 8:
        if 0 <= help[1] <= 8:
            # in upper[6]
            # "coordinate" is: [help[0], help[1], help[4]]
            # put through 3 deep for loop of a 9
                # girl, what did you mean "of a 9"?
                # i think of a 9x9x9
                # but i also think that there is a better solution
                # this sucks and is hard
            pass
        elif 9 <= help[1] <= 17:
            # in upper[3]
            pass
        else:
            # in upper[0]
            pass
    elif 9 <= help[0] <= 17:
        if 0 <= help[1] <= 8:
            # in upper[7]
            pass
        elif 9 <= help[1] <= 17:
            # in upper[4]
            pass
        else:
            # in upper[1]
            pass
    else:
        if 0 <= help[1] <= 8:
            # in upper[8]
            pass
        elif 9 <= help[1] <= 17:
            # in upper[5]
            pass
        else:
            # in upper[2]
            pass
    # put what is shown above into for loop
    # then, now that it is in a l*w*h kinda situation (more like l*h*w), use that coordinate to map to a position in a lower board
    # upper[help[4]][help[7]][help[8]]
    # to check, print that through upper[][][] (i think that is the right amount of braces) and print each number to make sure it's going to correct spot
    # hopefully this will work and i will sing kumbaya with my code (or how ever you spell it)
    for i in range(3):
        if 9 * i <= help[0] <= (9 * (i+1)) - 1:
            help.append(i)
            for k in range(3):
                if 9 * k <= help[1] <= (9 * (k+1)) - 1:
                    help.append(k)
                    help.append(help[2] + (help[3] * 3))
    for i in range(9):
        if 3 * i <= help[0] <= (3 * (i+1)) - 1:
            help.append(i)
            for k in range(9):
                if 3 * k <= help[1] <= (3 * (k+1)) - 1:
                    help.append(k)
                    help.append(((help[5] % 3) + (help[6] * 3)) % 9)
    help.append(((help[0] % 3) + (help[1] * 3)) % 9)
    ### need to fix the fact that you can click again. will need to happen after can read from array correctly ###
    ### will need to do that for each layer but instead of being able to draw for upper layers, not being able to send there ###
    if upper[help[4]][help[7]][help[8]] == "-":
        if boo:
            upper[help[4]][help[7]][help[8]] = "o"
            b.goto(fx + 1, fy - 15) # goes to confirmed best place (the +1 and -15 are just what i found to be the actual correct center)
            b.write("o", align="center", font=("Arial", 30, "bold")) # prints character
            boo = False # filps turn
        # same for "x"
        else:
            upper[help[4]][help[7]][help[8]] = "x"
            b.goto(fx + 1, fy - 15)
            b.write("x", align="center", font=("Arial", 30, "bold"))
            boo = True

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
