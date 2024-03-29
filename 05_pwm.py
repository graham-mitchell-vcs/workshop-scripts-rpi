import RPi.GPIO as GPIO
import time

led = 18
steps = 100
delay = 2/steps # seconds to cycle for
GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
p = GPIO.PWM(led, 400)
p.start(0)

try:
	while True:
		for x in range(0,steps):
			p.ChangeDutyCycle(x)
            time.sleep(delay)
		for x in range(steps,0,-1):
			p.ChangeDutyCycle(x)
            time.sleep(delay)

except Exception as e:
	GPIO.cleanup()
    print(e)
