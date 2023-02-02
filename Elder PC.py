import pygame, sys
from settings import *
from level import Level
from debug import debug
# here, I am importing all the important libraries which i will be using
# along with importing everything from the settings file (which i still need to create)

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Elder PC")
        self.clock = pygame.time.Clock()
        self.level = Level()
#here i am initialising pygame, creating the display surface and creating a clock

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
# in the run method i am creating an event loop.
# one event is making sure that i am closing the game

            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
# filling the screen with the colour black, updating the display and controlling the frame rate
if __name__ == "__main__":
    Game = Game()
    Game.run()
            
