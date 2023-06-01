import pygame
import sys
import math
from line import linea
from figuras import *#circle, tria_es, tria_eq, tria_is, cuadrado, rectangulo
from caches import cache, undo
# Inicializar Pygame
pygame.init()
# Crear una superficie de 800x600 píxeles, no debe cambiar esta superficie
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
background_color = (0,0,0)
screen.fill(background_color)
# Color del pixel
color = (255,0,0)
#Variables del cache
cache_line = []
cache_rect = []
cache_circle = []
cache_cuadrado = []
cache_tri_eq = []
cache_tri_es = []
cache_tri_is = []
SELECT=0
print("\n No sabes que hacer? ingresa el comando help\n")
while True:
    cmd = input("cmd> ")
    if cmd == "exit":
        #cierra el programa
        pygame.quit()
        sys.exit()
    elif "color" in cmd:
        cmd = cmd.split(" ")
        if len(cmd) == 2:
            if "-ls" in cmd:
                #Como cambiar el color del pixel
                print("Para cambiar el color del pixel ingresa 'color set # # #' (Codigo RGB)")
        elif len(cmd) == 5:
            if "set" in cmd:
                #cambia el color del pixel
                r = int(cmd[2])
                g = int(cmd[3])
                b = int(cmd[4])
                color = (r, g, b)
                print("Cambio el color")
    elif "background" in cmd:
        cmd = cmd.split(" ")
        if len(cmd) == 4:
            #Cambia el color del fondo
            r = int(cmd[1])
            g = int(cmd[2])
            b = int(cmd[3])
            background_color = (r, g ,b)
            cache(cache_line, cache_rect, cache_circle, cache_cuadrado, cache_tri_eq, cache_tri_es, cache_tri_is, background_color, screen)
            print("Cambio el background")
    elif "linea" in cmd:
        cmd=cmd.split(" ")
        if len(cmd)==5:
            #Dibuja una linea
            x1=int(cmd[1])
            y1=int(cmd[2])
            x2=int(cmd[3])
            y2=int(cmd[4])
            linea(x1, y1, x2, y2, color, screen)
            cache_line.append((x1, y1, x2, y2, color, screen))
            print("Hizo una linea")
            SELECT=1
    elif "draw circle" in cmd:
        cmd=cmd.split(" ")
        if len(cmd)==5:
            #Dibuja un circulo
            x=int(cmd[2])
            y=int(cmd[3])
            radio=int(cmd[4])
            circle(x, y, radio, color, screen)
            cache_circle.append((x, y, radio, color, screen))
            print("Hizo un circulo")
            SELECT=2
    elif "draw triangulo" in cmd:
        #Dibuja triangulos
        cmd=cmd.split(" ")
        if len(cmd)==7:
            x=int(cmd[3])
            y=int(cmd[4])
            base=int(cmd[5])
            altura=int(cmd[6])
            if "-es" in cmd:
                escaleno.perimetro(x, y, base, altura, color, screen)
                cache_tri_es.append((x, y, base, altura, color, screen))
                print("Hizo un triangulo escaleno")
                SELECT=3
            elif "-is" in cmd:
                tria_is(x, y, base, altura, color, screen)
                cache_tri_is.append((x, y, base, altura, color, screen))
                print("Hizo un triangulo isoceles")
                SELECT=4
        elif len(cmd)==6:
            if "-eq" in cmd:
                x=int(cmd[3])
                y=int(cmd[4])
                base=int(cmd[5])
                tria_eq(x, y, base, color, screen)
                cache_tri_eq.append((x, y, base, color, screen))
                print("Hizo un triangulo equilatero")
                SELECT=5
    elif "draw cuadrado" in cmd:
        #Dibuja un cuadrado
        cmd=cmd.split(" ")
        if len(cmd)==5:
            x=int(cmd[2])
            y=int(cmd[3])
            lado=int(cmd[4])
            cuadrado(x, y, lado, color, screen)
            cache_cuadrado.append((x, y, lado, color, screen))
            print("Hizo un cuadrado")
            SELECT=6
    elif "draw rectangulo" in cmd:
        #Dibuja un rectangulo
        cmd=cmd.split(" ")
        if len(cmd)==6:
            x=int(cmd[2])
            y=int(cmd[3])
            base=int(cmd[4])
            altura=int(cmd[5])
            rectangulo(x, y, base, altura, color, screen)
            cache_rect.append((x, y, base, altura, color, screen))
            print("Hizo un rectangulo")
            SELECT=7
    elif "undo" in cmd:
        undo(SELECT, cache_line, cache_rect, cache_circle, cache_cuadrado, cache_tri_eq, cache_tri_es, cache_tri_is, background_color, screen)
        SELECT= 0
    elif "help" in cmd:
        print("Hola este programa fue desarrollado por David Flores y es un paint por comandos")
        print("Hasta el momento tiene 12 comandos funcionales \n")
        print("1.- exit: Da fin al programa \n\n2.- color -ls: Muestra como cambiar el color del pixel \n")
        print("3.- background # # #: Cambia el color del fondo ingresando un codigo RGB \n\n4.- linea x1 y1 x2 y2: Ingresa 2 coordenas para trazar una linea de un punto A  a un punto B\n")
        print("5.- draw circle x y radio: Dibuja un circulo ingresando la coordenada del centro y el radio\n")
        print("6.- draw triangulo -es x y base altura: Dibuja un triangulo escaleno ingresando la coordenada donde estara junto con su base y altura\n")
        print("7.- draw triangulo -is x y base altura: Dibuja un triangulo isoceles ingresando la coordenada donde estara junto con su base y altura\n")
        print("8.- draw triangulo -eq x y base: Dibuja un triangulo equilater ingresando la coordenada donde estara junto con su base\n")
        print("9.- draw cuadrado x y lado: Dibuja un cuadrado ingresando la coordenada conde estara junto con la longitud de sus lados\n")
        print("10.- draw rectangulo x y base altura: Dibuja un rectangulo ingresando la coordenada donde estara junto con la base y altura\n")
        print("11.- undo: Borra el ultimo dibujo")
        print("12.- help: Explicacion breve")
        print("Para ingresar cualquier dato solo se ingresa el nombre del comando y por espacios los datos (coordenadas, valores, etc)")