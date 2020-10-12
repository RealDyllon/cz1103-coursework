from sense_hat import SenseHat
from random import randint, randrange, getrandbits
import time
#

sense = SenseHat()

print("input colors in r,g,b")


R = (255,0,0)
G = (0,255,0)
B = (0,0,255)
Y = (255,255,0)
b = (255,0,255)

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

flag = True

while True:
    print("tick")
    if flag:
    # sense.set_rotation([0, 90, 180, 270][randint(0,3)])
    # sense.set_pixels(image_pixels(colors[randrange(1, 4, 2)]))
    
        sense.set_rotation(0)
        sense.set_pixels(image_pixels(G))
    else:
        sense.set_rotation(180)
        sense.set_pixels(image_pixels(Y))
        
    flag = not flag
    
    time.sleep(1)
    sense.clear()



