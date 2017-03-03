import pygame
from lib import *
#suma de dos vectores y dibujarlos y producto por escalar.
#creando libreria, la libreria se importa asi:from lib import*, el la libreria no puede haber nada con main(), se pueden tener varias librerias


if __name__ == '__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)

    plano=Cartesiano(pantalla,[50,50])
    print plano.c
    #plano.Ejes(pantalla)
    plano.Ejes()
    #plano.Punto(pantalla,[10,40]) se usa cuando no esta definido en el cnstructor de la libreria lib
    plano.Punto([10,40])
    plano.Linea([5,5],[2,2])


    l=[[20,-10],[40,-10],[40,50]]
    plano.Poli(l)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                fin=True
__________________________________________
#Apartir de aqui esta la libreria creada en clase.
import pygame

ANCHO=500
ALTO=400
BLANCO=(255,255,255)
ROJO=(255,0,0)
VERDE=(0,255,0)
AZUL=(0,0,255)
#Como paltalla se usa mucho , lo definimos en el constructor.
class Cartesiano():

    def __init__(self,pantalla,centro):
        #self.c=[100,100] vesrion antes de definir en el constructor
        self.c=centro
        self.pan=pantalla
    def Ejes(self):
        pygame.draw.line(self.pan,ROJO,[self.c[0],0],[self.c[0],ALTO],1)
        pygame.draw.line(self.pan,ROJO,[0,self.c[1]],[ANCHO,self.c[1]],1)
    def Punto(self,p):
        #transformacion
        #px=self.c[0]+p[0]
        #py=self.c[1]-p[1] se usa cuando no esta metodo Tras
        #pygame.draw.circle(self.pan,ROJO,[px,py],2)
        pygame.draw.circle(self.pan,ROJO,self.Tras(p),2)
    def Tras(self,p):
        px=self.c[0]+p[0]
        py=self.c[1]-p[1]
        return [px,py]
    def Linea(self,p,q):
        pygame.draw.line(self.pan,ROJO,self.Tras(p),self.Tras(q),1)
    def Poli(self,l):
        lc=[]
        for elemento in l:
            p=self.Tras(elemento)
            lc.append(p)
        pygame.draw.polygon(self.pan,AZUL,lc,1)
    def SumaVectore(self,):
        a=[1,2,3]
        b=[1,2,3]
        nuevalista=[]
 
        for i in range(len(a)):
	           nuevalista.append(a[i]+b[i]) 
               print nuevalista
