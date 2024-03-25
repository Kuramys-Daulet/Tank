import pygame, controls
from tank import Tank
from pygame.sprite import Group
from stats import Stats
from scores import Scores




def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("Жауынгер Танк")
    bg_color = (252, 186, 3)
    tank = Tank(screen)
    bullets = Group()
    enemies = Group()
    controls.create_army(screen, enemies)
    stats = Stats()
    sc = Scores(screen, stats)
    bg_song = pygame.mixer.Sound('muic/main_song.mp3')
    bg_song.play(loops=-1)

    while True:
        controls.events(screen, tank, bullets)
        if stats.run_game:
            tank.update_tank()
            controls.update(bg_color, screen, stats, sc, tank, enemies, bullets)
            controls.update_bullets(screen, stats, sc, enemies, bullets)
            controls.update_enemies(stats, screen, sc, tank, enemies, bullets)


run()