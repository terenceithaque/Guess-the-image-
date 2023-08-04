# Programme principal du jeu
import pygame  # Importation du module Pygame
pygame.init()  # Démarrer Pygame

screen = pygame.display.set_mode(size=(400, 400))  # Fenêtre du jeu
pygame.display.set_caption("Guess the image !")

running = True  # Le jeu est-il en cours d'exécution ?


while running:
    for evenement in pygame.event.get():  # Pour chaque évènement détecté dans la fenêtre de jeu
        if evenement == pygame.QUIT:  # Si le joueur veut quitter le jeu
            running = False  # Terminer l'exécution de cette boucle, et, par conséquent, celle du jeu
