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

# Recibe el punto y lo devuelve trasladado con respecto al punto de origen
def Cart(p):
    '''
    p[x,y]: p[0] = x , p[1] = y
    '''
    xp = CENTRO[0] + p[0]
    yp = CENTRO[1] - p[1]
    return [xp, yp]

def Scal(p):
    '''
    p[x,y]: p[0] = x , p[1] = y
    '''
    xp = ESCALAR*(CENTRO[0] + p[0])
    yp = ESCALAR*(CENTRO[1] - p[1])
    return [xp, yp]


# Main
if __name__ == '__main__':
    pygame.init()
    pantalla = pygame.display.set_mode([ANCHO,ALTO])

    # Poligono, Puntos Cartesianos
    PuntoX = Cart([0,0])
    PuntoX1 = Cart([0,-30])
    PuntoX2 = Cart([20,-30])
    PuntoX3= Scal([0,0])
    PuntoX4 = Scal([0,-30])
    PuntoX5 = Scal([20,-30])

    # SetPuntos contiene todos los puntos del poligono
    SetPuntos = [PuntoX, PuntoX1, PuntoX2] # Se concateno las listas
    SetPuntosSc = [PuntoX3,PuntoX4,PuntoX5]
    # Dibuja el poligono
    triangulo(SetPuntos)
    pygame.display.flip()
    trianguloSc(SetPuntosSc)
    pygame.display.flip()

    fin = False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin = True
