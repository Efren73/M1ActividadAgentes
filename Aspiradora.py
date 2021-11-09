#Código para el problema de la aspiradora de MxN celdas
#Alumno: Efren Aldana
#Fecha de creación: 08/11/21

import random
import time

#Clase para identificar las coordenadas x y y
class Punto:
    def __init__(self, x, y): 
        self.x = 0 
        self.y = 0

filas = int(input("Introduce la cantidad de filas: "))
columnas = int(input("Introduce la cantidad de columnas: "))
cant_agentes = int(input("Introduce la cantidad de agentes: "))
porcentaje = int(input("Introduce el porcentaje de celdas sucias: "))
tmax = int(input("Introduce el tiempo máximo de ejecución (en segundos): "))

agentes = []

for i in range (cant_agentes):
    agentes.append(Punto(0, 0))

#El porcentaje se convierte en la cantidad de habitaciones sucias
#Ejemplo: Si son 12 celdas y el porcentaje es 50, porcentaje será 6 
porcentaje = int(porcentaje/100 * (filas * columnas))

#En caso de que el porcentaje sea 0, se convertirá en uno para que al menos exista una habitación sucia
if(porcentaje == 0):
  porcentaje = 1
  
#Se define la matriz de las habitaciones
habitaciones = []
visitadas = []
ocupadas = []
for i in range (filas):
  habitaciones.append([0]*columnas)
  visitadas.append([0]*columnas)
  ocupadas.append([0]*columnas)
  
ocupadas[0][0] = 1

contador_sucias = 0 
#Asignando las habitaciones sucias con la funcón random
#Para habitaciones limpias es 0 y para las sucias es 1
for i in range (filas):
  for j in range (columnas):
    if(contador_sucias == porcentaje):
      habitaciones[i][j] = 0
      continue 
    else:
      habitaciones[i][j] = random.randint(0, 1)
      if(habitaciones[i][j] == 1):
        contador_sucias += 1
        
#En caso de que las habitaciones sucias sean menores que el porcentaje, se ejecuta lo siguiente
if(porcentaje>contador_sucias):
  for i in range (filas):
    for j in range (columnas):
      if(porcentaje == contador_sucias):
        continue
      else:
          if(habitaciones[i][j] == 0):
            habitaciones[i][j] = 1 
            contador_sucias += 1


tiempo = 0
movimientos = 0
#Mientras el porcentaje sea mayor que 0 o el tiempo sea menor que el indicado, se seguirá ejecutando el programa
while(porcentaje > 0 and tiempo <= tmax):
    inicio = time.time()
    #Ciclo for para tomar en cuenta todos los agentes que existen
    for i in range (cant_agentes):
        #Entra al ciclo si la habitación está sucia
        if(habitaciones[agentes[i].x][agentes[i].y] == 1):
            print("Agente "+str(i+1)+" limpiando la celda ("+str(agentes[i].x + 1)+ ", " +str(agentes[i].y + 1)+")")
            habitaciones[agentes[i].x][agentes[i].y] = 0
            #Se reduce el porcentaje porque ya falta una habitación menos por limpiar
            porcentaje -= 1
            #Se registra la habitación como visitada
            visitadas[agentes[i].x][agentes[i].y] = 1
            ciclo = True
            posx = -1
            posy = -1
            count = 1
            #Ciclo en donde se decide a donde se va a mover el agente
            while(ciclo == True):
                if((agentes[i].x+posx) >= 0 and
                   (agentes[i].x+posx) <= (filas-1) and
                   (agentes[i].y+posy) >= 0 and
                   (agentes[i].y+posy) <= (columnas-1) and
                   visitadas[agentes[i].x + posx][agentes[i].y + posy] == 0 and count<=9):
                    #Si se encontró una posx y posy que no está ocupada se mueve al sigueinte
                    if(ocupadas[agentes[i].x+posx][agentes[i].y + posy] == 0):
                        ocupadas[agentes[i].x][agentes[i].y] = 0
                        agentes[i].x += posx
                        agentes[i].y += posy
                        print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                        #Se cuenta el movimiento del agente
                        movimientos += 1
                        ocupadas[agentes[i].x][agentes[i].y] = 1
                        ciclo = False
                #Si ya se visitaron las 8 posiciones posibles y todas ya se visitaron, se escoge una al azar
                elif(count > 9):
                    rand_val_1 = random.randint(-1, 1)
                    rand_val_2 = random.randint(-1, 1)
                    if((agentes[i].x+rand_val_1) < 0 or
                       (agentes[i].x+rand_val_1) > (filas-1) or
                       (agentes[i].y+rand_val_2) < 0 or
                       (agentes[i].y+rand_val_2) > (columnas-1) or
                       (rand_val_1 == 0 and rand_val_2 == 0)):
                        ciclo = False
                    else:
                        if(ocupadas[agentes[i].x+rand_val_1][agentes[i].y + rand_val_2] == 0):
                            ocupadas[agentes[i].x][agentes[i].y] = 0
                            agentes[i].x += rand_val_1
                            agentes[i].y += rand_val_2
                            ocupadas[agentes[i].x][agentes[i].y] = 1
                            print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                            movimientos += 1
                            ciclo = False
                        else:
                            ciclo = False

                #Contador para saber si se aumenta la posición en x o en y para saber todas las casillas de al rededor posibles
                if(count%3 == 0):
                    posy= -1
                    posx += 1
                else:
                    posy += 1
                if(ciclo == True):
                    count += 1                        
              
        elif(habitaciones[agentes[i].x][agentes[i].y] == 0):
            #Se registra la habitación como visitada
            visitadas[agentes[i].x][agentes[i].y] = 1
            ciclo = True
            posx = -1
            posy = -1
            count = 1
            #Ciclo en donde se decide a donde se va a mover el agente
            while(ciclo == True):
                if((agentes[i].x+posx) >= 0 and
                   (agentes[i].x+posx) <= (filas-1) and
                   (agentes[i].y+posy) >= 0 and
                   (agentes[i].y+posy) <= (columnas-1) and
                   visitadas[agentes[i].x + posx][agentes[i].y + posy] == 0 and count<=9):
                    #Si se encontró una posx y posy que no está ocupada se mueve al sigueinte
                    if(ocupadas[agentes[i].x+posx][agentes[i].y + posy] == 0):
                        ocupadas[agentes[i].x][agentes[i].y] = 0
                        agentes[i].x += posx
                        agentes[i].y += posy
                        print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                        #Se cuenta el movimiento del agente
                        movimientos += 1
                        ocupadas[agentes[i].x][agentes[i].y] = 1
                        ciclo = False
                #Si ya se visitaron las 8 posiciones posibles y todas ya se visitaron, se escoge una al azar
                elif(count > 9):
                    rand_val_1 = random.randint(-1, 1)
                    rand_val_2 = random.randint(-1, 1)
                    if((agentes[i].x+rand_val_1) < 0 or
                       (agentes[i].x+rand_val_1) > (filas-1) or
                       (agentes[i].y+rand_val_2) < 0 or
                       (agentes[i].y+rand_val_2) > (columnas-1) or
                       (rand_val_1 == 0 and rand_val_2 == 0)):
                        ciclo = False
                    else:
                        if(ocupadas[agentes[i].x+rand_val_1][agentes[i].y + rand_val_2] == 0):
                            ocupadas[agentes[i].x][agentes[i].y] = 0
                            agentes[i].x += rand_val_1
                            agentes[i].y += rand_val_2
                            ocupadas[agentes[i].x][agentes[i].y] = 1
                            print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                            movimientos += 1
                            ciclo = False
                        else:
                            ciclo = False
                #Contador para saber si se aumenta la posición en x o en y para saber todas las casillas de al rededor posibles
                if(count%3 == 0):
                    posy= -1
                    posx += 1
                else:
                    posy += 1
                if(ciclo == True):
                    count += 1
                    
    fin = time.time()
    tiempo += (fin-inicio)


#Ciclo para contar la cantidad de habitaciones limpias
limpias = 0
for i in range (filas):
  for j in range (columnas):
    if(habitaciones[i][j] == 0):
      limpias += 1

#Se obtiene el porcentaje de habitaciones limpias
porcentaje_final = 0.0
porcentaje_final = float((limpias / (filas*columnas))*100)

print("Tiempo que se registro en la limpieza de las habitaciones: ", tiempo)
print("El porcentaje de habitaciones limpias es de: ", porcentaje_final)
print("Movimientos realizados por los agentes: ", movimientos)
