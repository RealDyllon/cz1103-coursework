from sense_hat import SenseHat

sense = SenseHat()

def get_color(color):
    keep_looping = True
    no_of_try=1
    while keep_looping:
        color_str=input("Enter the value of the " + color + " color for message (0 to 255):")
        color_int = int(color_str)
        if color_int >= 0 and color_int <= 255:
            break

    return color_int
    
   
    
r_int = get_color("red")
g_int = get_color("green")
b_int = get_color("blue")
msg_color = (r_int, g_int, b_int)
sense.show_message("I got it!", text_colour = msg_color)