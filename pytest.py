#!/usr/bin/python
from PIL import Image
import Glitch, random

img = Glitch.ExtendedImage(Image.open("1.jpg"))
img.shear(12)
img.show()
