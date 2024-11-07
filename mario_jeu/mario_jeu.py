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

        mario = Mario(250,200)

        plateforme = Plateforme(200,400,300,30)

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
                

            if touche_droite_presse :
                plateforme.x -= 5

            # Remplir l'écran et dessiner la balle
            screen.fill(white)

            mario.deplacement(plateforme)
            mario.dessiner(screen)

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