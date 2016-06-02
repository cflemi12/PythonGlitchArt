#!/usr/bin/python
"""
This is the Glitch module that utilizes a wrapper class, ExtendedImage,
for PIL's Image module. This module has multiple functions that are used
solely for the purpose of manipulating the image in a glitch art like 
fashion. 
Author: Chase Fleming
Date: 4/19/16
"""

import math, random
from PIL import Image
import numpy as np

__all__ = ["getSelf", "vertical_chop", "horizontal_chop", "show", "save", "color_round", "color_cosine", "color_sine", "color_tangent", "horizontal_wave", "vertical_wave", "y_reverse", "x_reverse", "randomize_color", "shear", "log", "roll"]

class ExtendedImage(object):
    
    def __init__(self, img):
        """ Wrapper class constructor. """
        self._img = img

    def getSelf(self):
        """ Returns the Image object of the wrapper object. """
        return self._img

    def vertical_chop(self):
        """ Randomly chops image vertically and stitches it back together. """
        blank = Image.new(self._img.mode, self._img.size, "white")
        incrament = self._img.size[0]/random.choice(_factors(self._img.size[0]))
        boxes = [(x, 0, x+incrament, self._img.size[1]) for x in range(0, self._img.size[0], incrament)]
        random.shuffle(boxes)
        count = 0
        for box in boxes:
            blank.paste(self._img.crop(box), (count,0))
            count += incrament
        self._img = blank

    def horizontal_chop(self):
        """ Randomy chops image horizontally and stitches it back together. """
        blank = Image.new(self._img.mode, self._img.size, "white")
        incrament = self._img.size[1]/random.choice(_factors(self._img.size[1]))
        boxes = [(0, x, self._img.size[0], x+incrament) for x in range(0, self._img.size[1], incrament)]
        random.shuffle(boxes)
        count = 0
        for box in boxes:
            blank.paste(self._img.crop(box), (0, count))
            count += incrament
        self._img = blank 

    def show(self):
        """ @override Calls Image's show() method from the Wrapper class. """
        return self._img.show()

    def save(self, fn, type=0):
        """ @override Calls Image's save() method from the Wrapper class. """
        return self._img.save(fn, type)
    
    def color_round(self):
        """ For each pixel and each RGB value per pixel, it is rounded to either 0 or 255. """
        width, height = self._img.size
        blank = Image.new(self._img.mode, self._img.size, "white")
        for y in range(height):
            for x in range(width):
                r,b,g = self._img.getpixel((x,y))
                blank.putpixel((x, y), (_round(r),_round(b),_round(g)))
        self._img = blank

    def color_cosine(self):
        """ Each pixel's RGB value is cosine transformed with an amplitude of 255. """
        width, height = self._img.size
        blank = Image.new(self._img.mode, self._img.size, "white")
        for y in range(height):
            for x in range(width):
                r,b,g = self._img.getpixel((x,y))
                blank.putpixel((x, y), (int(round(math.cos(r)*255)),int(round(math.cos(b)*255)),int(round(math.cos(g)*255))))
        self._img = blank
        
    def color_sine(self):
        """ Each pixel's RGB value is sine transformed with an amplitude of 255. """
        width, height = self._img.size
        blank = Image.new(self._img.mode, self._img.size, "white")
        for y in range(height):
            for x in range(width):
                r,b,g = self._img.getpixel((x,y))
                blank.putpixel((x, y), (int(round(math.sin(r)*255)),int(round(math.sin(b)*255)),int(round(math.sin(g)*255))))
        self._img = blank
        
    def color_tangent(self):
        """ Each pixel's RBG value is tangent transformed with an amplitude of 255. """
        width, height = self._img.size
        blank = Image.new(self._img.mode, self._img.size, "white")
        for y in range(height):
            for x in range(width):
                r,b,g = self._img.getpixel((x,y))
                blank.putpixel((x, y), (int(round(math.tan(r)*255)),int(round(math.tan(b)*255)),int(round(math.tan(g)*255))))
        self._img = blank

    def horizontal_wave(self, amplitude=0):
        """ For each (x,y) pixel is transformed to (x,cos(.035y)+amplitude+y). """
        amplitude = (int(amplitude), int(abs(amplitude)))[amplitude<0]
        blank = Image.new(self._img.mode, (self._img.size[0], self._img.size[1]+2*amplitude), "black")
        width, height = self._img.size
        for x in range(width):
            for y in range(height):
                blank.putpixel((x, int(math.cos(.035*y)*amplitude)+amplitude+y), self._img.getpixel((x,y))) 
        blank = blank.resize(self._img.size)
        self._img = blank
        
    def vertical_wave(self, amplitude=0):
        """ For each (x,y) pixel is transformed to (cos(.035x)+amplitutde+x, y). """
        amplitude = (int(amplitude), int(abs(amplitude)))[amplitude<0]
        blank = Image.new(self._img.mode, (self._img.size[0]+2*amplitude, self._img.size[1]), "black")
        width, height = self._img.size
        for x in range(width):
            for y in range(height):
                blank.putpixel((int(math.cos(.035*x)*amplitude)+amplitude+x, y), self._img.getpixel((x,y))) 
        blank = blank.resize(self._img.size)
        self._img = blank

    def y_reverse(self):
        """ For every odd x pixel, the line of y pixels is reversed. """
        blank = Image.new(self._img.mode, self._img.size, "black")
        width, height = self._img.size
        for x in range(width):
            for y in range(height):
                if x%2:
                    blank.putpixel((x, height-y-1), self._img.getpixel((x,y)))
                else:
                    blank.putpixel((x,y), self._img.getpixel((x,y)))
        self._img = blank
        
    def x_reverse(self):
        """ For every odd y pixel, the line of x pixels is reversed. """
        blank = Image.new(self._img.mode, self._img.size, "black")
        width, height = self._img.size
        for y in range(height):
            for x in range(width):
                if y%2:
                    blank.putpixel((width-x-1, y), self._img.getpixel((x,y)))
                else:
                    blank.putpixel((x,y), self._img.getpixel((x,y)))
        self._img = blank

    def randomize_color(self):
        """ Randomizes the blue and green value of each RGB pixel. """
        for x in range(self._img.size[0]):
            for y in range(self._img.size[1]):
                r,g,b = self._img.getpixel((x,y))
                self._img.putpixel((x,y), (r, random.randrange(1,255), random.randrange(1, 255)))
                
    def shear(self, a):
        """ Shears transforms the image by a degrees and mods the value by size of image. """
        blank = Image.new(self._img.mode, self._img.size, "black")
        width, height = self._img.size
        for y in range(height):
            for x in range(width):
                xprime = int(x*math.cos(a) - y*math.sin(a))%width
                yprime = int(x*math.sin(a) + y*math.cos(a))%height 
                blank.putpixel((xprime,yprime), self._img.getpixel((x,y)))
        self._img = blank
        
    def log(self):
        """ Takes the log of the pixel values. """
        blank = Image.new(self._img.mode, self._img.size, "black")
        width, height = self._img.size
        for y in range(height):
            for x in range(width):
                r,b,g = self._img.getpixel((x,y))
                logpix = _function(r,b,g)
                blank.putpixel((x,y), logpix)
        self._img = blank

    def roll(self, ratio=1):
        """ Uses numpy roll to distort rows of pixels. """
        pixels = np.array(self._img)
        width, height = self._img.size
        columns = np.array_split(pixels, width, axis=1)
        count = 0
        for col in columns:
           columns[count] = np.roll(col,int(ratio*(height)*math.cos(width*count)))
           count = count + 1
        total = np.concatenate(columns,axis=1)
        total = Image.fromarray(total)
        self._img = total

def _factors(n):
    """ Returns a list of factors of n. """
    return list(sum([[i, n//i] for i in xrange(1, int(n**.5)+1) if not
         n%i], []))
    
def _round(n):
    """ Rounds n in the range of 0 to 255. """
    return (0,255)[n>=128]

def _function(a,b,c):
    fa = a
    fb = int(0.6*b)
    fc = int(10*math.log(c+1))
    return fa, fb, fc
