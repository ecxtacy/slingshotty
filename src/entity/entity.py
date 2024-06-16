import util
import pygame
from game import game as game_module

class Entity:

    # position
    # velocity
    # image path
    # width
    # height

    def __init__(self, name, position, velocity, acceleration, width, height, image_path):
        self.name = name
        self.update_acceleration(acceleration)
        self.update_velocity(velocity)
        self.update_position(position)
        self.update_height(height)
        self.update_width(width)
        self.add_image(image_path)
        self.estabilish()


    def update_position(self, position):
        self.position = position

    def update_velocity(self, velocity):
        self.velocity = velocity

    def update_acceleration(self, acceleration):
        self.acceleration = acceleration

    def update_width(self, width):
        self.width = width

    def update_height(self, height):
        self.height = height

    def get_centre_of_mass(self):
        return util.Vector(self.position.x + self.width / 2, self.position.y + self.height / 2)

    def add_image(self, path):
        self.surface = pygame.transform.scale(pygame.image.load(path), (self.width, self.height))

    def estabilish(self):
        self.rect = pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def accelerate(self):
        self.velocity += self.acceleration
    
    def update(self):
        self.move()
    
    def move(self):
        self.position += self.velocity
        self.rect.x = self.position.x
        self.rect.y = self.position.y

    def render(self):
        game_module.Game.screen.blit(self.surface, self.rect)
        # pygame.draw.circle(game_module.Game.screen, (255, 0, 0), (self.get_centre_of_mass().x, self.get_centre_of_mass().y), 5)

    def handle_events(self, event):
        pass












    # def render(self):
    #     game_module.Game.screen.blit(self.surface, self.rect)
    
            

