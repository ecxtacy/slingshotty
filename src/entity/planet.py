from entity import entity

class Planet(entity.Entity):

    def __init__(self, name, position, velocity, acceleration, width, height, image_path, mass, radius=None):
        super().__init__(name, position, velocity, acceleration, width, height, image_path)
        self.mass = mass
        self.radius = radius

    def cleanup(self):
        pass
    