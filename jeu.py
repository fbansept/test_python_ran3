import pygame
import sys
from balle import Balle

class Jeu :


    def __init__(self):

        self.screen_width = 800
        self.screen_height = 600

        # Initialiser pygame
        pygame.init()

        # Définir les dimensions de la fenêtre
        screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Aller-Retour d'une Balle")

        # Couleurs
        rouge = (255, 0, 0)
        white = (255, 255, 255)

        en_cours = True
        clock = pygame.time.Clock()

        liste_balle = []

        for index in range(100) :
            liste_balle.append(Balle(self))


        while en_cours:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    en_cours = False

            # Remplir l'écran et dessiner la balle
            screen.fill(white)

            for balle in liste_balle :
                balle.deplacement(self)
                balle.dessiner(screen)
            
            # Rafraîchir l'affichage
            pygame.display.flip()

            # Contrôler la vitesse de la boucle
            clock.tick(60)

        # Quitter pygame
        pygame.quit()
        sys.exit()


#On appele la fonction init de la classe Jeu
Jeu()