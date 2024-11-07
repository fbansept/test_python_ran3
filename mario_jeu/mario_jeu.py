import pygame
import sys

from mario import Mario
from plateforme import Plateforme

class JeuMario :

    def __init__(self):

        self.screen_width = 800
        self.screen_height = 600

        # Initialiser pygame
        pygame.init()

        # Définir les dimensions de la fenêtre
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Mario")

        white = (255, 255, 255)

        en_cours = True
        clock = pygame.time.Clock()

        mario = Mario(250,100)

        liste_plateformes = (Plateforme(200,400,400,30) , Plateforme(300,350,100,30))

        touche_droite_presse = False
        touche_gauche_presse = False
        touche_haut_presse = False

        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        touche_droite_presse = True
                    if event.key == pygame.K_LEFT:
                        touche_gauche_presse = True
                    if event.key == pygame.K_UP:
                        touche_haut_presse = True

                if event.type == pygame.KEYUP :
                    if event.key == pygame.K_RIGHT:
                        touche_droite_presse = False
                    if event.key == pygame.K_LEFT:
                        touche_gauche_presse = False
                    if event.key == pygame.K_UP:
                        touche_haut_presse = False
                

            liste_collision = mario.touche_plateforme(liste_plateformes)

            collision_droite = False
            collision_gauche = False
            collision_bas = False

            for plateforme_collision, direction_collision in liste_collision :
                if direction_collision == "DROITE" :
                    collision_droite = True
                elif direction_collision == "GAUCHE" :
                    collision_gauche = True
                elif direction_collision == "BAS" :
                    collision_bas = True


            if touche_droite_presse :
                if not collision_droite :
                    for plateforme in liste_plateformes :
                        plateforme.x -= 5

            if touche_gauche_presse :
                if not collision_gauche :
                    for plateforme in liste_plateformes :
                        plateforme.x += 5

            if touche_haut_presse :
                if collision_bas:
                    mario.vitesse_y = -7

            # Remplir l'écran et dessiner la balle
            screen.fill(white)

            mario.deplacement(liste_plateformes)
            mario.dessiner(screen)

            for plateforme in liste_plateformes :
                plateforme.dessiner(screen)
            
            # Rafraîchir l'affichage
            pygame.display.flip()

            # Contrôler la vitesse de la boucle
            clock.tick(60)

        # Quitter pygame
        pygame.quit()
        sys.exit()


#On appele la fonction init de la classe Jeu
JeuMario()