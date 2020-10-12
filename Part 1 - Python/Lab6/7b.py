from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

b = (128, 0, 0)
w = (255, 255, 255)

board = [
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b],
    [b, b, b, b, b, b, b, b]
    ]
    
x = 2
y = 2

board[x][y] = w

sense.set_pixels(sum(board, []))

    