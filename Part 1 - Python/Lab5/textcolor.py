def get_color(color):
    keep_looping = True
    no_of_try=1
    while keep_looping:
        color_str=input("Enter the value of the " + color + " color for message (0 to 255):")
        color_int = int(color_str)
        if color_int >= 0 and color_int <= 255:
            break
        else:
            print("your number is out of the range 0-255")

    return color_int