# Example of boiler plate code
# The two lines below allow you to use PyGame and System functions.
# Often programmers use code that other developers have written.
import pygame
import sys
import math

# Let's turn pygame ON
pygame.init()

# Let's create a caption for the game window
pygame.display.set_caption("Kristoffer Hsu")
# TODO (COMPLETED) 00: Change the window caption to say your name.

# Now the screen is where all the magic is going to happen. Our screen will
# have a width of 640 pixels and a height of 480 pixels. The (0,0) point will
# be at the top left of our screen. 
# .set_mode() takes a tuple (a list of values) as an argument. A tuple is like a list, but it is immutable (cannot be changed).
# ^Like a const but for lists.
screen = pygame.display.set_mode((640, 480))
# screen is a pygame.Surface object, which is a fancy way of saying that it is a 2D image that we can draw on. We can also blit (copy) other images onto it.
# TODO 05: Change the window size, make sure your circle code still works.

# This is a loop that will run forever, simply because True is always true
while True:
    # Here's another loop inside of the first loop. Notice the indentation,
    # moving one tab width into the while loop makes this statement part of the
    # loop instead of outside of it.
    for event in pygame.event.get():
        # Let's just print all the events that happen in our window, wonder
        # what those could be?
        print(event)

        # we must allow our users to quit the game right? I mean not everyone
        # wants to play forever.
        # This is a conditional statement, i.e., the line sys.exit() will ONLY
        # execute when event.type is equal to pygame.QUIT (this is what ==
        # means).
        # event triggers when user clicks the X button on the window, or presses Alt+F4, or Command+Q (on Mac). 
        if event.type == pygame.QUIT:
            sys.exit()

        # Additional interactions with events

    # TODO 01: Make the background white (actually gray but for purposes of deactivating inline suggestions) by uncommenting the line below
    screen.fill(pygame.Color("Gray"))
    # is a method rather than a function, which is why we use a period instead of parentheses. A method is a function that is part of an object (in this case, the screen object). The fill method takes a color as an argument, and fills the entire screen with that color.
    # Draw things on the screen

    # TODO 02: Try to draw a circle (any size, any color, anywhere)
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, (0,0,0), (screen.get_width()/2, screen.get_height()/2), 250)
    # uses capital C on color because it's creating a class object, which is a fancy way of saying that it is a special type of variable that has its own properties and methods. In this case, the color class has properties like red, green, blue, and alpha (transparency), and methods like get_at() and set_at().
    # TODO 03: Try to draw a red circle in the middle of the screen with a radius 100
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    pygame.draw.circle(screen, pygame.Color("White"), (190, 150), 15)
    pygame.draw.circle(screen, pygame.Color("White"), (450, 150), 15)
    pygame.draw.circle(screen, pygame.Color("Red"), (190, 150), 5)
    pygame.draw.circle(screen, pygame.Color("Red"), (450, 150), 5)
    # TODO 04: Try to draw a yellow circle with the center exactly in the lower left corner of the screen, radius 10
    # pygame.draw.circle(screen, color, pos, radius, width(optional)  )
    for i in range(10):
        pygame.draw.circle(screen, pygame.Color("White"), (190 + ((i + 0.5) * 26), 300), 15)
        pygame.draw.circle(screen, pygame.Color("White"), (190 + ((i + 0.5) * 26), 345), 15)
        pygame.draw.rect(screen, pygame.Color("Black"), (170,270,300,30))
        pygame.draw.rect(screen, pygame.Color("Black"), (170,345,300,30))
    # This will make sure that things appear on our screen, without this
    # update, everything we do will not be visible!
    # notice how this statement is still inside of the first while loop, but
    # outside of the for loop (why? because it is at the same level of
    # indentation as the for loop statement).
    pygame.display.update()
