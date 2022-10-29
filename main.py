import pygame
import time
pygame.init()

app_width = 800
app_height = 600

app = pygame.display.set_mode((app_width, app_height))
pygame.display.update()

pygame.display.set_caption('Snake')
game_over=False

green=(0,255,0)
red=(255,0,0)
white=(255,255,255)
black=(0,0,0)

x1 = app_width/2
y1 = app_height/2

snake_block=10

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()
snake_speed=30

font_style = pygame.font.SysFont(None, 50, bold=False, italic=False)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    app.blit(mesg, [app_width/2, app_height/2])

while not game_over:
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
        game_over = True

    x1 += x1_change
    y1 += y1_change
    app.fill(white)
    pygame.draw.rect(app, green, [x1,y1,snake_block,snake_block])

    pygame.display.update()

    clock.tick(snake_speed)

message("You lost", red)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()