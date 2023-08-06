# Programme principal du jeu
import random
import os
import pygame  # Importation du module Pygame
from tkinter import messagebox
pygame.init()  # Démarrer Pygame

# auteur = ["Cavazzano", "Rota", "Midthun"]


class Bouton:
    "Bouton"

    def __init__(self, x, y, width, height, text, onclick_function=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        print(self.text)
        self.onclick_function = onclick_function

        self.bouton_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.author_name = text.split(" ")[-1].lower()

    def draw(self, win, font):
        "Dessiner le bouton à l'écran"
        pygame.draw.rect(win, (100, 100, 100), self.bouton_rect)
        text_surf = font.render(self.text, True, (255, 255, 255))
        win.blit(text_surf, (self.x + (self.width / 2) - text_surf.get_width() / 2,
                             self.y + (self.height / 2) - text_surf.get_height()))

    def is_over(self, pos):
        return self.bouton_rect.collidepoint(pos)

    """def check_file(self, directory, string):
        "Vérifier si un fichier contient une chaîne de caractères précise dans son nom"
        for filename in os.listdir(directory):
            if string.lower() in filename.lower():
                return True
        return False"""

    def check_author(self, filename, string):
        "Vérifier si le bouton correspond avec l'auteur de l'image"

        if string.lower() in filename.lower():
            print("Bonne réponse !")
            return True
        else:
            print("Mauvaise réponse !")
            return False

    def click(self):
        if self.onclick_function is not None:
            self.onclick_function()


class Jeu:
    "Jeu"
# Fenêtre du jeu en plein écran

    def __init__(self):

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Guess the image !")

        # Appliquer un fond blanc à la fenêtre
        self.screen.fill((255, 255, 255))

        self.dossier_images = "images"  # Dossier des images
        # global liste_images
        self.liste_images = os.listdir(self.dossier_images)
        if self.liste_images == []:  # S'il n'y a pas d'images dans le dossier
            raise Exception(messagebox.showerror("Des images sont inexistantes ou introuvables",
                                                 "Le jeu n'a pas pû être exécuté en raison de l'absence d'images dans 'images'."))

        self.boutons = [Bouton(30 + i*190, 400, 180, 60, "Dessin par " + auteur.lower())
                        for i, auteur in enumerate(["Cavazanno", "Midthun", "Rota"])]

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
        # print(f"Image courante : {image}")
        self.screen.fill((255, 255, 255))
        chemin_image = os.path.join(self.dossier_images, image)
        image_chargee = pygame.image.load(chemin_image)
        # Obtenir la taille de la fenêtre
        # window_size = pygame.display.get_surface().get_size()
        image_chargee = pygame.transform.scale(image_chargee, (400, 300))

        self.screen.blit(image_chargee, (0, 0))  # Afficher l'image à l'écran

        font = pygame.font.Font(None, 15)
        for bouton in self.boutons:
            bouton.draw(self.screen, font)

        pygame.display.update()

    def image_generator(self, images):
        for image in images:
            yield image

    def start(self):
        "Démarrer le jeu"
        images = self.pick_images(3)
        print(images)
        image_gen = self.image_generator(images)
        current_image = next(image_gen, None)
        running = True  # Le jeu est-il en cours d'exécution ?

        while running:
            for evenement in pygame.event.get():  # Pour chaque évènement détecté dans la fenêtre de jeu
                if evenement.type == pygame.QUIT:  # Si le joueur veut quitter le jeu
                    ask_quit = messagebox.askquestion(
                        "Quitter le jeu maintenant", "Désirez-vous quitter le jeu ?")
                    if ask_quit == "yes":
                        running = False  # Terminer l'exécution de cette boucle, et, par conséquent, celle du jeu
                    else:
                        continue
                if evenement.type == pygame.MOUSEBUTTONDOWN:

                    for bouton in self.boutons:
                        if bouton.is_over(pygame.mouse.get_pos()):
                            author = current_image.split(
                                "_")[1].split(".")[0]
                            bouton.check_author(
                                current_image, author)

                            current_image = next(image_gen, None)

                if current_image is not None:
                    self.display_images_and_choices(
                        current_image, ["Choix 1", "Choix 2", "Choix 3"])

                pygame.display.update()


jeu = Jeu()
jeu.start()
