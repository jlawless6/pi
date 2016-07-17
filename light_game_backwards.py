#import libraries
import RPi.GPIO as GPIO, random, time

#set variables
switchR = 26	#red switch
switchB = 19	#blue switch
ledR = 13	#led lead 1 (red)
ledG = 6	#led lead 2 (green)
ledB = 5	#led lead 3 (blue)

#initialize GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(switchR, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(switchB, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup([ledR,ledG,ledB], GPIO.OUT)

#define a function to monitor switches
def monitorSwitches(seconds):
	#loop for specified time, checking for switch press
	timeEnd = time.time() + seconds
	while time.time() < timeEnd:
		if GPIO.input(switchR) == True:
			return announceWinner(switchR)
		if GPIO.input(switchB) == True:
			return announceWinner(switchB)
	return False

#define a function to announce the winner
def announceWinner(switch):
	#determine which switch was pressed first
	firstBtn = ledR if switch == switchR else ledB
	lastBtn = ledB if switch == switchR else ledR
	#determine which player won
	winner = lastBtn if ledColor == ledG else lastBtn
	#turn off active color and flash winning color
	GPIO.output(ledColor,False)
	for i in range(0,5):
		GPIO.output(winner,True)
		time.sleep(0.5)
		GPIO.output(winner,False)
		time.sleep(0.5)

#play the game, loop until a switch is pressed
winner = False
while winner == False:
	#select random LED color
	ledColor = random.choice([ledR,ledG,ledB])
	#play through one color cycle
	GPIO.output(ledColor, True)	#turn on LED
	winner = monitorSwitches(5)	#monitor switches
	GPIO.output(ledColor, False)	#turn off LED

GPIO.cleanup()
