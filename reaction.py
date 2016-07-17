from gpiozero import LED, Button
from time import sleep
from random import uniform

led = LED(4)
blue_button = Button(23)
red_button = Button(24)
game_count = input('How many games do you want to play?')
blue_score = 0
red_score = 0
def pressed(button):
	if button.pin.number == 23:
		global blue_score
		blue_score = blue_score + 1
                print('Blue Button Won The Game ' + str(blue_score) + ' Times!')
        else:
		global red_score
		red_score = red_score + 1
	        print('Red Button Won The Game ' + str(red_score) + ' Times!')

for x in xrange(game_count):
        led.on()
        sleep(uniform(2,5))
        led.off()
        blue_button.when_pressed = pressed
        red_button.when_pressed = pressed
        sleep(2)
