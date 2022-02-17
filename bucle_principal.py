import pygame as pg
import random 
import time

pg.init()

pantalla = pg.display.set_mode((600,800))



game_over = False

x = 300
y= 400

def muevex(num):
    if num == 600:
        while num != 0:
            num -= 1
            return num
def muevexpositivo(num):
    if num == 0:
        while num != 600:
            num += 1
            return num

while not game_over:
    eventos = pg.event.get()

    for evento in eventos:
        if evento.type == pg.QUIT:
            game_over = True
    

    
    if x != 600:
        x+=1
   
    

   

    
    



    pantalla.fill((255,0,0))
    

    bola= pg.draw.circle(pantalla, (255, 255, 0), (x,y), 10)


    
    pg.display.flip()

pg.quit()







