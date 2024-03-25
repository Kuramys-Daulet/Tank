import pygame
import sys
from bullet import Bullet
from enemy import Enemy
import time


def events(screen, tank, bullets):
    "обработка событии"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            # Оңға жылжу
            if event.key == pygame.K_d:
                tank.mright = True
            #Солға жылжу
            elif event.key == pygame.K_a:
                tank.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, tank)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Оңға жылжуды тоқтату
            if event.key == pygame.K_d:
                tank.mright = False
            # Солға жылжуды тоқтату
            elif event.key == pygame.K_a:
                tank.mleft = False

def update(bg_color, screen, stats, sc, tank, enemies, bullets):
    """Экранды жаңарту"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    tank.output()
    enemies.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc, enemies, bullets):
    #delet bullet
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, enemies, True, True)
    if collisions:
        for enemies in collisions.values():
            stats.score += 10 * len(enemies)
        sc.image_score()
        check_high_score(stats, sc)
        sc.image_tanks()
    if len(enemies) == 0:
        bullets.empty()
        create_army(screen, enemies)

def tank_kill(stats, screen, sc, tank, enemies, bullets):
    """Tankpen armya soggisui"""
    if stats.tanks_left > 0:
        stats.tanks_left -= 1
        sc.image_tanks()
        enemies.empty()
        bullets.empty()
        create_army(screen, enemies)
        tank.create_tank()
        time.sleep(1)
    else:
        stats.run_game = False
        sys.exit()



def update_enemies(stats, screen, sc, tank, enemies, bullets):
    enemies.update()

    if pygame.sprite.spritecollideany(tank, enemies):
        tank_kill(stats, screen, sc, tank, enemies, bullets)
    enemies_check(stats, screen, sc, tank, enemies, bullets)

def enemies_check(stats, screen, sc, tank, enemies, bullets):
    """Армия шектік линнияға жеткенін тексеру"""
    screen_rect = screen.get_rect()
    for enemy in enemies.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            tank_kill(stats, screen, sc, tank, enemies, bullets)
            break


def create_army(screen, enemies):
    # armia jasap jartitmiz
    enemy = Enemy(screen)
    enemy_width = enemy.rect.width
    number_enemy_x = int((800 - 2 * enemy_width) / enemy_width)
    enemy_height = enemy.rect.height
    number_enemy_y = int((800 - 100 - 2 * enemy_height) / enemy_height)

    for row_number in range(number_enemy_y - 2):
        for enemy_number in range(number_enemy_x):
            enemy = Enemy(screen)
            enemy.x = enemy_width + enemy_width * enemy_number
            enemy.y = enemy_height + enemy_height * row_number
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + enemy.rect.height * row_number
            enemies.add(enemy)

def check_high_score(stats, sc):
    """"proverka recodra"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))
