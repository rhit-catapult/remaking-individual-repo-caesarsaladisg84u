import pygame
import sys
import time

def main():
    # pre-define RGB colors for Pygame
    BLACK = pygame.Color("Black")
    WHITE = pygame.Color("White")
    IMAGE_SIZE = 470
    TEXT_HEIGHT = 30

    # initialize the pygame module
    pygame.init()

    # prepare the window (screen)
    screen = pygame.display.set_mode((IMAGE_SIZE, IMAGE_SIZE + TEXT_HEIGHT))
    pygame.display.set_caption("Text, Sound, and an Image")

    # Prepare the image
    # TODO (Done) 1: Create an image with the 2dogs.JPG image
    dogs_image = pygame.image.load("2dogs.JPG")
    
    # TODO 3: (Done) Scale the image to be the size (IMAGE_SIZE, IMAGE_SIZE)
    dogs_image = pygame.transform.scale(dogs_image, (IMAGE_SIZE, IMAGE_SIZE))
    # Prepare the text caption(s)
    # TODO 4: (Done) Create a font object with a size 28 font.
    bottom_font = pygame.font.SysFont("arial", 28)
    
    # print(pygame.font.get_fonts())
    # TODO 5: (Done) Render the text "Two Dogs" using the font object (it's like MAKING an image).
    # Prepare the music
    bottom_caption = bottom_font.render("Two Dogs", True, BLACK)
    # TODO 8: (Done) Create a Sound object from the "bark.wav" file.
    bark_sound = pygame.mixer.Sound("bark.wav")
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # TODO 9: Play the music (bark) if there's a mouse click.
            if event.type == pygame.MOUSEBUTTONDOWN:
                bark_sound.play()
        # Clear the screen and set the screen background
        screen.fill(WHITE)

        # Draw the image onto the screen
        # TODO (Done) 2: Draw (blit) the image onto the screen at position (0, 0)
        screen.blit(dogs_image, (0,0))
        # Draw the text onto the screen
        # TODO 6: (Done) Draw (blit) the text image onto the screen in the middle bottom.
        # Hint: Commands like these might be useful..
        #          screen.get_width(), caption1.get_width(), image1.get_height()
        caption_x = screen.get_width()/2 - bottom_caption.get_width() / 2
        caption_y = screen.get_height() - bottom_caption.get_height()
        screen.blit(bottom_caption, (caption_x, caption_y))
        # TODO 7: (Skipped) On your own, create a new bigger font and in white text place a 'funny' message on top of the image.

        # Update the screen
        pygame.display.update()
        


main()
