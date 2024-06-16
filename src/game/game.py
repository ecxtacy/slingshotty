import pygame
import random
from entity import player
from game import map_loader
import gc
from enum import Enum
import text
from game.start_screen import StartScreen


class GameStatus(Enum):
    RESTART = 1

class Game:

    def __init__(self, clock):
        self.clock = clock
        self.running = True

        self.stars = []
        self.drawn_stars = False
        self.star_brightness = []
        self.star_size = []

        self.planets = []
        self.earth = None
        self.paused = False
        self.current_level = 1
        self.loader = None
        self.start_screen = StartScreen((400, 250), 1000, 500)

    def load_text(self):
        self.restart_text = text.Text("Restart", None, 56, (255, 255, 255), (1700, 50))
        self.score_text = text.Text(f"Level: {self.current_level}", None, 48, (255, 255, 255), (1700, 120), underline=False)
        text.Text(f"Player: {self.start_screen.player_name}", None, 48, (125, 250, 100), (1700, 180))
    def load(self):
        self.load_text()
        self.loader = map_loader.MapLoader(self)
        self.loader.load(map_loader.levels[self.current_level])

    def set_fps(self, fps):
        self.fps = fps
        self.clock.tick(self.fps)
    
    def is_running(self):
        return self.running

    def stop(self):
        self.running = False

    def draw_stars(self, count, width, height):
        """

        Draw stars across the screen of given width and height.
        count number of stars to draw across width x height.
        """
        if not self.drawn_stars:    
            for i in range(count):
                bness = random.randint(30, 255)
                sz = random.randint(1, 2)
                x = random.randint(1, width)
                y = random.randint(1, height)
                pygame.draw.circle(Game.screen, (bness, bness, bness), (x, y), sz)
                self.star_brightness.append(bness)
                self.stars.append((x, y))
                self.star_size.append(sz)
            self.drawn_stars = True
        else:
            for i in range(0, len(self.stars)):
                b = self.star_brightness[i]
                star = self.stars[i]
                pygame.draw.circle(Game.screen, (b, b, b), (star[0], star[1]), self.star_size[i])

    def draw_slinger(self, start_pos):
        if self.player.slinger.mouse_holding:
            pygame.draw.line(Game.screen, (0, 0, 255), start_pos, pygame.mouse.get_pos(), 2)

    def add_player(self, player):
        self.player = player
    
    def add_planets(self, planets):
        self.planets = planets

    def pause(self):
        self.paused = True

    def render(self):
        if not self.start_screen.proceed:
            self.start_screen.render()
            return

        self.restart_text.render()
        self.score_text.render()

        # Name text
        text.Text(f"{self.start_screen.player_name}", None, 60, (125, 250, 100), (1650, 180)).render()

        self.earth.render()
        self.player.render()
        for planet in self.planets:
            planet.render()
        pass

    def update(self):

        self.score_text.update(f"Level: {self.current_level}")

        collision = self.player.handle_collision(self.planets, self.earth)
        if collision == player.CollisionType.NO_COLLISION:
            pass
        elif collision == player.CollisionType.EARTH:
            self.next_level()
            return
        elif collision == player.CollisionType.PLANET:
            self.restart_level()
            collision = player.CollisionType.NO_COLLISION
            return GameStatus.RESTART

        if self.player.slinger.player_launched:
            self.player.update(self.planets)
        for planet in self.planets:
            planet.update()
        pass

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.stop()

            if not self.start_screen.proceed:
                self.start_screen.handle_events(event)
                return

            # Game objects handle their respective events
            self.player.handle_events(event)
            self.restart_text.handle_events(event, self)

            for planet in self.planets:
                planet.handle_events(event)

            
    def next_level(self):
        self.cleanup()
        self.current_level += 1
        self.loader.load(map_loader.levels[self.current_level])

    def restart_level(self):
        self.cleanup()
        self.loader.load(map_loader.levels[self.current_level])

    def cleanup(self):
        self.player.cleanup()
        self.earth.cleanup()
        for planet in self.planets:
            planet.cleanup()
        self.planets = []
        self.player = None
        self.earth = None