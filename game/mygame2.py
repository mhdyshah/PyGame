import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()


display = pygame.display.set_mode((800, 600))
icon_image = pygame.image.load("images/a.png")
"""music1 = pygame.mixer.Sound("music/filename.wav")
music1.play()
game_sound = pygame.mixer.music.load("music/a.mp3")
pygame.mixer.music.play(-1)"""


pygame.display.set_icon(icon_image)
pygame.display.set_caption("SimpleGame")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 40)
font2 = pygame.font.Font(None, 80)

black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
player_position = [370, 500]
enemy_position = [random.randint(0, 740), 0]
player_speed = 50
enemy_speed = 5
fps = 60
game_over = False
enemy_l = [enemy_position]
score = 0
stop = False


def collision(player_pos, enemy_pos):
    player_x = player_pos[0]
    player_y = player_pos[1]
    enemy_x = enemy_pos[0]
    enemy_y = enemy_pos[1]
    if (player_x <= enemy_x < (player_x + 60)) or (enemy_x <= player_x < (enemy_x + 60)):
        if (player_y <= enemy_y < (player_y + 60)) or (enemy_y <= player_y < (enemy_y + 60)):
            return True
        else:
            return False


def enemies(enemy_list):
    a = random.randint(0, 5)
    if len(enemy_list) <= 5 and a < 1:
        x_pos = random.randint(0, 740)
        y_pos = 0
        enemy_list.append([x_pos, y_pos])


def draw_enemies(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(display, red, (enemy[0], enemy[1], 60, 60))


def enemy_pos_update(enemy_list, score):
    for index, enemy_position in enumerate(enemy_list):
        if 0 <= enemy_position[1] <= 600:
            enemy_position[1] += enemy_speed
        else:
            enemy_list.pop(index)
            score += 1
    return score


def check_collision(enemy_list, player_pos):
    for enemy in enemy_list:
        if collision(enemy, player_pos):
            return True
    return False


def level(scr, spd):
    if scr <= 10:
        spd = 4
    elif scr <= 20:
        spd = 6
    elif scr <= 40:
        spd = 8
    elif scr <= 60:
        spd = 12
    elif scr <= 100:
        spd = 18
    else:
        spd = 25
    return spd


def game_opening():
    font3 = pygame.font.Font(None, 500)
    text_s = font3.render("3", True, red)
    display.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    display.fill((68, 105, 14))

    text_s = font3.render("2", True, red)
    display.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    display.fill((68, 105, 14))

    text_s = font3.render("1", True, red)
    display.blit(text_s, (300, 150))
    pygame.display.update()
    time.sleep(1)
    display.fill((68, 105, 14))

    text_s = font3.render("GO", True, red)
    display.blit(text_s, (150, 150))
    pygame.display.update()
    time.sleep(1)
    display.fill((68, 105, 14))


game_opening()
"""game_sound = pygame.mixer.music.load("music/a.mp3")
pygame.mixer.music.play(-1)"""
music1 = pygame.mixer.Sound("music/a.wav")
music1.play(-1)


def stop_function(stp):
    while stp:
        font4 = pygame.font.Font(None, 100)
        txt_surface = font4.render("Pause", True, (100, 15, 105))
        display.blit(txt_surface, (300, 250))
        for evt in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if evt.type == KEYDOWN:
                if event.key == K_SPACE:
                    stp = False
        pygame.display.update()


while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player_position[0] += player_speed
            if event.key == K_LEFT:
                player_position[0] -= player_speed
            if event.key == K_UP:
                player_position[1] -= player_speed
            if event.key == K_DOWN:
                player_position[1] += player_speed
            if event.key == K_SPACE:
                stop = True
                stop_function(stop)

    """if collision(player_position, enemy_position):
        game_over = True
        break"""
    if check_collision(enemy_l, player_position):
        game_over_sound = pygame.mixer.music.load("music/b.wav")
        pygame.mixer.music.play()
        t_s2 = font2.render("Game Over", True, (15, 0, 0))
        display.blit(t_s2, (240, 270))
        t_s = font.render("Your Finally Score Is : " +
                          str(score), True, (25, 51, 10))
        display.blit(t_s, (240, 320))
        pygame.display.update()
        time.sleep(3)
        game_over = True
        break
    if player_position[0] <= 0:
        player_position[0] = 0
    if player_position[0] >= 740:
        player_position[0] = 740
    if player_position[1] <= 0:
        player_position[1] = 0
    if player_position[1] >= 540:
        player_position[1] = 540

    """enemy_position[1] += enemy_speed
    if enemy_position[1] == 600:
        enemy_position[1] = 0"""
    """if (enemy_position[1] >= 0) and (enemy_position[1] <= 600):
        enemy_position[1] += enemy_speed
    else:
        enemy_position[1] = 0
        enemy_position[0] = random.randint(0, 740)"""

    display.fill((68, 105, 14))
    enemies(enemy_l)
    draw_enemies(enemy_l)
    pygame.draw.rect(
        display, blue, (player_position[0], player_position[1], 60, 60))
    score = enemy_pos_update(enemy_l, score)
    t_s = font.render("Your Score Is : " + str(score), True, (238, 177, 39))
    display.blit(t_s, (20, 20))
    enemy_speed = level(score, enemy_speed)
    pygame.draw.rect(
        display, blue, (player_position[0], player_position[1], 60, 60))
    clock.tick(fps)
    pygame.display.update()
