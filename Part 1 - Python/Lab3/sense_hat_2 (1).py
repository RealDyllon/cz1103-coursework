import sys
from sense_hat import SenseHat

sense = SenseHat()

sense.set_rotation(180)
# sense.show_message("Hello", text_colour = (255, 255, 0), back_colour = (225, 0, 0), scroll_speed = 0.5)

def kill_script():
    input("you have input invalid data way too many times smh, press enter to kill the script")
    sys.exit()

speed = float(0)
speed_valid = False
speed_invalid_tries = 0
while not speed_valid:
    try:
        speed = float(input("enter the desired speed: "))
    except ValueError:
       print("not a floating number, try again!")
       speed_invalid_tries += 1
       if speed_invalid_tries >= 3:
           kill_script()
       pass
    else:
        if (speed > 0):
            speed_valid = True
            
print("selected speed is ",  str(speed) )

# def func for later
def str_to_int(n):
    return int(n)

def input_rgb(input_string):
    user_color = [-1,-1,-1]
    user_color_valid = False
    user_color_invalid_tries = 0

    while not all(( 0 <= channel <= 255) for channel in user_color):
        try:
            user_color = list(map(str_to_int,(input('enter r,g,b code for {}: '.format(input_string)).split(","))))
        except (TypeError, ValueError):
            print("oops invalid rgb input")
            user_color_invalid_tries ++ 1
            if user_color_invalid_tries >=3:
                kill_script()
        else:
            user_color_valid = True
            
    return user_color
    
text_color = [-1,-1,-1]
bg_color = [-1, -1, -1]
same_colors = True
    
while same_colors:
    text_color = input_rgb("text color")
    bg_color = input_rgb("background color")
    if bg_color == text_color:
        print("same colors!!! how to see??? try again leh.")
        same_colors = True
    else:
        same_colors = False
    
print("displaying msg on senseHAT, with text_color:", text_color, "bg_color:", bg_color,  "and speed", speed)

sense.show_message("This is fun!", text_colour = (text_color),  back_colour = (bg_color), scroll_speed = speed)