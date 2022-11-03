import pygame
import time
import random
pygame.init()

app_width = 800
app_height = 600

app = pygame.display.set_mode((app_width, app_height))
pygame.display.update()

pygame.display.set_caption('Snake')


green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)
yellow = (255,255,102)
blue = (50,153,213)


snake_block=10



clock = pygame.time.Clock()
snake_speed=20

font_style = pygame.font.SysFont("bahnschrift", 25, bold=False, italic=False)
score_font = pygame.font.SysFont("comicsansms", 35, bold=False, italic=False)

def snake(snake_block, snake_list):
    for a in snake_list:
        pygame.draw.rect(app, green, [a[0], a[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    app.blit(mesg, [app_width/3, app_height/3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = app_width/2
    y1 = app_height/2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    x_of_food = round(random.randrange(0, app_width - snake_block) / 10.0) * 10.0
    y_of_food = round(random.randrange(0, app_width - snake_block) / 10.0) * 10.0


    while not game_over:

        while game_close == True:
            app.fill(black)
            message("You LOST! Press Q-Quit A-Play Again", white)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
            
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= app_width or x1 < 0 or y1 >= app_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        app.fill(black)
        
        pygame.draw.rect(app, red, [x_of_food, y_of_food , snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == x_of_food and y1 == y_of_food:
            x_of_food = round(random.randrange(0, app_width - snake_block) / 10.0) * 10.0
            y_of_food = round(random.randrange(0, app_width - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)
    pygame.quit()
    quit()
gameLoop()
