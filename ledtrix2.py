from time import sleep
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
n = [0,0,0]
colorlist = [r,y,w,g,c,b,v,r]
colordict = {
				'r': r,
				'y': y,
				'g': g,
				'c': c,
				'b': b,
				'v': v,
				'w': w
			}		
			

	
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
def runleft():
	wait = float(raw_input('wait(sec): '))
	count = int(raw_input('# of times: '))
	for i in range(count):
		left()
		sleep(wait)
		
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
def runright():
	wait = float(raw_input('wait(sec): '))
	count = int(raw_input('# of times: '))
	for i in range(count):
		right()
		sleep(wait)
		
def displist():
	for color in colorlist:
		for r in range(len(imagebuf)):
			for c in range(len(imagebuf[0])):
				imagebuf[r][c] = color
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


def colorall():
	thiscolor = raw_input('\tcolor(r,y,g,c,b,w): ')
	print(thiscolor)
	for row in range(len(imagebuf)):
		for led in range(len(imagebuf[0])):
			imagebuf[row][led] = colordict[thiscolor]
	
def closeall():
	thegrid.kill = True
	exit()

def pickbright():
	newval = float(raw_input('new val: '))
	brightness(newval)
	

def diagbow():
	
	xlen = len(imagebuf[0])
	ylen = len(imagebuf)
	
	for y in range(ylen):
		for x in range(xlen):
			for i in range(-4, 5):
			
				if y == x + i:
					imagebuf[ylen-y-1][x] = colorlist[i+4]


def flash():
	global imagebuf
	thegrid.image = imagebuf
	count = int(raw_input('# of times: '))
	on = float(raw_input('time on(sec): '))
	off = float(raw_input('time off(sec): '))

	imagebufholder = imagebuf[:]
	blankboard = [	[n,n,n,n,n],
					[n,n,n,n,n],
					[n,n,n,n,n],
					[n,n,n,n,n]]
	
	for i in range(count):
		thegrid.image = blankboard
		sleep(off)
		thegrid.image = imagebufholder
		sleep(on)
	
				



thegrid = Lightgrid()				
			
image2 = [ 	[[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1]],
			[[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
		]	
imagebuf = image2

thegrid.image = imagebuf


opts = {
			'exit'		:closeall,
			'left'		:left,
			'right'		:right,
			'displist'	:displist,
			'bright'	:pickbright,
			'raise'		:fullraise,
			'drop'		:fulldrop,
			'rainbow'	:rainbow,
			'colorall'	:colorall,
			'diagbow'	:diagbow,
			'flash'		:flash,
			'runright'	:runright,
			'runleft'	:runleft
		}

		
while True:
	userin = raw_input('> ')
	if userin in opts:
		opts[userin]()

