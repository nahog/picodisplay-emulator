# Pimoroni's picodisplay emulator

Basic emulator for pico display https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/pico_display of python calls using graphycs.py library from https://mcsp.wartburg.edu/zelle/python/

1. Add `graphycs.py` and `picodisplay.py` to your `lib` folder (if you don't have a lib folder, create one and also add `__init__.py` to it)
2. Add `from lib import picodisplay as p` and `picodisplay = p.PicoDisplay()` and comment out the normal `import picodisplay`
3. Add `picodisplay.keep_running()` at the end of the main file

Example:

```python
from lib import picodisplay as p
picodisplay = p.PicoDisplay()
# After this you can use picodisplay as usual (not all methods are implemented)

buf = bytearray(picodisplay.get_width() * picodisplay.get_height() * 2)
picodisplay.init(buf)

picodisplay.set_pen(255, 0, 0)
picodisplay.clear()
picodisplay.set_pen(0, 255, 0)
picodisplay.pixel(10, 10)
picodisplay.set_pen(0, 0, 255)
picodisplay.pixel_span(20, 20, 50)
pen = picodisplay.create_pen(99, 33, 99)
picodisplay.set_pen(pen)
picodisplay.rectangle(100, 60, 30, 60)
picodisplay.set_pen(255, 255, 255)
picodisplay.circle(200, 40, 10)
picodisplay.update() # Update method does nothing for now, changes are applied directly to the window (no buffer)
picodisplay.set_led(255, 0, 0)

# This is needed at the end of your program to keep the emulator open
picodisplay.keep_running()
```
## Extras

A mininal implementation of utime is also provided to simulate basic micropython timing calls

```python
from lib.utime import MicroTime
utime = MicroTime()
# After this you can use utime as usual (not all methods are implemented)

utime.ticks_ms()
utime.sleep(1)
```

## Implemented methods

### picodisplay

- init(buffer)
- get_height()
- get_width()
- set_backlight(brightness)
- set_led(r, g, b)
- is_pressed(button)
- set_pen(r, g, b)
- create_pen(r, g, b)
- clear()
- pixel(x, y)
- pixel_span(x, y, l)
- rectangle(x, y, w, h)
- circle(x, y, r)
- update()

### utime

- ticks_ms()
- sleep(seconds)

## Other projects that uses this lib

- https://github.com/nahog/pico-tetris