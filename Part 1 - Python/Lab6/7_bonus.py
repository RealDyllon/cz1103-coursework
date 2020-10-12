from sense_hat import SenseHat
from time import sleep
from copy import deepcopy
from datetime import datetime
#
from random import randrange

# ------------------------

# This function checks the pitch value and the x coordinate
# to determine whether to move the marble in the x-direction.
# Similarly, it checks the roll value and y coordinate to
# determine whether to move the marble in the y-direction.

sense = SenseHat()

w = (255, 255, 255)
b = (0, 0, 0)
r = (255, 0, 0)
g = (0, 255, 0)

# --------------

def get_epoch_now():
    return round(datetime.now().timestamp())


has_init = False
target_x = 0
target_y = 0
time_last_reset = get_epoch_now()

def get_board_copy():
    global has_init
    global target_x
    global target_y
    global time_last_reset
    
    new_board = [
        [r, r, r, r, r, r, r, r],
        [r, b, b, b, b, b, b, r],
        [r, b, b, b, b, b, b, r],
        [r, b, b, r, b, b, b, r],
        [r, b, r, r, b, r, b, r],
        [r, b, b, b, b, r, b, r],
        [r, b, b, b, b, r, b, r],
        [r, r, r, r, r, r, r, r]
    ]
    
    
    time_diff = get_epoch_now() - time_last_reset
    
    print(time_diff)
    
    if time_diff >= 10 or not has_init:
        target_x = randrange(1,7)
        target_y = randrange(1,7)
        has_init = True
        time_last_reset = get_epoch_now()
        print("target position reset")
    
    new_board[target_y][target_x] = g
    
    return new_board

def check_wall(x,y,new_x,new_y):
    if board[new_y][new_x] != r:
        return new_x, new_y
    elif board[new_y][x] != r:
        return x, new_y
    elif board[y][new_x] != r:
        return new_x, y
    else:
        return x,y


def move_marble(pitch,roll,x,y):
    new_x = x #assume no change to start with
    new_y = y #assume no change to start with
    if 1 < pitch < 179 and x != 0:
        new_x -= 1 # move left
    elif 359 > pitch > 179 and x != 7:
        new_x += 1 # move right
    if 1 < roll < 179 and y != 7:
        new_y += 1 # move up
    elif 359 > roll > 179 and y != 0:
        new_y -= 1 # move down
        
    new_x,new_y = check_wall(x,y,new_x,new_y)    
        
    return new_x, new_y


# -----------------------

board = get_board_copy()

x = 4
y = 4

game_over = False

while not game_over:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x,y = move_marble(pitch,roll,x,y)
    
    
    
    board = get_board_copy()
    
    if board[y][x] == g:
        game_over = True
        
    board[y][x] = w
    sense.set_pixels(sum(board,[]))
    
    sleep(0.05)
    
print("you win")
sense.show_message("you win!")
    
