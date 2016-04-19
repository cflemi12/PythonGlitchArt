#!/usr/bin/python
from PIL import Image
import Glitch

img = Glitch.ExtendedImage(Image.open("1.jpg"))
img.color_rounding(500)
