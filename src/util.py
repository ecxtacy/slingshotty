import math
from collections import deque
from game import game as game_module
import pygame

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __sub__(self, other):
        temp = Vector(self.x - other.x, self.y - other.y)
        return temp

    # Overload the += operator
    def __iadd__(self, v2):
        if not isinstance(v2, Vector):
            return NotImplemented

        self.x += v2.x
        self.y += v2.y
        return self
    
    def __imul__(self, v2):
        if not isinstance(v2, Vector):
            return NotImplemented

        self.x *= v2.x
        self.y *= v2.y
        return self

    def __isub__(self, v2):
        if not isinstance(v2, Vector):
            return NotImplemented

        self.x -= v2.x
        self.y -= v2.y
        return self

    def get_magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def __str__(self):
        return f"( {self.x} <i>, {self.y} <j> )"

def get_unit_vector(vec):
    x = vec.x
    y = vec.y
    denom = math.sqrt(x*x + y*y)
    return Vector(x/denom, y/denom)

def distance(v1, v2):
    x1, y1 = v1
    x2, y2 = v2
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


class Trial:
    def __init__(self, limit, color):
        self.limit = limit
        self.points = deque()
        self.color = color

    def cleanup(self):
        self.points = None
        pass
    
    def append(self, point):
        self.points.append(point)
        if len(self.points) > self.limit:
            self.points.popleft()
    
    def render(self):
        for point in self.points:
            pygame.draw.circle(game_module.Game.screen, self.color, (point[0], point[1]), 2)

    