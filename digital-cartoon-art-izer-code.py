# -*- coding: utf-8 -*-
"""
Description: This program takes an image and makes it into digital cartoon art.

Name: Nicole Nigro
    
Notes: Install packages PIL 1.1.7 or later and wxPython 2.9.2.4-1 or later
"""

#the following things below are imported so this program can function
from PIL.Image import open, new
from PIL.ImageColor import getrgb
from PIL.ImageOps import grayscale
import wx
import os

class CartoonArt: #this is the cartoon art class

    def __init__(self):
        """this is the constructor method. it takes 1 parameter: self. it initializes
        one instance variable and initizlizes three instance variables to lists."""
        self.spacing = 4 #spacing for dots and lines. initalizes the self.spacing variable to 4.
        self.palette = [] #intializes the self.palette variable to an empty list
        self.colors  = [] #intializes the self.colors variable to an empty list
        self.color_palette= ['D4CEFD', 'F48DC0', 'B7F9D2', 'FFF3B7', 'B7EBF7'] #intializes the self.color_palette variable to a list the the 5 hexadecimal colors
    
    def hex_to_rgb(self, hex):
        """this is the hex_to rgb method. it takes 2 parameters: self and hex. it converts a color from a hexadecimal value to a rgb tuple."""
        """ Convert a given color from a hexadecimal value to a rgb tuple. For
            example a hex value of "C9A814" would get converted to (201, 168, 20).
            Returns the tuple value as a string.
            Parameters:
            [In] hex - the hexidecimal code (string) representing a color value. """ 
        #print '#' + hex, "  ", getrgb('#' + hex)
        return getrgb('#' + hex) #convert to hex value

    def rgb_to_hex(self, rgb):
        """this is the rgb_to_hex method. it takes 2 parameters: self and rgb. it converts a color from a rgb tuple to a hexadecimal value."""
        """ Convert a given color from a rgb tuple to a hexadecimal value. For
            example a rgb value of (201, 168, 20) would get converted to C9A814.
            It returns the hexadecimal value as a string.
            Parameters:
            [In] rgb - a tubple representing an rgb value.
        """
        hexValue = '%02x%02x%02x' % rgb
        #print rgb, "  ", hexValue.upper()
        return hexValue.upper()   

    def get_path(self, wildcard):
        """this is the get_path method. it takes 2 parameters: self and wildcard. it has the user pick a file to use in this program."""
        """
        Prompts user to select a file from a dialog box.
        Parameters:
        [In] wildcard - used to filter files in dialog box to only those with
                        the extension given.
        """
        app = wx.App(None)
        style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        else:
            path = None
        dialog.Destroy()
        return path
      
    def make_cartoon_pic(self, pixels, palette):  
        """this is the make_cartoon_pic method. it takes 3 parameters: self, pixels, and palette. the objective of this method is to make the
        cartoon picture."""
        new_pixels=[] #setting new_pixels equal to an empty list
        for p in pixels: #this for loop searches for the p variable in pixels
            if p>=0 and p<50: #if statement for when p is greater than or equal to 0 or if it's less than 50
                  new_pixels.append(self.hex_to_rgb(palette[0])) #appends for the first color in the color_palette list.
            elif p>=50 and p<100:#if statement for when p is greater than or equal to 50 or if it's less than 100
                  new_pixels.append(self.hex_to_rgb(palette[1])) #appends for the second color in the color_palette list.
            elif p>=100 and p<150: #if statement for when p is greater than or equal to 100 or if it's less than 150
                new_pixels.append(self.hex_to_rgb(palette[2]))#appends for the thirf color in the color_palette list.
            elif p>=150 and p<200: #if statement for when p is greater than or equal to 150 or if it's less than 200
                new_pixels.append(self.hex_to_rgb(palette[3])) #appends for the fourth color in the color_palette list.
            else: #else statment for the remaining values of p
                new_pixels.append(self.hex_to_rgb(palette[4])) #appends for the fifth color in the color_palette list.
        return new_pixels

    def make_dots(self, image, color):
        """this is the make_dots method. it takes 3 parameters: self, image, and color. the objective of this method is to make the dots for
        the digital cartoon art."""
        w, h=image.size #setting w, h equal to image.size (w for x and h for y)
        print w,h
        dot_color=(0,0,0) #setting dot_color equal to (0,0,0). this format will be used in the 2 lines below.
        for x in range (0, w-6, 6): #for loop where x starts at 0, ends at w-6, and is skipping by 6.
            for y in range (0, h-6, 6): #for loop where y starts at 0, ends at h-6, and is skipping by 6.
                p=image.getpixel((x, y)) #gets the pixels for the image in an (x, y) format
                if p==self.hex_to_rgb (color): #if statement for when the variable p is equal to self.hex_to_rgb(color)
                    image.putpixel ((x, y), dot_color) #puts the pixel in the lower left corner
                    image.putpixel ((x+1, y), dot_color) #puts the pixel in the lower right corner
                    image.putpixel ((x, y+1), dot_color) #puts the pixel in the upper left corner
                    image.putpixel ((x+1, y+1), dot_color) #puts the pixel in the upper right corner
        for x in range (3, w-6, 6): #for loop where x starts at 3, ends at w-6, and is skipping by 6. it starts at 3 because this series of dots is in between the series coded above.
            for y in range (3, h-6, 6): #for loop where x starts at 3, ends at h-6, and is skipping by 6. it starts at 3 because this series of dots is in between the series coded above.
                p=image.getpixel((x, y)) #gets the pixels for the image in an (x, y) format and sets it equal to p, a variable
                if p==self.hex_to_rgb (color): #if statement for when the variable p is equal to self.hex_to_rgb(color)
                    image.putpixel ((x, y), dot_color) #puts the pixel in the lower left corner
                    image.putpixel ((x+1, y), dot_color)#puts the pixel in the upper right corner
                    image.putpixel ((x, y+1), dot_color)#puts the pixel in the upper left corner
                    image.putpixel ((x+1, y+1), dot_color)#puts the pixel in the upper right corner
        return image

    def make_lines(self, image, color):
        """this is the make_lines method. it has 3 parameters: self, image, and color. the objective of this method is to make the lines for
        the digital cartoon art."""
        w, h=image.size #setting w, h equal to image.size (w for x and h for y)
        print w,h
        dot_color=(0,0,0) #setting dot_color equal to (0,0,0). this format will be used in 1 of the lines below.
        for x in range (0, w): #for loop where x starts at 0 and ends at w.
            for y in range (0, h-6, 6): #for loop where y starts at 0, ends at h-6 and skips 6. it only needs to skip for this (can either be for x in range OR for y in range) because there needs to be spaces between the lines.
                p=image.getpixel((x, y)) #gets the pixels for the image in an (x, y) format and sets it equal to p, a variable
                if p==self.hex_to_rgb (color): #if statement for when the variable p is equal to self.hex_to_rgb(color)
                    image.putpixel ((x, y), dot_color) #puts the pixel in the lower left corner
        return image

    def process_image(self):
        """this is the process_image method. It's only parameter is self. the objective of this method is to finally process the digital cartoon
        art image."""
        file_path=self.get_path('*.*')#the file that is being used for the digital cartoon art
        print 'You selected', file_path #prints in the output saying what file the 
        img=open(file_path) #opens the image
        gray_img=grayscale(img) #passes the selected color image as an argument, to convert the image to a grayscale format
        gray_pixels=gray_img.getdata() #grayscale values are saved to this list: gray_pixels
        """the following lines (136-147) are print statements to help debug the code"""
        #for i in range(10):
            #print gray_pixels[i]
        #print pix_list
        #gray_img.show()
        #img = self.make_dots(img, 'FFFF00')
        #img = self.make_lines(img, '99FFFF')
        #img.show()
        new_img_pixels = self.make_cartoon_pic(gray_pixels, self.color_palette)
        #w,h = img.size
 	#print "img total pixels:", w*h
 	#print "new_img total pixels:", len(new_img_pixels)
 	#assert(w*h == len(new_img_pixels))
 	img_new = new("RGB", img.size) #a new empty image
 	img_new.putdata(new_img_pixels) #passes the pixel list returned by make_cartoon_pic as an argument to the putdata function to create a new image (img_new)
 	img_new = self.make_dots(img_new, self.color_palette[2]) #calls the make_dots method
 	img_new=self.make_lines(img_new, self.color_palette[0]) #calls the make_lines method
        
        #the lines below (154-155) are used to save the image
 	import os 
 	img_new.save(os.path.dirname(file_path) + "/" + "Nicole_cartoon.jpg")
    
if __name__ == '__main__':  # run the program only if this is the code file we're working on
    cartoon = CartoonArt()
    cartoon.process_image()
