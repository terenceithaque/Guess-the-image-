# Programme principal du jeu
import random
import os
import pygame  # Importation du module Pygame
from tkinter import messagebox
pygame.init()  # Démarrer Pygame


class Jeu:
    "Jeu"
# Fenêtre du jeu en plein écran

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Guess the image !")

        self.dossier_images = "images"  # Dossier des images
        # global liste_images
        self.liste_images = os.listdir(self.dossier_images)
        if self.liste_images == []:  # S'il n'y a pas d'images dans le dossier
            raise Exception(messagebox.showerror("Des images sont inexistantes ou introuvables",
                                                 "Le jeu n'a pas pû être exécuté en raison de l'absence d'images dans 'images'."))

    def pick_images(self, images_to_pick):
        "Choisir plusieurs images au hasard dans liste_images"
        n_images_choisies = 0
        images_choisies = []  # Pour l'instant, aucune image n'a été choisie
        while n_images_choisies < images_to_pick:  # Tant qu'on n'a pas choisi autant d'images que demandé
            image = random.choice(self.liste_images)
            if image in images_choisies:  # Si on a déjà choisi la même image
                continue

            print(image)
            images_choisies.append(image)
            n_images_choisies += 1

        return images_choisies

    def display_images_and_choices(self, image, choices):
        "Afficher chaque image et les choix de réponse correspondants"
        # Charger et afficher l'image
        chemin_image = os.path.join(self.dossier_images, image)
        image_chargee = pygame.image.load(chemin_image)
        # Obtenir la taille de la fenêtre
        window_size = pygame.display.get_surface().get_size()
        pygame.transform.scale(image_chargee, window_size)
        self.screen.blit(image_chargee, (0, 0))  # Afficher l'image à l'écran

    def image_generator(self, images):
        for image in images:
            yield image

    def start(self):
        "Démarrer le jeu"
        images = self.pick_images(2)
        print(images)
        image_gen = self.image_generator(images)
        current_image = next(image_gen, None)
        running = True  # Le jeu est-il en cours d'exécution ?

        while running:
            for evenement in pygame.event.get():  # Pour chaque évènement détecté dans la fenêtre de jeu
                if evenement == pygame.QUIT:  # Si le joueur veut quitter le jeu
                    running = False  # Terminer l'exécution de cette boucle, et, par conséquent, celle du jeu

            if current_image is not None:
                self.display_images_and_choices(
                    current_image, ["Choix 1", "Choix 2", "Choix 3"])
            current_image = next(image_gen, None)

            pygame.display.update()


jeu = Jeu()
jeu.start()
