import pygame
import sys
import random 

pygame.init()

Width = 850

Length = 650

Speed = 5
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
White = (255,255,255)
Black = (0,0,0)
player_pos = [400,550]
player_size = [50,70]
enemy_size = [50,70]
enemy_pos = [random.randint(0,Width-enemy_size[0]), 20]
enemy_list = [enemy_pos]

screen = pygame.display.set_mode((Width,Length))

Fps = pygame.time.Clock()

game_over = False

def drop_enemies(enemy_list):
    if len(enemy_list) < 10:
        x_pos = random.randint(0,Width-enemy_size[0]
        enemy_list.append([x_pos,20])
def draw_enemies(enemy_list):
    for enemy_pos in enemy_list:
        pygame.draw.rect(screen,Red,(enemy_pos[0],enemy_pos[1],enemy_size[0],enemy_size[1]))
def update_enemies(enemy_list):
    for idx,enemy_pos in enumerate(enemy_list):
        if enemy_pos[1] >= 0 and enemy_pos[1] < Length:
            enemy_pos[1] += Speed
        else:
            enemy_list.pop(idx)
def check_collision(enemy_list,player_pos):
    for enemy_pos in enemy_list:
        if collision_detect(enemy_pos,player_pos)
            return True
    return False
        


def collision_detect(player_pos,enemy_pos):
    p_x = player_pos[0]
    p_y = player_pos[1]
    
    e_x = enemy_pos[0]
    e_y = enemy_pos[1]
    if e_x >= p_x and e_x < (p_x + player_size[0]) or p_x >= e_x and p_x < (e_x + enemy_size[0]):
        if e_y >= p_y and e_y < (p_y + player_size[1]) or p_y >= e_y and p_y < (e_y + enemy_size[1]):
            return True
    return False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player_pos[0]
            y = player_pos[1]
            if event.key == pygame.K_LEFT:
                x -= player_size[0]
            elif event.key == pygame.K_RIGHT:
                x += player_size[0]
            player_pos = [x,y]
    screen.fill(Black) 
    
    if collision_detect(player_pos,enemy_pos):
        screen.fill(Red)
        game_over = True
    Fps.tick(30)
    drop_enemies(enemy_list)
    update_enemies(enemy_list) 
    if check_collision(enemy_list,player_pos):
        screen.fill(Red)
        game_over = True
    draw_enemies(enemy_list) 
       
    pygame.draw.rect(screen,Blue,(player_pos[0],player_pos[1],player_size[0],player_size[1]))
    pygame.display.update()