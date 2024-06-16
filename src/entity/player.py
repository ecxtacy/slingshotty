from entity import entity
from util import *
from game import game as game_module
from game import slinger
from enum import Enum

class CollisionType(Enum):
    NO_COLLISION = 0
    EARTH = 1
    PLANET = 2


class Player(entity.Entity):
    def __init__(self, name, position, velocity, acceleration, width, height, image_path):
        super().__init__(name, position, velocity, acceleration, width, height, image_path)
        self.trail = Trial(100, (0, 255, 0))
        self.slinger = slinger.Slinger()
        self.collided_with_planet = False
        self.collided_with_earth = False

    def cleanup(self):
        self.trail.cleanup()
        self.slinger.cleanup()

        self.trail = None
        self.slinger = None
        self.surface = None
        self.rect = None

    # Override
    def render(self):
        self.trail.render()
        self.slinger.render()
        super().render()
        pass

    def handle_planet_collision(self):
        self.collided_with_planet = True
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        return CollisionType.PLANET

    def handle_earth_collision(self):
        self.collided_with_earth = True
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
        return CollisionType.EARTH

    def handle_collision(self, planets, earth):
        player_mask = pygame.mask.from_surface(self.surface)
        earth_mask = pygame.mask.from_surface(earth.surface)

        if player_mask.overlap(earth_mask, (earth.position.x - self.position.x, earth.position.y - self.position.y)):
            return self.handle_earth_collision()

        for planet in planets:
            planet_mask = pygame.mask.from_surface(planet.surface)
            
            if player_mask.overlap(planet_mask, (planet.position.x - self.position.x, planet.position.y - self.position.y)):
                return self.handle_planet_collision()

        

    # Override
    def update(self, planets):
        if self.collided_with_planet or self.collided_with_earth:
            return

        if not self.slinger.mouse_holding:
            self.acceleration = self.get_net_acceleration(planets)
            self.accelerate()
        super().update()
        com = self.get_centre_of_mass()
        self.trail.append((com.x, com.y))

    def get_net_acceleration(self, planets):

        acc = Vector(0, 0)
        for planet in planets:
            r_vector = planet.get_centre_of_mass() - self.get_centre_of_mass()
            g_vector_magnitude = planet.mass / (r_vector.get_magnitude() ** 2 + 1)
            r_unit_vector = get_unit_vector(r_vector)
            ax = r_unit_vector.x * (g_vector_magnitude)
            ay = r_unit_vector.y * (g_vector_magnitude)
            acc += Vector(ax, ay)

        return acc

    def handle_events(self, event):
        self.slinger.handle_events(event, self)

    def __str__(self):
        return f"""
            Player: 
            position => ({self.position.x, self.position.y})
            velocity => ({self.velocity.x, self.velocity.y})
            surface => ({self.surface})
            rect => ({self.rect})
        """

    def __del__(self):
        pass
