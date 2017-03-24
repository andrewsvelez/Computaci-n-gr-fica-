import pygame
import random

ANCHO=640
ALTO=480
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
NEGRO=(0,0,0)

class Bloque(pygame.sprite.Sprite):
    def __init__(self,color,alto,ancho):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([alto,ancho])
        self.image.fill(color)
        self.rect = self.image.get_rect()

if __name__ == '__main__':
    pygame.init()

    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    #cargar imagenes
    jugador=pygame.image.load('jugador.jpg')
    bloques=pygame.image.load('Skeleton.png')

    bloques=pygame.sprite.Group()
    #jugador=Bloque(ROJO,30,30)
    todos=pygame.sprite.Group()
    todos.add(jugador)

    bloques=pygame.sprite.Group()

    for i in range(10):
        #b=Bloque(AZUL,30,30)
        b=bloques
        b.rect.x=random.randint(10,(ANCHO-30))
        b.rect.y=random.randint(10,(ALTO-30))
        bloques.add(b)
        todos.add(b)



    fin=False
    reloj=pygame.time.Clock()
    puntos=0
    while not fin:
        pos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
        #jugador.rect=pos
        jugador.rect.x=pos[0]
        jugador.rect.y=pos[1]
        #lista de golpeados
        #lg=pygame.sprite.spritecollide(jugador,bloques,True)
        lg=pygame.sprite.spritecollide(jugador,bloques,False)
        for b in lg:
            puntos+=1
            print puntos
            #print 'Golpe'
        pantalla.fill(BLANCO)
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
