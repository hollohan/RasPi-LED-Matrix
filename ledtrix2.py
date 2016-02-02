from time import sleep
from threading import Thread
from lightgrid import Lightgrid


imagebuf = [ 	[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
				[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
				[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
				[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
		]

# declare some colors		
r = [1,0,0]
y = [1,1,0]
g = [0,1,0]
c = [0,1,1]
b = [0,0,1]
v = [1,0,1]
w = [1,1,1]
colorlist = [r,y,w,g,c,b,v]
colordict = {
				'r': r,
				'y': y,
				'g': g,
				'c': c,
				'b': b,
				'v': v,
				'w': w
			}		
			


def postimg():
	thegrid.image = imagebuf
	
def left():
	hold = []
	for i in range(len(imagebuf)):
		for x in range(len(imagebuf[0])):
			if x == 0:
				hold.append(imagebuf[i][x])
			else:
				imagebuf[i][x-1] = imagebuf[i][x]
	for i in range(len(hold)):
		imagebuf[i][4] = hold[i]
	postimg()
		
def right():
	hold = []
	for i in range(len(imagebuf)):
		for x in range(len(imagebuf[0])):
			if 4-x == 4:
				hold.append(imagebuf[i][4-x])
			else:
				imagebuf[i][4-x+1] = imagebuf[i][4-x]
	for i in range(len(hold)):
		imagebuf[i][0] = hold[i]
	postimg()
		
def displist():
	for color in colorlist:
		for r in range(len(imagebuf)):
			for c in range(len(imagebuf[0])):
				imagebuf[r][c] = color
		postimg()
		sleep(2)
	
def brightness(val):
	thegrid.offsleep = val
	
def fullraise():
	step = .0001
	
	while thegrid.offsleep >= 0+step:
		thegrid.offsleep -= step
		sleep(.01)
	
	
def fulldrop():
	step = .0001
	
	while thegrid.offsleep <= .009:
		thegrid.offsleep += step
		sleep(.01)

		
def rainbow():
	for x in range(len(imagebuf)):
		for z in range(len(imagebuf[0])):
			if z == 0: imagebuf[x][z] = r 
			elif z == 1: imagebuf[x][z] = y
			elif z == 2: imagebuf[x][z] = g
			elif z == 3: imagebuf[x][z] = c
			else: imagebuf[x][z] = b
	postimg()

'''
def colorall():
	thiscolor = input('\tcolor(r,y,g,c,b,w): ')
	print(thiscolor)
	for row in range(len(imagebuf)):
		for led in range(len(imagebuf[0])):
			imagebuf[row][led] = colordict[thiscolor]
	postimg()
'''	
				



thegrid = Lightgrid()				
			
image2 = [ 	[[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1]],
			[[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
		]	
imagebuf = image2
postimg()

while True:
	uin = raw_input('> ')
	if uin == 'exit':
		thegrid.kill = True
		exit()
	if uin =='left':
		left()
	if uin =='right':
		right()
	if uin =='displist':
		displist()
	if uin == 'bright':
		newval = float(raw_input('new val: '))
		brightness(newval)
	if uin == 'raise':
		fullraise()
	if uin == 'drop':
		fulldrop()
	if uin == 'rainbow':
		rainbow()
	if uin == 'colorall':
		colorall()