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
    def __init__(self,archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()

class Enemigo(pygame.sprite.Sprite):
    def __init__(self,archivo_img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(archivo_img).convert_alpha()
        self.rect = self.image.get_rect()
        self.der=0
        self.vel=2

    def update(self):
        if self.rect.x>(ANCHO-self.rect.width):
            self.der=1
            self.vel+=1
        if self.rect.x<2:
           self.der=0
        if self.der==0:
           self.rect.x+=self.vel
        else:
            self.rect.x-=self.vel


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    #cargar imagenes
    jugador=Bloque('jugador.jpg')
    bloques=pygame.sprite.Group()
    #jugador=Bloque(ROJO,30,30)
    todos=pygame.sprite.Group()
    todos.add(jugador)

    bloques=pygame.sprite.Group()

    for i in range(2):
        #b=Bloque(AZUL,30,30)
        b=Enemigo('Skeleton.png')
        b.rect.x=random.randint(10,(ANCHO-b.rect.width))
        b.rect.y=random.randint(10,(ALTO-b.rect.height))
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
        todos.update()
        todos.draw(pantalla)
        pygame.display.flip()
        reloj.tick(50)
