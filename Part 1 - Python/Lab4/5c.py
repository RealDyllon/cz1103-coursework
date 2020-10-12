from sense_hat import SenseHat
from random import randint, getrandbits
import time
#

sense = SenseHat()

print("input colors in r,g,b")


R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
Y = (255,255,0)
b = (63,63,63)

colors = [R, G, B, Y]

def image_pixels(c):
    return [
        b, b, b, b, b, b, b, b,
        b, c, c, b, b, c, c, b,
        b, c, c, b, b, c, c, b,
        b, b, b, b, b, b, b, b,
        b, b, b, b, b, b, b, b,
        b, c, b, b, b, b, c, b,
        b, c, c, c, c, c, c, b,
        b, b, b, b, b, b, b, b
    ]

starttime = time.time()

while True:
    print("tick")
    sense.set_rotation([0, 90, 180, 270][randint(0,3)])
    sense.set_pixels(image_pixels((randint(0,255),randint(0,255),randint(0,255),)))
    
    time.sleep(1)
    sense.clear()



