import pygame
import time

window_width = 500
window_height = 500


global paddle_position
paddle_position = [210, 450] 
ball_position = [250, 250]

pygame.init()
pygame.joystick.init()
pygame.display.set_caption("Breakout!")
window = pygame.display.set_mode((window_width, window_height)) 



def ball_collision():
    global ball_position
    if ball_position[1] == paddle_position[1] and ball_position[0] == ball_position[0]:
        ball_position[0] *= -1
        ball_position[1] *= -1


def ball_movement():
    ball_position[0] += 2
    ball_position[1] += 2
    print(ball_position)

def draw_stuff():
    window.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(window, pygame.Color(0, 0, 255), (paddle_position[0], paddle_position[1], 80, 10))
    pygame.draw.circle(window, pygame.Color(255, 0, 0),(ball_position[0], ball_position[1]), int(10))    

def game_over():
    if ball_position[1] > window_height - 10:
        game_over_message()

def game_over_message():
    font = pygame.font.SysFont("Comic Sans", 30)
    render = font.render("Game Over", True, pygame.Color(255, 255, 255))
    rect = render.get_rect()
    rect.midtop = (window_width / 2, window_height / 2)
    window.blit(render, rect)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()
    exit(0)


def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
             joystick = pygame.joystick.Joystick(i)
             joystick.init()
             axes = joystick.get_numaxes()
             for i in range(axes):
                 axis = joystick.get_axis(i)
                 if i == 0:
                     if axis > 0.0:
                        paddle_position[0] += 10
                     if axis < 0.0:
                        paddle_position[0] -= 10
        ball_collision()
        ball_movement()
        game_over()
        draw_stuff()
        pygame.display.update()
        
game_loop()

