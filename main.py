import pygame
import sys
import random
from pygame.locals import *

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Mienteme')

# Carga de imágenes
image1 = pygame.image.load('C:\\Users\\Gris\\Documents\\src\\lietome\\imagen1.jpg')
image2 = pygame.image.load('C:\\Users\\Gris\\Documents\\src\\lietome\\imagen2.jpg')

# Fuente de texto
font = pygame.font.Font(None, 36)

# Variables de control
current_image = image1
start_time = pygame.time.get_ticks()
image_duration = random.randint(1, 33) * 10  # Duración de imagen 1 entre 1 y 33 segundos en milisegundos
transition_duration = random.uniform(0.0033, 0.033) * 10  # Duración de transición entre 0.0033 y 0.033 segundos en milisegundos
final_duration = random.randint(3, 33) * 10  # Duración de imagen 1 después de la transición entre 3 y 33 segundos en milisegundos

# Variables para preguntas y respuestas
correct_answer = 7  # La respuesta correcta es la opción 7
options = list(range(1, 8))  # Genera las opciones del 1 al 7
user_answer = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key in [K_1, K_2, K_3, K_4, K_5, K_6, K_7]:
                user_answer = int(pygame.key.name(event.key))

    elapsed_time = pygame.time.get_ticks() - start_time

    if elapsed_time < image_duration:
        screen.blit(current_image, (0, 0))
    elif elapsed_time < image_duration + transition_duration:
        alpha = min(255, int((elapsed_time - image_duration) / transition_duration * 255))
        temp_image = current_image.copy()
        temp_image.set_alpha(alpha)
        screen.blit(temp_image, (0, 0))
    elif elapsed_time < image_duration + transition_duration + final_duration:
        screen.blit(current_image, (0, 0))
    else:
        current_image = image1 if current_image == image2 else image2
        start_time = pygame.time.get_ticks()
        image_duration = random.randint(1, 33) * 10
        transition_duration = random.uniform(0.0033, 0.033) * 10
        final_duration = random.randint(3, 33) * 10
        user_answer = None  # Reinicia la respuesta del usuario

    # Muestra las opciones si no se ha respondido aún
    if user_answer is None:
        text = font.render("Elige la opción correcta (1-7):", True, (255, 255, 255))
        screen.blit(text, (20, 20))
        for i, option in enumerate(options):
            text = font.render(f"{option}", True, (255, 255, 255))
            screen.blit(text, (50 + i * 50, 70))

    # Comprueba la respuesta del usuario
    if user_answer == correct_answer:
        text = font.render("Correcto", True, (0, 255, 0))
        screen.blit(text, (width // 2 - 50, height // 2))
    elif user_answer is not None:
        text = font.render("Incorrecto", True, (255, 0, 0))
        screen.blit(text, (width // 2 - 60, height // 2))

    pygame.display.flip()

# Cierra Pygame
pygame.quit()
sys.exit()
