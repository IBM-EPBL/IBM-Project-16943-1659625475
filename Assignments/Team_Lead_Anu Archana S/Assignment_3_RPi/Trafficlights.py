from gpiozero import Button, TrafficLights
from time import sleep

button=Button(21)
light=TrafficLights(25,8,7)

while true :
    button.wait_for_press()
    light.green.on()
    sleep(1)
    light.amber.on()
    sleep(1)
    light.red.on()
    sleep(1)
    light.off()

