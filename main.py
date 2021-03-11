from lib.picodisplay import PicoDisplay
from lib.utime import MicroTime
from lib.machine import Pin, PWM
utime = MicroTime()
picodisplay = PicoDisplay()
# added for emulation ↑↑↑↑↑↑↑↑↑↑

# import picodisplay
# import utime
# from machine import Pin, PWM

buf = bytearray(picodisplay.get_width() * picodisplay.get_height() * 2)
picodisplay.init(buf)

picodisplay.set_pen(255, 0, 0)
picodisplay.clear()

picodisplay.set_pen(0, 255, 0)
picodisplay.pixel(10, 10)
picodisplay.pixel(10, 11)
picodisplay.pixel(10, 12)
picodisplay.pixel(11, 10)
picodisplay.pixel(11, 11)
picodisplay.pixel(11, 12)
picodisplay.pixel(12, 10)
picodisplay.pixel(12, 11)
picodisplay.pixel(12, 12)

picodisplay.set_pen(0, 0, 255)
picodisplay.pixel_span(20, 20, 50)
picodisplay.pixel_span(80, 100, 500)

pen = picodisplay.create_pen(99, 33, 99)
picodisplay.set_pen(pen)
picodisplay.rectangle(100, 60, 30, 60)

picodisplay.set_pen(255, 255, 255)
picodisplay.circle(200, 40, 10)

picodisplay.update()

picodisplay.set_led(255, 0, 0)
picodisplay.set_led(0, 255, 0)
picodisplay.set_led(0, 0, 255)

pwm = PWM(Pin(0))
pwm.freq(440)
pwm.duty_u16(8192)

while True:
    if picodisplay.is_pressed(picodisplay.BUTTON_A):
        print('A')
    if picodisplay.is_pressed(picodisplay.BUTTON_B):
        print('B')
    if picodisplay.is_pressed(picodisplay.BUTTON_X):
        print('X')
    if picodisplay.is_pressed(picodisplay.BUTTON_Y):
        print('Y')
    print(utime.ticks_ms())
    utime.sleep(1)

pwm.duty_u16(0)

# added for emulation ↓↓↓↓↓↓↓↓↓↓
picodisplay.keep_running()