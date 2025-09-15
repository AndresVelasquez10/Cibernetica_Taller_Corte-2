import pygame
import numpy as np
import time 

pygame.init()
#Escogemos el tamaño de la pantalla
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
bg = 25, 25, 25
#Color de fondo
screen.fill(bg)




nxC, nyC = 25, 25

#Dimensiones de las celdas
dimCW = width / nxC
dimCH = height / nyC

#celdas vivas = 1, muertas = 0  
gameState = np.zeros((nxC, nyC ))


#Automáticamente creamos algunas células vivas
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1
gameState[4, 5] = 1
gameState[3, 4] = 1
gameState[21, 21] = 1

gameState[21, 21] = 1  
gameState[22, 22] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1
gameState[20, 23] = 1

#Bucle para ejecutar el juego
running = True
paused = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    if not paused:
        newGameState = np.copy(gameState)
        screen.fill(bg)
        time.sleep(0.1)

        for y in range(0, nyC):
            for x in range(0, nxC):
                #Calculamos el número de vecinos
                n_neigh = gameState[(x-1)% nxC, (y-1) % nyC] + \
                          gameState[(x) % nxC, (y-1) % nyC] + \
                          gameState[(x+1) % nxC, (y-1) % nyC] + \
                          gameState[(x-1) % nxC, y % nyC] + \
                          gameState[(x+1) % nxC, y % nyC] + \
                          gameState[(x-1) % nxC, (y+1) % nyC] + \
                          gameState[(x) % nxC, (y+1) % nyC] + \
                          gameState[(x+1) % nxC, (y+1) % nyC]
                #Reglas del juego 
                #(Una muerta revive al tener 3 vivas junto a ella)
                if gameState[x, y] == 0 and n_neigh == 3:
                    newGameState[x, y] = 1
                #(Una viva muere si tiene menos de 2 o más de 3 vivas junto a ella)
                elif gameState[x,y] == 1 and (n_neigh < 2 or n_neigh > 3):
                    newGameState[x, y] = 0
                #Poligono de cada celda
                poly = [((x) * dimCW,  y *  dimCH),
                        ((x+1) * dimCW, y *  dimCH),
                        ((x+1) * dimCW, (y+1) *  dimCH),
                        ((x) *   dimCW,  (y+1) *  dimCH)]
                #Celda muerta: gris, celda viva: verde
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
                else: 
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
        gameState = np.copy(newGameState)

    pygame.display.flip()





