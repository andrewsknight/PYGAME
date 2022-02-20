from curses import BUTTON1_RELEASED
import pygame as pg
import random 
import time
pg.init()

class Bola:
    def __init__(self, x, y, padre,  color = (255, 255, 255), radio = 10, vx = 1, vy = 1 ):
        self.x = x
        self.y = y
        self.color = color
        self.radio = radio
        self.vx = vx
        self.vy = vy
        self.padre = padre


    def mover(self):
        self.x += self.vx 
        self.y += self.vy

        if self.x <= self.radio or self.x >= self.padre.get_width() - self.radio:
            self.vx *= -1

        #if self.radio >= self.x >= limDer - self.radio:

        if self.y <= self.radio or self.y >= self.padre.get_height() - self.radio:
            self.vy *= -1

    def dibujar(self,):
        pg.draw.circle(self.padre, self.color, (self.x, self.y), self.radio,)

class Game:
    def __init__(self, ancho=600, alto=800):
        self.pantalla = pg.display.set_mode((ancho, alto))
        
        self.bolas = []
        for i in range(1,15):
            
            colorAleatorio = []
            for colorAl in range(0, 3):
                colorAle = random.randint(1, 255)
                colorAleatorio.append(colorAle)


            radio = random.randint(1,60)
            self.bolaNueva = Bola(random.randint(1+radio, 600-radio),random.randint(1+radio, 800-radio),self.pantalla,(colorAleatorio), radio, random.randint(-2,2), random.randint(-2,2))
            self.bolas.append(self.bolaNueva)
            
        
        

      
        

    def bucle_ppal(self):
        game_over = False

        while not game_over:

            eventos = pg.event.get()
            for evento in eventos:
                if evento.type == pg.QUIT:
                    game_over = True

         
            self.pantalla.fill((255, 0, 0))    
           
            for self.bol in self.bolas:
                self.bol.mover()
                self.bol.dibujar()
           
            
            pg.display.flip()

    
if __name__ == '__main__':
    pg.init()

    game = Game()
    game.bucle_ppal()

    pg.quit()
    