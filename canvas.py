import numpy as np
from PIL import Image


class Canvas:
    """Object where all shapes are going to be drown"""

    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color

        #Create a 3d numpy array of zeros
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)\
        #Change [0, 0, 0] with user given values for color
        self.data[:] = self.color

    def make(self, imagepath):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)