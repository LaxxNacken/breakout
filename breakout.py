import pygame
import time

window_width = 500
window_height = 500

global paddle_position1
paddle_position1 = [210, 490]
global paddle_position2
paddle_position2 = [290, 490]
ball_position = [240, 250]
ball_move = [2, 2]

pygame.init()
pygame.joystick.init()
pygame.display.set_caption("Breakout!")
window = pygame.display.set_mode((window_width, window_height))
FPS = pygame.time.Clock()


def ball_collision():
    global ball_move
    if ball_position[1] > paddle_position1[1] - 10 and ball_position[0] > paddle_position1[0] and ball_position[0] < \
            paddle_position2[0]:
        ball_move[1] *= -1
    if ball_position[0] > window_width - 10 or ball_position[0] < 0 + 10:
        ball_move[0] *= -1
    if ball_position[1] < 0 + 10:
        ball_move[1] *= -1

def ball_movement():
    ball_position[0] = ball_position[0] + ball_move[0]
    ball_position[1] = ball_position[1] + ball_move[1]


def draw_stuff():
    window.fill(pygame.Color(0, 0, 0))
    pygame.draw.rect(window, pygame.Color(0, 0, 255), (paddle_position1[0], paddle_position1[1], 80, 10))
    pygame.draw.circle(window, pygame.Color(255, 0, 0), (int(ball_position[0]), int(ball_position[1])), int(10))


def game_over():
    if ball_position[1] > 490:
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
                        paddle_position1[0] += 10
                        paddle_position2[0] += 10
                    if axis < 0.0:
                        paddle_position1[0] -= 10
                        paddle_position2[0] -= 10
        ball_movement()
        ball_collision()
        game_over()
        draw_stuff()
        pygame.display.update()
        FPS.tick(60)

game_loop()
