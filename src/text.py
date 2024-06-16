from game import game as game_module
import pygame

class Text:
    def __init__(self, text, font, size, color, pos, underline=False):
        self.font = font
        tmp_fnt = pygame.font.Font(font, size)
        tmp_fnt.underline = underline
        self.underline = underline
        self.text = tmp_fnt.render(text, True, color)
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]
        self.w = self.text.get_width()
        self.h = self.text.get_height()
        self.size = size
        self.color = color

    def update(self, new_text):
        font = pygame.font.Font(self.font, self.size)
        font.underline = self.underline
        self.text = font.render(new_text, True, self.color)
        self.w = self.text.get_width()
        self.h = self.text.get_height()
        pass

    def handle_events(self, event, game):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if(x > self.pos[0] and x < self.pos[0] + self.w or y > self.pos[1] and y < self.pos[1] + self.h):
                game.restart_level()
            pass
        pass

    def render(self):
        game_module.Game.screen.blit(self.text, self.pos)

    def cleanup(self):
        pass
