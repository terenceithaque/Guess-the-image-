# Programme principal du jeu
import random
import os
import pygame  # Importation du module Pygame
from tkinter import messagebox
pygame.init()  # Démarrer Pygame

screen = pygame.display.set_mode(size=(400, 400))  # Fenêtre du jeu
pygame.display.set_caption("Guess the image !")

dossier_images = "images"  # Dossier des images
liste_images = os.listdir(dossier_images)
if liste_images == []:  # S'il n'y a pas d'images dans le dossier
    raise Exception(messagebox.showerror("Des images sont inexistantes ou introuvables",
                    "Le jeu n'a pas pû être exécuté en raison de l'absence d'images dans 'images'."))


def pick_images(images_to_pick):
    "Choisir plusieurs images au hasard dans liste_images"
    n_images_choisies = 0
    images_choisies = []  # Pour l'instant, aucune image n'a été choisie
    while n_images_choisies < images_to_pick:  # Tant qu'on n'a pas choisi autant d'images que demandé
        image = random.choice(liste_images)
        images_choisies.append(image)
        n_images_choisies += 1

    return images_choisies


images = pick_images(1)
print(images)
running = True  # Le jeu est-il en cours d'exécution ?


while running:
    for evenement in pygame.event.get():  # Pour chaque évènement détecté dans la fenêtre de jeu
        if evenement == pygame.QUIT:  # Si le joueur veut quitter le jeu
            running = False  # Terminer l'exécution de cette boucle, et, par conséquent, celle du jeu
