import numpy as np
from PIL import Image


class Square:
    """
    A square shape that can be drawn on a Canvas object.
    """
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        """ Draws the square onto the canvas"""
        canvas.data[self.x: self.x + self.side, self.y: self.y + self.side] = self.color


class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        """Draws the rectangle onto the canvas"""
        canvas.data[self.x: self.x + self.height, self.y: self.y + self.width] = self.color


class Canvas:
    """ Object where all shapes are going to be drawn"""

    def __init__(self, height, width, color):
        self.width = width
        self.height = height
        self.color = color

        # Create a 3D numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        # Change the zeros with user given values form color
        self.data[:] = self.color

    def make(self, imagepath):
        """Converts the current array into an image file"""
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)
