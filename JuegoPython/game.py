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

# while 1:
#     clock.tick(23)
#
#     # APPENDING  THE IMAGE TO THE BACK OF THE SAME IMAGE
# #     i =0
#     while i < tiles:
#         screen.blit(bg, (bg.get_width() * i + scroll, 0))
#         i += 1
#     # FRAME FOR SCROLLING
#     scroll -= 6
#
#     # RESET THE SCROLL FRAME
#     if abs(scroll) > bg.get_width():
#         scroll = 0
#     py.display.update()


while running:
    # para el background infi

    i = 0
    while i < tiles:
        screen.blit(bg, (bg.get_width() * i + scroll, 0))
        i += 1
    scroll -= 6

    # RESET THE SCROLL FRAME
    if abs(scroll) > bg.get_width():
        scroll = 0
    py.display.update()

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    clock.tick(30)  # limits FPS to 60

py.quit()