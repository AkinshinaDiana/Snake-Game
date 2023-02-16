import random
import time
import sys
import pygame
pygame.init()

YELLOW = (242, 242, 228)
GREEN = (0, 212, 78)
BLACK = (0, 0, 0)
BLUE = (16, 134, 244)
RED = (245, 37, 37)
ORANGE = (245, 137, 22)

W = 10
H = 10
x = 300
y = 200
x_change = 0
y_change = 0
score = 0
len_snake = 1
list_snake = []

playing_surface = pygame.display.set_mode((600, 400))
pygame.display.set_caption("My Snake (by Diana_Akinshina)")
# pygame.display.set_icon(pygame.image.load('icon_snake.png'))
clock = pygame.time.Clock()
FPS = 10



score_font = pygame.font.SysFont("comicsansms", 20)
message_font = pygame.font.SysFont('monotypecorsiva', 25)

food = pygame.Surface((10, 10))
food.fill(BLACK)
rect_food = food.get_rect()
food_possition = [random.randrange(0, 590, 10), random.randrange(0, 390, 10)]

gameRunning = True


while gameRunning:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            gameRunning = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                x_change = 0
                y_change = -10
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = 10
            elif event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0
            elif event.key == pygame.K_ESCAPE:
                gameRunning = False
            elif event.key == pygame.K_SPACE:
                gameRunning == True
                



    x += x_change
    y += y_change

    playing_surface.fill(YELLOW)
    value = score_font.render("Score:  "+ str(score),1, BLUE)
    value.set_alpha(70)
    playing_surface.blit(value, (0, 0))
    snake = pygame.Surface((W,H))
    snake.fill(GREEN)
    rect_snake = snake.get_rect()
    playing_surface.blit(snake, (x, y))
    playing_surface.blit(food, (food_possition[0], food_possition[1]))

    snake_Head = []
    snake_Head.append(x)
    snake_Head.append(y)
    list_snake.append(snake_Head)
    if len(list_snake) > len_snake:
        del list_snake[0]

    if x == food_possition[0] and y == food_possition[1]:
        food_possition = [random.randrange(0, 590, 10), random.randrange(0, 390, 10)]
        pygame.draw.rect(playing_surface, BLACK, (food_possition[0], food_possition[1], 10, 10))
        len_snake +=1
        score += 100

    for i in list_snake:
         pygame.draw.rect(playing_surface, GREEN, [i[0], i[1], 10, 10])

    if any((x >= 600, x < 0, y >= 400, y < 0, x == snake_Head)):
        game_over_msg1 = message_font.render("Игра окончена! Вы проиграли! Ваш счет  "+str(score)+"  очков", 1, RED)
        game_over_msg2 = message_font.render("Нажмите Esc - для выхода или Пробел - начать заново", 1, ORANGE)
        playing_surface.fill(YELLOW)
        playing_surface.blit(game_over_msg1, (50, 150))
        playing_surface.blit(game_over_msg2, (30, 200))
    pygame.display.update()
    clock.tick(FPS)
