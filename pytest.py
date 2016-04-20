#!/usr/bin/python
from PIL import Image
import Glitch, random

img = Glitch.ExtendedImage(Image.open("1.jpg"))
img.horizontal_wave(random.randrange(20,50))
img.y_reverse()
img.color_round()
img.save("whymadhavpt2.jpg", "JPEG")
