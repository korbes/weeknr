import pystray
from PIL import Image, ImageDraw

width = 32
height = 32
color1 = 0
color2 = 255

def on_exit(icon, item):
    icon.stop()

mymenu = pystray.Menu(pystray.MenuItem('Exit', on_exit))

icon = pystray.Icon('test', menu=mymenu)
# Generate an image
image = Image.new('RGB', (width, height), color1)
dc = ImageDraw.Draw(image)
dc.rectangle((width // 2, 0, width, height // 2), fill=color2)
dc.rectangle((0, height // 2, width // 2, height), fill=color2)

icon.icon = image

def setup(icon):
    icon.visible = True

icon.run(setup)

