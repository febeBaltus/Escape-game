import pygame


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("media/astro.jpg")
        self.hoogte = (self.image.get_height())/2
        self.breedte = (self.image.get_width())/2
        self.rect = self.image.get_rect()
        self.schaal = 100               # need to change scale "100" to picture format in order to prevent quality downgrade

        info = pygame.display.Info()    # getting display information for positioning the player at the same spot on any device
        X = int((info.current_w)/2)     # turning a float in to an integer to enable the working of the "self.rect.center" (center won't work on floads)
        Y = int((info.current_h)*3/4)   # fload --> int, also: position "Y" *=3/4 of display height (for "X" /= 2 display with)
        self.rect.center = (X, Y)       # positioning the player

        
    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.rect.x += 30
        if keys[pygame.K_LEFT]:
            self.rect.x -= 30
        if keys[pygame.K_UP]:
            self.rect.y -= 30
        if keys[pygame.K_DOWN]:
            self.rect.y += 30

    def grow(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.image = pygame.transform.scale(self.image, (self.breedte*self.schaal/100, self.hoogte*self.schaal/100))
            self.schaal /= 1.25
        if keys[pygame.K_DOWN]:
            self.image = pygame.transform.scale(self.image, (self.breedte*self.schaal/100, self.hoogte*self.schaal/100))
            self.schaal *= 1.25

    def draw(self, surface):
        surface.blit(self.image, (self.rect.x, self.rect.y))
