import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

GPIO.setmode(GPIO.BOARD)

image = [ 	[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
		]

cpins = [ [3,5,7], [8,10,12], [11,13,15], [16,18,22], [19,21,23] ]
rpins = [ 32, 36, 38, 40 ]

r = [1,0,0]
y = [1,1,0]
g = [0,1,0]
c = [0,1,1]
b = [0,0,1]
v = [1,0,1]
w = [1,1,1]
colorlist = [r,y,w,g,c,b,v]

offsleep = 0
kill = False

for set in cpins:
	for pin in set:
		GPIO.setup(pin, GPIO.OUT)

for pin in rpins:
	GPIO.setup(pin, GPIO.OUT)
	

# set all pins low
for pin in rpins:
	GPIO.output(pin, GPIO.LOW)

	
def display():
	while True:
		if kill == True: exit()
		for r in range(len(rpins)):
			for s in range(len(cpins)): # set
				for p in range(len(cpins[0])):	# pin
					if image[r][s][p] == 1:
						GPIO.output(cpins[s][p], 1)
					else: GPIO.output(cpins[s][p], 0)
						
			GPIO.output(rpins[r], GPIO.HIGH)
			sleep(.0001)
			GPIO.output(rpins[r], GPIO.LOW)
			sleep(offsleep)

def left():
	hold = []
	for i in range(len(image)):
		for x in range(len(image[0])):
			if x == 0:
				hold.append(image[i][x])
			else:
				image[i][x-1] = image[i][x]
	for i in range(len(hold)):
		image[i][4] = hold[i]
		
def right():
	hold = []
	for i in range(len(image)):
		for x in range(len(image[0])):
			if 4-x == 4:
				hold.append(image[i][4-x])
			else:
				image[i][4-x+1] = image[i][4-x]
	for i in range(len(hold)):
		image[i][0] = hold[i]
		
def displist():
	for color in colorlist:
		for r in range(len(image)):
			for c in range(len(image[0])):
				image[r][c] = color
		sleep(2)

def brightness(val):
	global offsleep
	offsleep = val
	
def fullraise():
	global offsleep
	step = .0001
	
	while offsleep >= 0+step:
		offsleep = offsleep - step
		sleep(.01)
		
def fulldrop():
	global offsleep
	step = .0001
	
	while offsleep <= .009:
		offsleep = offsleep + step
		sleep(.01)
	
def lower():
	pass
	
def rainbow():
	for x in range(len(image)):
		for z in range(len(image[0])):
			if z == 0: image[x][z] = r 
			elif z == 1: image[x][z] = y
			elif z == 2: image[x][z] = g
			elif z == 3: image[x][z] = c
			else: image[x][z] = b

def colorall():
	color = input('\tcolor(r,y,g,c,b,w): ')
	
				
	
			
image2 = [ 	[[1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
			[[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 0, 0], [1, 0, 1]],
			[[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 0, 1]],
			[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
		]	
image = image2

mythread = Thread(target=display)
mythread.start()

while True:
	uin = raw_input('> ')
	if uin == 'exit':
		kill = True
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
		colorall():