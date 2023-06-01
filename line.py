import pygame

def linea(x1, y1, x2, y2, color, screen):

    # Calcular la distancia en píxeles entre los puntos
    dx = x2 - x1
    dy = y2 - y1
    # Calcular el número de píxeles que se deben mover en cada eje
    main_steps = max(abs(dx), abs(dy))
    # Calcular el incremento en cada eje por paso
    x_increment = dx / main_steps
    y_increment = dy / main_steps
    # Bucle principal
    while True:
        # Comprobar si se ha llegado al punto final
        if round(x1, 3) == x2 and round(y1, 3) == y2:
            break
        # Dibujar un píxel en la posición actual
        screen.set_at((int(x1), int(y1)), color)
        # Actualizar la posición en cada eje
        x1 += x_increment 
        y1 += y_increment 
        # Actualizar la pantalla
        pygame.display.flip()
        