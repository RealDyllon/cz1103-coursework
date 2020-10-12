from sense_hat import SenseHat
from random import randint
import time
#

sense = SenseHat()

print("input colors in r,g,b")
colors = [
(255,0,0),
(0,255,0),
(0,0,255),
(255,255,0)
# O = (0,0,0)
]

starttime = time.time()
while True:
    print("tick")
    sense.clear()
    
    for color in colors:
        sense.set_pixel(randint(0,7), randint(0,7), color)
    
    time.sleep(1)
    



