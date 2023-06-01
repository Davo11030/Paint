from line import linea
from figuras import *

def cache(cache_line, cache_rect, cache_circle, cache_cuadrado, cache_tri_eq, cache_tri_es, cache_tri_is, background_color, screen):  
    screen.fill(background_color)
    pygame.display.flip()
    for dato in cache_line:
        linea(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
    for dato in cache_circle:
        circle(dato[0], dato[1], dato[2], dato[3], dato[4])
    for dato in cache_tri_es:
        tria_es(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
    for dato in cache_tri_is:
        tria_is(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])
    for dato in cache_tri_eq:
        tria_eq(dato[0], dato[1], dato[2], dato[3], dato[4])
    for dato in cache_cuadrado:
        cuadrado(dato[0], dato[1], dato[2], dato[3], dato[4])
    for dato in cache_rect:
        rectangulo(dato[0], dato[1], dato[2], dato[3], dato[4], dato[5])

def undo(select, cache_line, cache_rect, cache_circle, cache_cuadrado, cache_tri_eq, cache_tri_es, cache_tri_is, background_color, screen):
    if select==0:
        print("Usted no a realizado ningun dibujo")
    elif select==1:
        cache_line.pop()
    elif select==2:
        cache_circle.pop()
    elif select==3:
        cache_tri_es.pop()
    elif select==4:
        cache_tri_is.pop()
    elif select==5:
        cache_tri_eq.pop()
    elif select==6:
        cache_cuadrado.pop()
    elif select==7:
        cache_rect.pop()
    cache(cache_line, cache_rect, cache_circle, cache_cuadrado, cache_tri_eq, cache_tri_es, cache_tri_is, background_color, screen)
    select=0
    return select