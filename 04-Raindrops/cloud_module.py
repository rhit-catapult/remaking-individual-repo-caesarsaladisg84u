import pygame
import sys
import time  # Note this!
import random  # Note this!
import raindrop_module
class Cloud:
    def __init__(self, screen, x, y, image_filename):
        """ Creates a Cloud sprite that will produce Raindrop objects.  The cloud will be moving around. """
        # Done 24: Initialize this Cloud, as follows:
        #     - Store the screen.
        #     - Set the initial position of this Cloud to x and y.
        #     - Set the image of this Cloud to the given image filename.
        #     - Create a list for Raindrop objects as an empty list called raindrops.
        #   Use instance variables:
        #      screen  x  y  image   raindrops.
        self.screen = screen
        self.x = x
        self.y = y
        self.image_cloud = pygame.image.load("cloud.png")
        self.raindrops = []

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 25: Draw (blit) this Cloud's image at its current position.
        self.screen.blit(self.image_cloud, (self.x, self.y))

    def rain(self, raindrop):
        """ Adds a Raindrop to the array of raindrops so that it looks like the Cloud is raining. """
        # Done 28: Append a new Raindrop to this Cloud's list of raindrops,
        #     where the new Raindrop starts at:
        #       - x is a random integer between this Cloud's x and this Cloud's x + 300.
        #       - y is this Cloud's y + 100.
        self.raindrops.append(raindrop(self.screen, random.randint(self.x, self.x+300), self.y+100))