import pygame

ancho_ventana = 400
altura_ventana = 400

window = pygame.display.set_mode((ancho_ventana, altura_ventana))
pygame.display.set_caption("Dijkstra 21310430")

columnas = 20
filas = 20

ancho_caja = ancho_ventana // columnas
altura_caja = altura_ventana // filas

cuadricula = [] #Este arreglo almacena todas las cajas de nuestra ventana
cola = []  #Almacena nuestra elementos en cola 
camino = [] # 


class Nodo:
    def __init__(self, i, j):
        self.x = i
        self.y = j
        self.inicio = False
        self.barrera = False
        self.final = False
        self.en_cola = False
        self.visitado = False
        self.vecinos = []
        self.predecesor = None




    def dibujar(self, win, color):
        pygame.draw.rect(win, color, (self.x * ancho_caja, self.y * altura_caja, ancho_caja-2, altura_caja-2))



    def colocar_vecinos(self):  #Esta funcion nos ayuda a poder seleccionar los vecinos de cada casilla
        if self.x > 0:
            self.vecinos.append(cuadricula[self.x - 1][self.y]) 
        if self.x < columnas - 1:
            self.vecinos.append(cuadricula[self.x + 1][self.y])
        if self.y > 0:
            self.vecinos.append(cuadricula[self.x][self.y - 1])
        if self.y < filas - 1:
            self.vecinos.append(cuadricula[self.x][self.y + 1])


# Creacion de cuadricula
for i in range(columnas):
    arr = []
    for j in range(filas):
        arr.append(Nodo(i, j))
    cuadricula.append(arr)



# Agregar vecinos
for i in range(columnas): # Aqui lo que hago es darle a cada una de las casilllas sus respectivos vecinos con la funcion colocar_vecinos
    for j in range(filas):
        cuadricula[i][j].colocar_vecinos()




def main():
    iniciar_busqueda = False
    colocar_nodo_final = False
    colocar_nodo_inicio = False
    buscando = True
    nodo_final = None
    nodo_inicio = None
    

    while True:
        for event in pygame.event.get():
            # Evento para cerrar la ventana
            if event.type == pygame.QUIT:
                pygame.quit()
            # Controles de mouse
            if event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                # Indicar barrera
                if event.buttons[0]:              
                    i = x // ancho_caja
                    j = y // altura_caja
                    cuadricula[i][j].barrera = True
                # Indicar inicio
                if event.buttons[2] and not colocar_nodo_inicio and not  colocar_nodo_final:
                    i = x // ancho_caja
                    j = y // altura_caja
                    nodo_inicio = cuadricula[i][j]
                    nodo_inicio.inicio = True
                    colocar_nodo_inicio = True
                    nodo_inicio.visitado = True
                    cola.append(nodo_inicio)
                #  Indicar final
                elif event.buttons[2] and not colocar_nodo_final and colocar_nodo_inicio:
                    i = x // ancho_caja
                    j = y // altura_caja
                    nodo_final = cuadricula[i][j]
                    nodo_final.final = True
                    colocar_nodo_final = True


            # inicio Algoritmo
            if event.type == pygame.KEYDOWN and colocar_nodo_inicio and colocar_nodo_final:
                iniciar_busqueda = True

        if iniciar_busqueda:
            if len(cola) > 0 and buscando:
                nodo_actual = cola.pop(0)
                nodo_actual.visitado =True 
                if nodo_actual == nodo_final:
                    buscando = False
                    while nodo_actual.predecesor != nodo_inicio:
                        camino.append(nodo_actual.predecesor)
                        nodo_actual = nodo_actual.predecesor
                else:
                    for vecino in nodo_actual.vecinos:
                        if not vecino.en_cola and not vecino.barrera:
                            vecino.en_cola = True
                            vecino.predecesor = nodo_actual
                            cola.append(vecino)


        window.fill((0, 0, 0))

        for i in range(columnas):
            for j in range(filas):
                nodo = cuadricula[i][j]
                nodo.dibujar(window, (255, 255, 255))

                if nodo.en_cola:
                    nodo.dibujar(window, (200, 0, 0))
                if nodo.visitado:
                    nodo.dibujar(window, (0, 200, 0))
                if nodo in camino:
                    nodo.dibujar(window, (0, 0, 200))

                if nodo.inicio:
                    nodo.dibujar(window, (0, 200, 200))
                if nodo.barrera:
                    nodo.dibujar(window, (10, 10, 10))
                if nodo.final:
                    nodo.dibujar(window, (200, 200, 0))

        pygame.display.flip()


main()
         

