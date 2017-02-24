import pygame

ANCHO = 400
ALTO = 200
CENTRO = (50,50)
ROJO = [255, 0, 0]
AZUL = [034, 113, 179]
LILA = [108, 070, 117]
ESCALAR=(2)


def triangulo(p):
    pygame.draw.polygon(pantalla, LILA, p)
def trianguloSc(p):
    pygame.draw.polygon(pantalla, AZUL, p)

# Main
if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    pygame.display.flip()


    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
            if event.type == pygame.KEYDOWN:
                if event.key==pygame
