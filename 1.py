import pygame
from libc import *

ANCHO = 600
ALTO = 600
CENTRO = (ANCHO/2,ALTO/2)

if __name__ == '__main__':
    # Inicializacion Pantalla Pygame
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])
    reloj = pygame.time.Clock()

    x1 = -300
    y1 = 0

    x2 = 0
    y2 = 300

    pantalla.fill(NEGRO)
    # Mantener Pantalla Activa
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        # etapa 1
        while (x1 != 0):
            y1 = x1 + 300
            Punto1 = cart(CENTRO, [x1,y1])
            pygame.draw.circle(pantalla, AZULC, Punto1, 4)
            x1 = x1 + 1
            pygame.display.flip()
            pantalla.fill(NEGRO)
            reloj.tick(60)
        # etapa 2
        if x1 == 0:
            y2 = (-1) * x2 + 300
            Punto2 = cart(CENTRO, [x2,y2])
            pygame.draw.circle(pantalla, AZULC, Punto2, 4)
            x2 = x2 + 1
        pygame.display.flip()
        pantalla.fill(NEGRO)
        reloj.tick(60)
