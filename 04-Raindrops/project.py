import pygame
import sys
import time  # Note this!
import random  # Note this!
import hero_module
import cloud_module
import raindrop_module

def main():
    """ Main game loop that creates the sprite objects, controls interactions, and draw the screen. """
    # Done 1: Initialize the game, display a caption, and set   screen   to a 1000x600 Screen.
    pygame.init()
    pygame.display.set_caption("Rainy Day")
    screen = pygame.display.set_mode((1000, 600))

    # Done 2: Make a Clock
    clock = pygame.time.Clock()

    # Done 7: As a temporary test, make a new Raindrop called test_drop at x=320 y=10
    # test_drop = Raindrop(screen, 320, 10)
    # Done 15: Make a Hero, named mike, with appropriate images, starting at position x=200 y=400.
    mike = hero_module.Hero(screen, 200, 400, "Mike_umbrella.png", "Mike.png")
    # Done 15: Make a Hero, named alyssa, with appropriate images, starting at position x=700 y=400.
    alyssa = hero_module.Hero(screen, 700, 400, "Alyssa_umbrella.png", "Alyssa.png")
    # Done 23: Make a Cloud, named cloud, with appropriate images, starting at position x=300 y=50.
    cloud = cloud_module.Cloud(screen, 300, 50, "cloud.png")
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP]:
            #^checks if up key being pressed
            cloud.y -= 5
        if pressed_keys[pygame.K_DOWN]:
            #^checks if down key being pressed
            cloud.y += 5
        if pressed_keys[pygame.K_LEFT]:
            #^checks if left key being pressed
            cloud.x -= 5
        if pressed_keys[pygame.K_RIGHT]:
            #^checks if right key being pressed
            cloud.x += 5
        # Done 5: Inside the game loop, draw the screen (fill with white)
        screen.fill((255,255,255))
        cloud.draw()
        # Done 29: Remove the temporary testdrop code from this function and refactor it as follows:
        # Done: Make the Cloud "rain", then:
        cloud.rain(raindrop_module.Raindrop)
        # Done    For each Raindrop in the Cloud's list of raindrops:
        for raindrop in cloud.raindrops:
            raindrop.move()
            raindrop.draw()
            #       - move the Raindrop.
            #       - draw the Raindrop.
            # Drop  30: if the Hero (Mike or Alyssa) is hit by a Raindrop, set the Hero's last_time_hit to the current time.
            # Optional  - if the Raindrop is off the screen or hitting a Hero, remove it from the Cloud's list of raindrops.
            if mike.hit_by(raindrop):
                mike.last_hit_time = time.time()
            elif alyssa.hit_by(raindrop):
                alyssa.last_hit_time = time.time()

        # Done 18: Draw the Heroes (Mike and Alyssa)
        mike.draw()
        alyssa.draw()
        # Done 6: Update the display and remove the pass statement below
        pygame.display.update()
    #pass


# Done 0: Call main.
main()