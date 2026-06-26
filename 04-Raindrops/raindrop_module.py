import pygame
import sys
import time  # Note this!
import random  # Note this!
class Raindrop:
    def __init__(self, screen: pygame.Surface, x, y):
        #^ __init__ is a constructor, which is a special method that is called when an object is created. It initializes the object's attributes. In this case, it initializes a Raindrop object with its screen, x and y position, and speed.
        #^constructor, passes in self because it is a method of the class, and screen, x, y because those are needed to create a raindrop
        #: allows you to define the variable
        """ Creates a Raindrop sprite that travels down at a random speed. """
        # Done 8: Initialize this Raindrop, as follows:
        #     - Store the screen.
        #     - Set the initial position of the Raindrop to x and y.
        #     - Set the initial speed to a random integer between 5 and 15.
        #   Use instance variables:   screen  x  y  speed.
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = random.randint(5,15)

    def move(self):
        """ Move the self.y value of the Raindrop down the screen (y increase) at the self.speed. """
        # Done 11: Change the  y  position of this Raindrop by its speed.
        self.y += self.speed

    def off_screen(self):
        """ Returns true if the Raindrop y value is not shown on the screen, otherwise false. """
        # Note: this will be used for testing, but not used in the final version of the code for the sake of simplicity.
        # Done 13: Return  True  if the  y  position of this Raindrop is greater than 800.
        return self.y > self.screen.get_height()

    def draw(self):
        """ Draws this sprite onto the screen. """
        # Done 9: Draw a vertical line that is 5 pixels long, 2 pixels thick,
        #      from the current position of this Raindrop (use either a black or blue color).
        pygame.draw.line(self.screen, (0, 0, 128), (self.x, self.y),(self.x, self.y + 5), 2)
        #^self refers to the instance, no longer has reference to original screen, only the screen saved in the self.screen variable in constructor
