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
        
    def deplacement(self, liste_plateformes) :
  
        self.y += self.vitesse_y

        if self.touche_plateforme(liste_plateformes) :
            self.vitesse_y = 0
        else :
            self.vitesse_y += 0.2

        if self.vitesse_y > 5 :
            self.vitesse_y = 5



    def touche_plateforme(self, liste_plateformes) :

        for plateforme in liste_plateformes :
            if self.y >= plateforme.y - self.hauteur and self.x + self.largeur >= plateforme.x and self.x <= plateforme.x + plateforme.largeur :
                return True
            
        return False
        
