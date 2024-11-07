import pygame

class Mario :

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hauteur = 60
        self.largeur = 30
        self.vitesse_y = 5

    def dessiner(self, screen) :
        pygame.draw.rect(
            screen,(255,0,0),
            (self.x, 
             self.y, 
             self.largeur, 
             self.hauteur))
        
    def deplacement(self, programme) :
        self.y += self.vitesse_y

        if self.y >= programme.screen_height - self.hauteur :
            self.vitesse_y = 0
        
