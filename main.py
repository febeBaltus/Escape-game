from json.encoder import ESCAPE
import pygame
from pygame.locals import *
from world import World
import sys
from pynput import keyboard

pygame.init()


FPS = pygame.time.Clock()

keys = pygame.key.get_pressed()
world = World()
pygame.display.set_caption("Escape-Game")


def quit():
    pygame.display.quit()
    pygame.quit()
    sys.exit()


while True:
    FPS.tick(30)
    world.act()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()

        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
