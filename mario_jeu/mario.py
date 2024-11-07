import math
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

        liste_collision = self.touche_plateforme(liste_plateformes)
        collision_verticale = False

        for plateforme_collision, direction_collision in liste_collision :
            if direction_collision == "HAUT" or direction_collision == "BAS" :
                collision_verticale = True

            if direction_collision == "HAUT" :
                self.y = plateforme_collision.y + plateforme_collision.hauteur

        if collision_verticale :
            self.vitesse_y = 0
        else :
            self.vitesse_y += 0.2

        if self.vitesse_y > 5 :
            self.vitesse_y = 5



    def touche_plateforme(self, liste_plateformes) :

        liste_plateforme_touche = []

        for plateforme in liste_plateformes :

            # on test si il y a une collision entre mario et la plateforme
            if self.y >= plateforme.y - self.hauteur and self.x + self.largeur >= plateforme.x and self.x <= plateforme.x + plateforme.largeur and (self.y + self.hauteur < plateforme.y + plateforme.hauteur or self.y < plateforme.y + plateforme.hauteur):

                # on test de quel côté mario a tapé la plateforme 
                # (la distance la plus courte entre les coté opposé des 2 rectangle)
                distance_droite = abs(self.x + self.largeur - plateforme.x)
                distance_gauche = abs(self.x - (plateforme.x + plateforme.largeur))
                distance_haut = abs(self.y - (plateforme.y + plateforme.hauteur))
                distance_bas = abs(self.y + self.hauteur - plateforme.y)

                minimum = min(distance_droite,distance_gauche,distance_haut,distance_bas)

                # on retourne un tuple avec la plateforme en collision et le coté touché de mario
                if distance_droite == minimum :
                    liste_plateforme_touche.append((plateforme, "DROITE"))
                elif distance_gauche == minimum :
                    liste_plateforme_touche.append((plateforme, "GAUCHE"))
                elif distance_haut == minimum :
                    liste_plateforme_touche.append((plateforme, "HAUT"))
                else :
                    liste_plateforme_touche.append((plateforme, "BAS"))
            
        return liste_plateforme_touche
        
