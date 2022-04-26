from tkinter import Y
from turtle import screensize
from xmlrpc.client import boolean
import pygame
from pygame.locals import *
from pygame.sprite import Group
from pygame.locals import *
import msvcrt
from astronaut import Player


EnableFullScreen = False

pygame.init()
info = pygame.display.Info()
SIZE = WIDTH, HEIGHT = info.current_w, info.current_h


class World:
    def __init__(self):
        DIM = 800
        self.DISPLAYSURF = pygame.display.set_mode(SIZE)
        self.background = pygame.image.load("./media/achtergrond3.jpg")
        self.background = pygame.transform.scale(self.background, SIZE)
        self.astronaut = Player()

    def act(self):
        self.DISPLAYSURF.blit(self.background, (0, 0))
        self.astronaut.move()
        self.astronaut.draw(self.DISPLAYSURF)
        self.astronaut.grow()

    def setFullScreen(self):
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
