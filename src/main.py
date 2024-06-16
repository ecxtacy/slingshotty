import pygame
from game import game as game_module
from game import map_loader
from game import slinger
from entity import entity
from entity import planet as planet_module
from entity import player as player_module
from util import *
import math

# Initialize pygame
pygame.init()

# The screen width and height
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Setup screen and clock
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()

# Create a game object
game = game_module.Game(clock)
game_module.Game.screen = screen

# Load the level and game
game.load()

# Infinite game loop
while game.is_running():

    # Handle events
    game.handle_events()

    game_status = game.update()
    if(game_status == game_module.GameStatus.RESTART):
        continue

    screen.fill("black")
    game.draw_stars(1000, SCREEN_WIDTH, SCREEN_HEIGHT)
    game.render()

    # Refresh the display and buffers
    pygame.display.flip()

    game.set_fps(60)

pygame.quit()