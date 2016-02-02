# constantly updates GPIO with image

import RPi.GPIO as GPIO
from time import sleep
import threading


class Lightgrid(threading.Thread):

	offsleep = 0
	kill = False

	image = [ 	[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
				[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
				[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],
				[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
			]
	cpins = [ [3,5,7], [8,10,12], [11,13,15], [16,18,22], [19,21,23] ]
	rpins = [ 32, 36, 38, 40 ]
	
	
	def __init__(self):
		threading.Thread.__init__(self)

		GPIO.setmode(GPIO.BOARD)
		
		# set all col pins for output
		for set in self.cpins:
			for pin in set:
				GPIO.setup(pin, GPIO.OUT)
				
		# set all row pins for output
		for pin in self.rpins:
			GPIO.setup(pin, GPIO.OUT)
			
		# set all pins low
		for pin in self.rpins:
			GPIO.output(pin, GPIO.LOW)
				
		self.start()
	
	
	
	# sets GPIO pins accordingly
	def run(self):
		while True:
			if self.kill: exit()
			
			for r in range(len(self.rpins)):
				for s in range(len(self.cpins)): # set
					for p in range(len(self.cpins[0])):	# pin
					
						if self.image[r][s][p] == 1:
							GPIO.output(self.cpins[s][p], 1)
						else: GPIO.output(self.cpins[s][p], 0)
				
				# sleep and offsleep can be used here for soft PWM				
				GPIO.output(self.rpins[r], GPIO.HIGH)
				sleep(.0001)
				GPIO.output(self.rpins[r], GPIO.LOW)
				sleep(self.offsleep)