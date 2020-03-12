from gpiozero import LED

red = LED(22)
red.blink()

red = LED(22)
amber = LED(27)
green = LED(17)

red.blink(1, 1)
amber.blink(2, 2)
green.blink(3, 3)

red.on()
sleep(1)
amber.on()
sleep(1)
green.on()
sleep(1)

while True:
    red.on()
    sleep(1)
    amber.on()
    sleep(1)
    green.on()
    sleep(1)
    red.off()
    sleep(1)
    amber.off()
    sleep(1)
    green.off()

