from gpiozero import LED, Button
from time import sleep
from signal import pause

led = LED(5)
timer_button = Button(19)

timer_button.when_pressed = led.on
timer_button.when_released = led.off

pause()
#def pressed(button):
#	if button.pin.number == 23:
#		global blue_score
#		blue_score = blue_score + 1
#                print('Blue Button Won The Game ' + str(blue_score) + ' Times!')

#for x in xrange(game_count):
#        led.on()
#        sleep(uniform(2,5))
#        led.off()
#        blue_button.when_pressed = pressed
       
