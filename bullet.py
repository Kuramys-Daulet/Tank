import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, tank):
        # making bullet from gun
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 5, 50)
        self.color = 0, 0, 0
        self.speed = 4.5
        self.rect.centerx = tank.rect.centerx
        self.rect.top = tank.rect.top
        self.y = float(self.rect.y)

    def update(self):
        # bullet up
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        # draw bullet
        pygame.draw.rect(self.screen, self.color, self.rect)