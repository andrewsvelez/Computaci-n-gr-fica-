import pygame
ANCHO=400
ALTO=200
C=(100,100)
AZUL=[0,0,255]


def Circle1(p=[50,50],r=5):
    #p=[50,50]
    pygame.draw.circle(pantalla,AZUL,p,r)

def Triangulo():
    pygame.draw.polygon(pantalla,AZUL,[[20,10],[10,30],[30,40]],3)

def Plano():
    pygame.draw.line(pantalla,[255,0,0],[0,C[1]],[ANCHO,C[1]])
    pygame.draw.line(pantalla,[255,0,0],[C[1],0],[C[0],ALTO])
def escalamiento():
    '''
    xp=xSx
    yp=ySy
    '''



if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    Plano()
    #Circle1()
    Triangulo()
    pygame.display.flip()

    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fin=True
