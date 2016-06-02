#!/usr/bin/python
from PIL import Image
import Glitch, random
from Glitch import ExtendedImage

im = ExtendedImage(Image.open("5.jpg"))
im.roll(.2)
im.show()
