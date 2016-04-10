import RPi.GPIO as GPIO
from FourWins import GamingBoard
import time
from threading import Thread
from _thread import start_new_thread
class LEDMatrix(Thread):
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

    def __init__(self, gamingBoard):
        Thread.__init__(self)
        self.myBoard = gamingBoard
        self.list = self.myBoard.board
        self.clear_screen()
        self.put_border_on_screen()
        self.put_board_on_screen()
        start_new_thread(self.blinkTimer,())

    def clock(self):
        GPIO.output(self.clock_pin, 1)
        GPIO.output(self.clock_pin, 0)

    def latch(self):
        GPIO.output(self.latch_pin, 1)
        GPIO.output(self.latch_pin, 0)

    def bits_from_int(self, x):
        a_bit = x & 1
        b_bit = x & 2
        c_bit = x & 4
        return (a_bit, b_bit, c_bit)

    def set_row(self, row):
        a_bit, b_bit, c_bit = self.bits_from_int(row)
        GPIO.output(self.a_pin, a_bit)
        GPIO.output(self.b_pin, b_bit)
        GPIO.output(self.c_pin, c_bit)

    def set_color_top(self, color):
        red, green, blue = self.bits_from_int(color)
        GPIO.output(self.red1_pin, red)
        GPIO.output(self.green1_pin, green)
        GPIO.output(self.blue1_pin, blue)

    def set_color_bottom(self, color):
        red, green, blue = self.bits_from_int(color)
        GPIO.output(self.red2_pin, red)
        GPIO.output(self.green2_pin, green)
        GPIO.output(self.blue2_pin, blue)

    def refresh(self):
        self.list = self.myBoard.board
        self.put_board_on_screen()
        for row in range(8):
            GPIO.output(self.oe_pin, 1)
            self.set_color_top(0)
            self.set_row(row)

            for col in range(32):
                self.set_color_top(self.screen[row][col])
                self.set_color_bottom(self.screen[row+8][col])
                self.clock()

            self.latch()
            GPIO.output(self.oe_pin, 0)

            time.sleep(self.delay)

    def set_pixel(self, x, y, color):
        self.screen[y][x] = color

    def put_border_on_screen(self):
        # Color of the border (here: blue)
        color = 4

        # border for a 6x7 field in the middle of the matrix
        for row in range(2, 16):
            for col in range(8, 24):
                if (row == 2 or row == 15 or col == 8 or col == 23):
                    self.screen[row][col] = color

    def put_board_on_screen(self):
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                self.screen[2*i+3][2*j+9]  = self.list[i][j]
                self.screen[2*i+3][2*j+10] = self.list[i][j]
                self.screen[2*i+4][2*j+9]  = self.list[i][j]
                self.screen[2*i+4][2*j+10] = self.list[i][j]

    def clear_screen(self):
        for row in range(16):
            for col in range(32):
                self.screen[row][col] = 0

    def clearBlink(self):
        for row in range(0, 2):
            for col in range(8, 23):
                self.screen[row][col] = 0


    def run(self):
        while True:
            self.refresh()

    def blinkTimer(self):
        while True:       
            blinkPos = self.myBoard.currentPosition
            player = self.myBoard.currentPlayer
            self.screen[0][2*blinkPos+7] = player
            self.screen[0][2*blinkPos+8] = player
            self.screen[1][2*blinkPos+7] = player
            self.screen[1][2*blinkPos+8] =player
            time.sleep(0.2)
            self.clearBlink()
            time.sleep(0.2)

