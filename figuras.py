import pygame
import math
from line import linea

def circle(center_x, center_y, radius, color, screen):
    # Calcular los puntos de la circunferencia
    num_points = 1000
    angle_step = 2 * math.pi / num_points
    # Dibujar la circunferencia
    for i in range(num_points):
        angle = i * angle_step
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        screen.set_at((x, y), color)
        pygame.display.flip()

def lineas_tria(x1, x2, x3, y1, y2, y3, color, screen):
    linea(x1, y1, x2, y2, color, screen)
    linea(x2, y2, x3, y3, color, screen)
    linea(x3, y3, x1, y1, color, screen)

def tria_es(x1, y1, base, altura, color, screen):
    x2 = x1 + base
    y2 = y1
    x3 = x1
    y3 = y1 - altura
    lineas_tria(x1, x2, x3, y1, y2, y3, color, screen)

def tria_is(x1, y1, base, altura, color, screen):
    x2 = x1 + base
    y2 = y1
    x3 = x1 + base // 2
    y3 = y1 - altura
    lineas_tria(x1, x2, x3, y1, y2, y3, color, screen)

def tria_eq(x1, y1, base, color, screen):
    angulo = math.radians(60)
    x2 = x1 + base
    y2 = y1
    x3 = x1 + base // 2
    y3 = y1 - int(math.sin(angulo)*base)
    lineas_tria(x1, x2, x3, y1, y2, y3, color, screen)

def lineas_cuadro(x1, x2, y1, y2, color, screen):
    linea(x1, y1, x2, y1, color, screen)
    linea(x2, y1, x2, y2, color, screen)
    linea(x2, y2, x1, y2, color, screen)
    linea(x1, y2, x1, y1, color, screen)

def cuadrado(x1, y1, lado, color, screen):
    x2 = x1 + lado
    y2 = y1 + lado
    lineas_cuadro(x1, x2, y1, y2, color, screen)
    
def rectangulo(x1, y1, base, altura, color, screen):
    x2 = x1 + base
    y2 = y1 - altura
    lineas_cuadro(x1, x2, y1, y2, color, screen)