#Python code for blinking LED and Traffic lights
from gpiozero import Button,TrafficLights
import time
button=Button(21)
lights=TrafficLights(7,8,25)
while True
   button.wait_for_press()
   lights.red.blink()
   time.sleep(20)
   lights.amber.blink()
   time.sleep(20)
   lights.green.blink()
   time.sleep(20)
   lights.off
     

