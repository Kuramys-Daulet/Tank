import pygame.font
from tank import Tank
from pygame.sprite import Group

class Scores():
    """igrovaya info"""
    def __init__(self, screen, stats):
        """ұпай санауды іске қосу"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()
        self.image_tanks()

    def image_score(self):
        """преобразовает текст счета в графмическое изображение"""
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (252, 186, 3))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_high_score(self):
        """max score"""
        self.high_score_image = self.font.render(str(self.stats.high_score), True, self.text_color, (252, 186, 3))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_tanks(self):
        """"kolicshve life"""
        self.tanks = Group()
        for tank_number in range(self.stats.tanks_left):
            tank = Tank(self.screen)
            tank.rect.x = 15 + tank_number * tank.rect.width
            tank.rect.y = 20
            self.tanks.add(tank)

    def show_score(self):
        """vivod sheta"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.tanks.draw(self.screen)

