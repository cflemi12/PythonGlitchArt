#!/usr/bin/python

import math, random, sys
from PIL import Image
from matplotlib.cbook import Null

class ExtendedImage(object):
    
    #initalizes ExtendedObject as being an image
    def __init__(self, img):
        self._img = img
    
    #returns the image object
    def getSelf(self):
        return self._img
    
    #randomly chops image vertically and puts it back together
    def vertical_chop(self):
        blank = Image.new(self._img.mode, self._img.size, "white")
        incrament = self._img.size[0]/random.choice(factors(self._img.size[0]))
        boxes = [(x, 0, x+incrament, self._img.size[1]) for x in range(0, self._img.size[0], incrament)]
        random.shuffle(boxes)
        count = 0
        for box in boxes:
            blank.paste(self._img.crop(box), (count,0))
            count += incrament
        self._img = blank
        
    #randomy chops image horizontally and puts it back together
    def horizontal_chop(self):
        blank = Image.new(self._img.mode, self._img.size, "white")
        incrament = self._img.size[1]/random.choice(factors(self._img.size[1]))
        boxes = [(0, x, self._img.size[0], x+incrament) for x in range(0, self._img.size[1], incrament)]
        random.shuffle(boxes)
        count = 0
        for box in boxes:
            blank.paste(self._img.crop(box), (0, count))
            count += incrament
        self._img = blank 
    
    #returns image object
    def getSelf(self):
        return self._img
    
    #@override show method
    def show(self):
        return self._img.show
    def color_rounding(self, amplitude=0):
        width, height = self._img.size
        blank = Image.new(self._img.mode, self._img.size, "white")
        for y in range(height):
            for x in range(width):
                r,b,g = self._img.getpixel((x,y))
                blank.putpixel((x, y), (round(r),round(b),round(g)))
        self._img = blank

    
        
def factors(n):
    return list(sum([[i, n//i] for i in xrange(1, int(n**.5)+1) if not
         n%i], []))
    
def round(n):
    return (0,255)[n>=128]
