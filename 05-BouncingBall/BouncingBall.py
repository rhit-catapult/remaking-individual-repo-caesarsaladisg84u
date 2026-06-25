import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!

# Done: Create a Ball class.
# Done: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# Done: Methods: __init__, draw, move
class Ball:
    def __init__(self, screen, color, x, y, radius, speed_x, speed_y):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
    def Draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.radius)

    def Move(self):
        self.x += self.speed_x
        self.y += self.speed_y
    def Rebound(self):
        if self.x > self.screen.get_width():
            self.speed_x = -1*self.speed_x
        if self.x < 0:
            self.speed_x = -1*self.speed_x
        if self.y > self.screen.get_height():
            self.speed_y = -1*self.speed_y
        if self.y < 0:
            self.speed_y = -1*self.speed_y

balls = []
def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 960))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # Done: Create an instance of the Ball class called ball1
    for i in range(10000):
        ball = Ball(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)), random.randint(0, 1280), random.randint(0, 960), random.randint(5, 20), random.randint(-5, 5), random.randint(-5, 5))
        balls.append(ball)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # Done: Move the ball
        for ball in balls:
            ball.Rebound()
            ball.Move()

        for ball in balls:
            ball.Draw()
        # Done: Draw the ball

        pygame.display.update()


main()


# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
