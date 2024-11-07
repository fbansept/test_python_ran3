import pygame

class Plateforme :

    def __init__(self, x, y, largeur, hauteur):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = (0,0,255)

    def dessiner(self, screen) :
        pygame.draw.rect(
            screen,
            self.couleur,
            (self.x, 
             self.y, 
             self.largeur, 
             self.hauteur))