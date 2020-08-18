# -*- coding: utf-8 -*-
"""
Description: This program takes an image and makes it into digital cartoon art.

Name: Nicole Nigro
    
Notes: Install packages PIL 1.1.7 or later and wxPython 2.9.2.4-1 or later
"""

from PIL.Image import open, new
from PIL.ImageColor import getrgb
from PIL.ImageOps import grayscale
import wx
import os

class CartoonArt:
    
    #constructor
    def __init__(self):
        self.spacing = 4 #spacing for dots and lines
        self.palette = [] 
        self.colors  = []
        self.color_palette= ['D4CEFD', 'F48DC0', 'B7F9D2', 'FFF3B7', 'B7EBF7'] #5 hexadecimal colors
    
    #converts a color from a hexadecimal value to a rgb tuple
    def hex_to_rgb(self, hex):
        return getrgb('#' + hex)
    
    #converts a color from a rgb tuple to a hexadecimal value
    def rgb_to_hex(self, rgb):
        hexValue = '%02x%02x%02x' % rgb
        return hexValue.upper()   
    
    #prompts the user to pick a file to use in this program
    def get_path(self, wildcard):
        app = wx.App(None)
        style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        else:
            path = None
        dialog.Destroy()
        return path
    
    #makes the cartoon picture with the color palette specified in the constructor
    def make_cartoon_pic(self, pixels, palette):  
        new_pixels=[]
        for p in pixels:
            #assigns pixels to different colors (from the palette) based off of original image's grayscale values
            if p>=0 and p<50: 
                  new_pixels.append(self.hex_to_rgb(palette[0]))
            elif p>=50 and p<100:
                  new_pixels.append(self.hex_to_rgb(palette[1])) 
            elif p>=100 and p<150: 
                new_pixels.append(self.hex_to_rgb(palette[2]))
            elif p>=150 and p<200:
                new_pixels.append(self.hex_to_rgb(palette[3]))
            else: 
                new_pixels.append(self.hex_to_rgb(palette[4]))
        return new_pixels
    
    #draws dots on the cartoon art
    def make_dots(self, image, color):
        w, h=image.size
        print w,h
        dot_color=(0,0,0)
        for x in range (0, w-6, 6): #skips 6 pixels to put spaces between the dots
            for y in range (0, h-6, 6):
                p=image.getpixel((x, y))
                if p==self.hex_to_rgb (color):
                    image.putpixel ((x, y), dot_color)
                    image.putpixel ((x+1, y), dot_color) 
                    image.putpixel ((x, y+1), dot_color)
                    image.putpixel ((x+1, y+1), dot_color)
        for x in range (3, w-6, 6): #starts at 3 because this series of dots is in between the series above
            for y in range (3, h-6, 6): 
                p=image.getpixel((x, y)) 
                if p==self.hex_to_rgb (color): 
                    image.putpixel ((x, y), dot_color) 
                    image.putpixel ((x+1, y), dot_color)
                    image.putpixel ((x, y+1), dot_color)
                    image.putpixel ((x+1, y+1), dot_color)
        return image
    
    #draws lines on the cartoon art
    def make_lines(self, image, color):
        w, h=image.size
        print w,h
        dot_color=(0,0,0)
        for x in range (0, w):
            for y in range (0, h-6, 6): #skips 6 pixels to put spaces between the lines
                p=image.getpixel((x, y))
                if p==self.hex_to_rgb (color):
                    image.putpixel ((x, y), dot_color) #puts the pixel in the lower left corner
        return image
    
    #processes and saves the finished art
    def process_image(self):
        file_path=self.get_path('*.*')
        print 'You selected', file_path 
        img=open(file_path)
        gray_img=grayscale(img)
        gray_pixels=gray_img.getdata() 
        new_img_pixels = self.make_cartoon_pic(gray_pixels, self.color_palette)
        img_new = new("RGB", img.size)
        img_new.putdata(new_img_pixels)
        img_new = self.make_dots(img_new, self.color_palette[2])
        img_new=self.make_lines(img_new, self.color_palette[0])
        
        import os 
        img_new.save(os.path.dirname(file_path) + "/" + "Nicole_cartoon.jpg") #saves image--change the last string to whatever you want your image saved as
    
if __name__ == '__main__':
    cartoon = CartoonArt()
    cartoon.process_image()
