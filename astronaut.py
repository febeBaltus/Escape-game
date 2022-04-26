import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.oorspronkelijk_image = pygame.image.load("astro.jpg")
        self.hoogte = self.oorspronkelijk_image.get_height()
        self.breedte = self.oorspronkelijk_image.get_width()
        self.image = pygame.transform.scale(self.oorspronkelijk_image, (self.breedte / 2, self.hoogte / 2))
        self.rect = self.image.get_rect()
        self.rect.center = (600, 600)
        self.schaal = 100
        self.breedte1 = self.image.get_width()
        self.hoogte1 = self.image.get_height()

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 25
        if keys[pygame.K_LEFT]:
            self.rect.x -= 25
        if keys[pygame.K_UP]:
            self.rect.y -= 25
        if keys[pygame.K_DOWN]:
            self.rect.y += 25

    def grow(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.image = pygame.transform.scale(self.image, (self.breedte1*self.schaal/100, self.hoogte1*self.schaal/100))
            self.schaal -= 5

        if keys[pygame.K_DOWN]:
            self.image = pygame.transform.scale(self.image, (self.breedte1*self.schaal/100, self.hoogte1*self.schaal/100))
            self.schaal += 5

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
