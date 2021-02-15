# Pimoroni's picodisplay emulator

Basic emulator for pico display https://github.com/pimoroni/pimoroni-pico/tree/main/micropython/modules/pico_display of python calls using graphycs.py library from https://mcsp.wartburg.edu/zelle/python/

Example:

```python
from lib import picodisplay as p
picodisplay = p.PicoDisplay()
# after this you can use picodisplay as usual (not all methods are implemented)

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
picodisplay.update() # .update() does nothing, for now, changes are applied directly to the windows (no buffer)
picodisplay.set_led(255, 0, 0)

# This is needed at the end of your program to keep the emulator open
picodisplay.keep_running()
```
