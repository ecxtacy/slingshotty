import pygame
from game import game as game_module
from text import Text

class StartScreen:

    def __init__(self, pos, width, height):
        self.x, self.y = pos[0], pos[1]
        self.w = width
        self.h = height
        self.proceed = False
        self.player_name = ""
        self.heading_text = Text("Enter your name", None, 76, (200, 200, 200), (self.x + 7*self.w/24, self.y + 50))
        self.enter_button = Text("Enter", None, 40, (100, 200, 100), (25*self.x // 12, self.y + 350), underline = True)
        pass

    def update(self):
        pass

    def render(self):
        # Render the borders
        pygame.draw.line(game_module.Game.screen, (200, 200, 200), (self.x, self.y), (self.x + self.w, self.y), 5)
        pygame.draw.line(game_module.Game.screen, (200, 200, 200), (self.x, self.y), (self.x, self.y + self.h), 5)
        pygame.draw.line(game_module.Game.screen, (200, 200, 200), (self.x + self.w, self.y), (self.x + self.w, self.y + self.h), 5)
        pygame.draw.line(game_module.Game.screen, (200, 200, 200), (self.x, self.y + self.h), (self.x + self.w, self.y + self.h), 5)
        
        self.heading_text.render()
        self.enter_button.render()
        Text(self.player_name, None, 58, (200, 200, 100), (23*self.x // 12, self.y + 200)).render()
        pass

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            enter_button_rect = self.enter_button.text.get_rect()
            p, q = self.enter_button.x, self.enter_button.y
            w, h = enter_button_rect.w, enter_button_rect.h
            if x > p and x < p + w and y > q and y < q + h:
                if len(self.player_name) > 0:
                    self.proceed = True
        elif event.type == pygame.KEYDOWN:
            if pygame.K_0 <= event.key <= pygame.K_9 or pygame.K_a <= event.key <= pygame.K_z:
                self.player_name += chr(event.key)
            elif event.key == pygame.K_BACKSPACE:
                self.player_name = self.player_name[:-1]
            elif event.key == pygame.K_SPACE:
                self.player_name += ' '
        pass

    def cleanup(self):
        self.pos = None
        self.width = None
        self.height = None