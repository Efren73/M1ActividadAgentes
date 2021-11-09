#Código para el problema de la aspiradora de MxN celdas
#Alumno: Efren Aldana
#Fecha de creación: 08/11/21

import random
import time

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
for i in range (filas):
  habitaciones.append([0]*columnas)
  visitadas.append([0]*columnas)

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
posx = 0
posy = 0

#Mientras el porcentaje sea mayor que 0 o el tiempo sea menor que el indicado, se seguirá ejecutando el programa
while(porcentaje > 0 and tiempo <= tmax):
    inicio = time.time()
    
    for i in range (cant_agentes):
        if(habitaciones[agentes[i].x][agentes[i].y] == 1):
            print("Agente "+str(i)+" limpiando la celda ("+str(agentes[i].x)+ ", " +str(agentes[i].y)+")")
            habitaciones[agentes[i].x][agentes[i].y] = 0
            visitadas[agentes[i].x][agentes[i].y] = 1
            porcentaje -= 1
            rand_val_1 = random.randrange(-1, 2, 2)
            rand_val_2 = random.randrange(-1, 2, 2)
            if((agentes[i].x+rand_val_1) < 0 or
               (agentes[i].x+rand_val_1) > (filas-1) or
               (agentes[i].y+rand_val_2) < 0 or
               (agentes[i].y+rand_val_2) > (columnas-1) or
               (visitadas[agentes[i].x + rand_val_1][agentes[i].y+rand_val_2] == 1)):
              continue
            else: 
              agentes[i].x += rand_val_1
              agentes[i].y += rand_val_2
              print("Moviendo agente " +str(i)+ " a la casilla ("+str([agentes[i].x])+", "+str([agentes[i].y])+")")
              movimientos += 1
              
        elif(habitaciones[agentes[i].x][agentes[i].y] == 0 and visitadas[agentes[i].x][agentes[i].y] == 0):
            
            visitadas[agentes[i].x][agentes[i].y] = 1
            rand_val_1 = random.randrange(-1, 2, 2)
            rand_val_2 = random.randrange(-1, 2, 2)
            if((agentes[i].x+rand_val_1) < 0 or
               (agentes[i].x+rand_val_1) > (filas-1) or
               (agentes[i].y+rand_val_2) < 0 or
               (agentes[i].y+rand_val_2) > (columnas-1) or
               (visitadas[agentes[i].x + rand_val_1][agentes[i].y+rand_val_2] == 1)):
                print("Si llego aqui", i)
                continue
            else:
              print("Aqui igual llego")
              agentes[i].x += rand_val_1
              agentes[i].y += rand_val_2
              print("Moviendo agente " +str(i)+ " a la casilla ("+str([agentes[i].x])+", "+str([agentes[i].y])+")")
              movimientos += 1
        
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
print("Movimientos realizados por el agente: ", movimientos)
