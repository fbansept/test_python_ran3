import pygame
import random

class Balle :

    def __init__(self, programme):
        self.rayon = 30
        self.x = random.randint(self.rayon, programme.screen_width - self.rayon)
        self.y = random.randint(self.rayon, programme.screen_height - self.rayon)
        self.vitesse_x = random.randint(2,5)
        self.vitesse_y = random.randint(2,5)
        self.couleur = (random.randint(0,220), random.randint(0,220), random.randint(0,220))

    def dessiner(self, screen) :
        pygame.draw.circle(screen, 
                        self.couleur, 
                        (self.x, self.y),
                        self.rayon)
        
    def deplacement(self, programme) :
        self.x += self.vitesse_x
        self.y += self.vitesse_y

        if self.x <= self.rayon or self.x >= programme.screen_width - self.rayon :
            self.vitesse_x = -self.vitesse_x

        if self.y <= self.rayon or self.y >= programme.screen_height - self.rayon  :
            self.vitesse_y = -self.vitesse_y
