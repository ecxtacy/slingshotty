import pygame 
from util import *
from game import game as game_module

class Slinger:

    SLING_POWER_REDUCE_FACTOR = 10

    def __init__(self):
        self.start_pos = None
        self.release_pos = None
        self.player_launched = False
        self.mouse_holding = False

    def cleanup(self):
        pass

    def handle_events(self, event, player):
        if event.type == pygame.MOUSEBUTTONDOWN and not self.player_launched:
            self.mouse_holding = True
            if self.start_pos == None:
                com = player.get_centre_of_mass()
                self.start_pos = (com.x, com.y)
        elif event.type == pygame.MOUSEBUTTONUP:
            if self.mouse_holding:
                self.player_launched = True

                # Sling release logic
                self.release_pos = pygame.mouse.get_pos()
                mag = distance(self.start_pos, self.release_pos) / Slinger.SLING_POWER_REDUCE_FACTOR
                dirn = get_unit_vector(Vector(self.start_pos[0] - self.release_pos[0], self.start_pos[1] - self.release_pos[1]))
                vel = Vector(mag * dirn.x, mag * dirn.y)
                player.update_velocity(vel)

            self.mouse_holding = False

    def update(self):
        pass

    def render(self):
        if self.mouse_holding:
            # print()
            pygame.draw.line(game_module.Game.screen, (50, 50, 150), self.start_pos, pygame.mouse.get_pos(), 10)