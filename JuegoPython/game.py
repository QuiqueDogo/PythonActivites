#importacion
import pygame as py
import math

#inicialiizamos
py.init()
# screen = py.display.set_mode((1280, 720))
FrameHeight = 720
FrameWidth = 1280
screen = py.display.set_mode((FrameWidth, FrameHeight))
clock = py.time.Clock()
bg = py.image.load("mariolevel.jpg").convert()

running = True
scroll = 0
# HERE 1 IS THE CONSTATNT FOR REMOVING BUFFERING
tiles = math.ceil(FrameWidth  /bg.get_width()) + 1

py.display.set_caption("Intento de Flappy bird")


import os

class Player(py.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = py.image.load("bird.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.vel_y = 0
        self.gravity = 0.8
        self.jump_force = -12

    def update(self, keys):

        self.vel_y += self.gravity
        self.rect.y += self.vel_y


        if keys[py.K_SPACE]:
            self.vel_y = self.jump_force


        if self.rect.bottom > FrameHeight:
            self.rect.bottom = FrameHeight
            self.vel_y = 0
        if self.rect.top < 0:
            self.rect.top = 0
            self.vel_y = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

player = Player(0,0)
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = py.sprite.Group()
player_list.add(player)

while running:
    # para el background infi

    i = 0
    while i < tiles:
        screen.blit(bg, (bg.get_width() * i + scroll, 0))
        i += 1
    scroll -= 2

    # RESET THE SCROLL FRAME
    if abs(scroll) > bg.get_width():
        scroll = 0


    keys = py.key.get_pressed()
    player.update(keys)
    player.draw(screen)

    py.display.update()

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    clock.tick(30)  # limits FPS to 60

py.quit()