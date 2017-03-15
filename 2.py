import pygame
from libc import *

ANCHO = 600
ALTO = 600
CENTRO = (ANCHO/2,ALTO/2)

if __name__ == '__main__':
    # Inicializacion Pantalla Pygame
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO, ALTO])

    # Dibujar plano cartesiano
    planoCartesiano(ANCHO,ALTO,pantalla)
    r = 100
    PuntoL = [[0,0], [r, 0]]
    d = PuntoL[0]
    ang1 = 45
    pygame.display.flip()
    PuntoR = rotacionPunto(PuntoL[1], d, ang1)
    linea(pantalla, AZUL, cart(CENTRO,PuntoL[0]), cart(CENTRO,PuntoR))
    ang2 = 45

    # Mantener Pantalla Activa
    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
        while (ang2 != 91):
            PuntoC = rotacionPolares(r, ang2)
            X = int(PuntoC[0])
            Y = int(PuntoC[1])
            pygame.draw.circle(pantalla, AZUL, cart(CENTRO, [X, Y]), 0)
            pygame.display.flip()
            ang2 = ang2 + 1
        pygame.display.flip()
