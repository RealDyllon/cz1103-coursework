from sense_hat import SenseHat
from random import randint, getrandbits
import time

sense = SenseHat()

B = (0,0,0)
A = (0,255,0)
X = (0,0,255)
R = (255,0,0)

def arrow_image(a,b):
    return [
    b,b,b,b,b,b,b,b,
    b,b,b,a,b,b,b,b,
    b,b,a,a,a,b,b,b,
    b,a,b,a,b,a,b,b,
    b,b,b,a,b,b,b,b,
    b,b,b,a,b,b,b,b,
    b,b,b,a,b,b,b,b,
    b,b,b,b,b,b,b,b,
    ]
    
b = (0,0,0)
c = A
    
smiley = [
    b, b, b, b, b, b, b, b,
    b, c, c, b, b, c, c, b,
    b, c, c, b, b, c, c, b,
    b, b, b, b, b, b, b, b,
    b, b, b, b, b, b, b, b,
    b, c, b, b, b, b, c, b,
    b, c, c, c, c, c, c, b,
    b, b, b, b, b, b, b, b
    ]

angles = [0, 90, 180, 270]

def getAccelDirection():
    X,Y,Z = acceleration = sense.get_accelerometer_raw()
    print(acceleration)
    
    x = acceleration["x"]
    y = acceleration["y"]
    
    if abs(x) < abs(y):
        if y > 0:
            return 0
        else:
            return 180
    else:
        if x > 0:
            return 270
        else:
            return 90
            
time_limit = 1
score = 0

def superimpose_score():
    for i in range(0, score):
        sense.set_pixel(7, i, 255, 0, 255)

while True:
    
    # choose random direction
    angle = angles[randint(0,3)]
    sense.set_rotation(angle)
    sense.set_pixels(arrow_image(X, B))
    superimpose_score()
    
    # wait 1 sec for user input
    time.sleep(time_limit)
    
    # check user input
    
    user_accel = getAccelDirection()
    
    if score > 7:
        break;
    
    if user_accel == angle:
        sense.set_pixels(arrow_image(A,B))
        superimpose_score()
            
        time_limit *= 0.9
        score += 1
        print("score:", score)
    else: 
        sense.set_pixels(arrow_image(R,B))
        score = 0
        time_limit = 1
        print("you lost")
    
    
    # x = acceleration["x"]
    # y = acceleration["y"]
    # z = float(Z)
    
    time.sleep(time_limit)
    
sense.set_rotation(180) # my pi is upside down lol
sense.set_pixels(smiley)
    
    
    
    
   
    
