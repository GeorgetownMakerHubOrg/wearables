#
# CircuitPython code
# Supported on Gemma M0
# There is no machine API on Atmel SAMD21 port - https://circuitpython.readthedocs.io/en/3.x/docs/ 
# CircuitPython doesn't support interrupts?  WTF?
#

import digitalio, pulseio, board, adafruit_dotstar
from time import sleep

dot = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
dot[0] = (0,0,0)

led = pulseio.PWMOut(board.D2)             # make it a PWM device

LOW = 1
HIGH = 255

def fade(start, stop, increment, delay):
  for i in range(start, stop, increment):
    led.duty_cycle = i ** 2                # 16 bit value so 255^2
    sleep(delay)

def main():
    delay = 0.01                               # let's have fun with this
    while True:
        fade(LOW, HIGH, 1, delay)     # up
        fade(HIGH, LOW, -1, delay)    # down
