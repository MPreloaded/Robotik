import RPi.GPIO as GPIO
import time
     
delay = 0.000001
     
GPIO.setmode(GPIO.BCM)

# GPIOs for color management. 1 are the 8 rows on the top, 2 8 rows on the bottom
red1_pin = 17
green1_pin = 18
blue1_pin = 22
red2_pin = 23
green2_pin = 24
blue2_pin = 25

# GPIO for the clock. Needed to change the column
clock_pin = 3

# GPIO for row management. a is 1, b is 2, c is 4 (remember: binary)
a_pin = 7
b_pin = 8
c_pin = 9

# GPIO for the latch. Needed to change the row
latch_pin = 4

# GPIO for oe. Something along the lines 'output anable'
oe_pin = 2
     
# Setup all GPIO pins to receive output data
GPIO.setup(red1_pin, GPIO.OUT)
GPIO.setup(green1_pin, GPIO.OUT)
GPIO.setup(blue1_pin, GPIO.OUT)
GPIO.setup(red2_pin, GPIO.OUT)
GPIO.setup(green2_pin, GPIO.OUT)
GPIO.setup(blue2_pin, GPIO.OUT)
GPIO.setup(clock_pin, GPIO.OUT)
GPIO.setup(a_pin, GPIO.OUT)
GPIO.setup(b_pin, GPIO.OUT)
GPIO.setup(c_pin, GPIO.OUT)
GPIO.setup(latch_pin, GPIO.OUT)
GPIO.setup(oe_pin, GPIO.OUT)
     
# screen to produce on the led matrix. Beginning in the upper left corner
screen = [[0 for x in range(32)] for x in range(16)]
   
def clock():
    GPIO.output(clock_pin, 1)
    GPIO.output(clock_pin, 0)
     
def latch():
    GPIO.output(latch_pin, 1)
    GPIO.output(latch_pin, 0)
     
def bits_from_int(x):
    a_bit = x & 1
    b_bit = x & 2
    c_bit = x & 4
    return (a_bit, b_bit, c_bit)
     
def set_row(row):
    a_bit, b_bit, c_bit = bits_from_int(row)
    GPIO.output(a_pin, a_bit)
    GPIO.output(b_pin, b_bit)
    GPIO.output(c_pin, c_bit)
     
def set_color_top(color):
    red, green, blue = bits_from_int(color)
    GPIO.output(red1_pin, red)
    GPIO.output(green1_pin, green)
    GPIO.output(blue1_pin, blue)
     
def set_color_bottom(color):
    red, green, blue = bits_from_int(color)
    GPIO.output(red2_pin, red)
    GPIO.output(green2_pin, green)
    GPIO.output(blue2_pin, blue)
     
def refresh():
    for row in range(8):
        GPIO.output(oe_pin, 1)
        set_color_top(0)
        set_row(row)

        for col in range(32):
            set_color_top(screen[row][col])
            set_color_bottom(screen[row+8][col])
            clock()

        latch()
        GPIO.output(oe_pin, 0)

        time.sleep(delay)    
     
def set_pixel(x, y, color):
    screen[y][x] = color
    
def put_border_on_screen():
    # Color of the border (here: blue)
    color = 4

    # border for a 6x7 field in the middle of the matrix
    for row in range(2, 16):
        for col in range(8, 24):
            if (row == 2 or row == 15 or col == 8 or col == 23):
                screen[row][col] = color;

def put_board_on_screen(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            screen[2*i+3][2*j+9]  = list[i][j]
            screen[2*i+3][2*j+10] = list[i][j]
            screen[2*i+4][2*j+9]  = list[i][j]
            screen[2*i+4][2*j+10] = list[i][j]
    
def clear_screen():
    for row in range(16):
        for col in range(32):
            screen[row][col] = 0;

def setup_list():
    list = [[0 for x in range(7)] for x in range(6)]
    list[5][3] = 1
    list[5][2] = 3

    return list

list = setup_list()
clear_screen()
put_border_on_screen()
put_board_on_screen(list)
     
while True:
    refresh()
