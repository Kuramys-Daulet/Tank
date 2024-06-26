import pygame
from pygame.sprite import Sprite

class Tank(Sprite):
    def __init__(self, screen):
        "иниицаллизация танка"
        super(Tank, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/tank.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def output(self):
        "рисование танка"
        self.screen.blit(self.image, self.rect)

    def update_tank(self):
        """обновление позиции танка"""
        if  self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        elif self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_tank(self):
        """"ortasinda tank"""
        self.center = self.screen_rect.centerx