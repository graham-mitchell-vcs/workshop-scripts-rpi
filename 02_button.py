import RPi.GPIO as GPIO
import time

led = 18
button = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(button,GPIO.IN, pull_up_down=GPIO.PUD_UP)


def buttonIsPressed(pin):
	if GPIO.input(pin) == False:
		return True
	else:
		return False


try:
	while True:
		while buttonIsPressed(button):
			GPIO.output(led , True)
			time.sleep(1)
		GPIO.output(led , False)
		time.sleep(.125)

except Exception as e:
    GPIO.cleanup()
    print(e)
