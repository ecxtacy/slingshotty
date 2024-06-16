from enum import Enum
from entity import player as player_module
from entity import planet as planet_module
from util import *
from game import start_screen

class SpriteType(Enum):
    START_SCREEN = -1
    PLAYER = 0
    PLANET = 1
    EARTH = 2
    GAME_END = 3

class SpriteDetails:

    def __init__(self, sprite_type, image, pos, vel, w, h, mass=None):
        self.sprite_type = sprite_type
        self.image = image
        self.pos = pos
        self.vel = vel
        self.mass = mass
        self.w = w
        self.h = h

class Level:

    def __init__(self, info):
        self.info = info

levels = [
    None,
    Level([
        SpriteDetails(SpriteType.PLAYER, "assets/player.png", (100, 100), (0, 0), 64, 64),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (550, 250), (0, 0), 128, 128, mass=5000),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (250, 550), (0, 0), 128, 128, mass=5000),
        SpriteDetails(SpriteType.EARTH, "assets/earth.png", (1500, 900), (0, 0), 128, 128, mass=15000),
    ]),
    Level([
        SpriteDetails(SpriteType.PLAYER, "assets/player.png", (100, 100), (0, 0), 64, 64),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (250, 250), (0, 0), 128, 128, mass=5000),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (250, 550), (0, 0), 128, 128, mass=5000),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (550, 550), (0, 0), 128, 128, mass=5000),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (800, 600), (0, 0), 128, 128, mass=5000),
        SpriteDetails(SpriteType.EARTH, "assets/earth.png", (1500, 900), (0, 0), 128, 128, mass=10000),
    ]),
    Level([
        SpriteDetails(SpriteType.PLAYER, "assets/player.png", (100, 100), (0, 0), 80, 80),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (700, 500), (0, 0), 180, 180, 5000),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (1000, 200), (0, 0), 180, 180, 5000),
        SpriteDetails(SpriteType.EARTH, "assets/earth.png", (1700, 900), (0, 0), 136, 136, 5000)
    ]),
    Level([
        SpriteDetails(SpriteType.PLAYER, "assets/player.png", (100, 100), (0, 0), 80, 80),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (700, 500), (0, 0), 280, 280, 50000),
        SpriteDetails(SpriteType.EARTH, "assets/earth.png", (1700, 900), (0, 0), 136, 136, 5000)
    ]),
    Level([
        SpriteDetails(SpriteType.PLAYER, "assets/player.png", (100, 100), (0, 0), 80, 80),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (700, 500), (0, 0), 180, 180, 5000),
        SpriteDetails(SpriteType.PLANET, "assets/planet.png", (1000, 200), (0, 0), 180, 180, 5000),
        SpriteDetails(SpriteType.EARTH, "assets/earth.png", (1700, 900), (0, -1), 136, 136, 5000)
    ]),

    # Game end
    Level([
        SpriteDetails(SpriteType.PLAYER, "assets/endgame.png", (600, 300), (0, 0), 300, 200)
    ])
]

    
class MapLoader:

    def __init__(self, game):
        self.game = game

    def load(self, level):
        for sprite in level.info:
            match sprite.sprite_type:
                case SpriteType.PLAYER:
                    self.game.add_player(self.create_player(sprite))
                case SpriteType.PLANET:
                    planet = self.create_planet(sprite)
                    self.game.planets.append(planet)
                case SpriteType.EARTH:
                    earth = self.create_planet(sprite)
                    self.game.planets.append(earth)
                    self.game.earth = earth
                case SpriteType.START_SCREEN:
                    self.game.start_screen = start_screen.StartScreen(sprite.pos, sprite.w, sprite.h)

    
    def create_player(self, sprite):
        player = player_module.Player(
            "player", 
            Vector(sprite.pos[0], sprite.pos[1]),
            Vector(sprite.vel[0], sprite.vel[1]), 
            Vector(0, 0), 
            sprite.w, 
            sprite.h, 
            sprite.image
        )
        return player

    def create_planet(self, sprite):
        planet = planet_module.Planet(
            "planet",
            Vector(sprite.pos[0], sprite.pos[1]),
            Vector(sprite.vel[0], sprite.vel[1]), 
            Vector(0, 0),
            sprite.w,
            sprite.h,
            sprite.image,
            sprite.mass,
        )
        return planet