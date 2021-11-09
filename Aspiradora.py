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
#Mientras el porcentaje sea mayor que 0 o el tiempo sea menor que el indicado, se seguirá ejecutando el programa
while(porcentaje > 0 and tiempo <= tmax):
    inicio = time.time()
    for i in range (cant_agentes):
        if(habitaciones[agentes[i].x][agentes[i].y] == 1):
            print("Agente "+str(i+1)+" limpiando la celda ("+str(agentes[i].x + 1)+ ", " +str(agentes[i].y + 1)+")")
            habitaciones[agentes[i].x][agentes[i].y] = 0
            porcentaje -= 1
            visitadas[agentes[i].x][agentes[i].y] = 1
            ciclo = True
            posx = -1
            posy = -1
            count = 1
            while(ciclo == True):
                
                if((agentes[i].x+posx) >= 0 and
                   (agentes[i].x+posx) <= (filas-1) and
                   (agentes[i].y+posy) >= 0 and
                   (agentes[i].y+posy) <= (columnas-1) and
                   visitadas[agentes[i].x + posx][agentes[i].y + posy] == 0 and count<=9):
                    cont_temporal = 0
                    for j in range (cant_agentes):
                        if(i == j):
                            continue
                        elif(agentes[i].x + posx == agentes[j].x and agentes[i].y + posy == agentes[j].y):
                            cont_temporal += 1
                    if(cont_temporal == 0):
                        agentes[i].x += posx
                        agentes[i].y += posy
                        print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                        movimientos += 1
                        ciclo = False
                
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
                        cont_temporal = 0
                        for j in range (cant_agentes):
                            if(i == j):
                                continue
                            elif(agentes[i].x + posx == agentes[j].x and agentes[i].y + posy == agentes[j].y):
                                cont_temporal += 1
                        if(cont_temporal == 0):
                            agentes[i].x += rand_val_1
                            agentes[i].y += rand_val_2
                            print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                            movimientos += 1
                            ciclo = False
                        else:
                            ciclo = False

                if(count%3 == 0):
                    posy= -1
                    posx += 1
                else:
                    posy += 1
                if(ciclo == True):
                    count += 1                        
              
        elif(habitaciones[agentes[i].x][agentes[i].y] == 0):
            visitadas[agentes[i].x][agentes[i].y] = 1
            ciclo = True
            posx = -1
            posy = -1
            count = 1
            while(ciclo == True):
                if((agentes[i].x+posx) >= 0 and
                   (agentes[i].x+posx) <= (filas-1) and
                   (agentes[i].y+posy) >= 0 and
                   (agentes[i].y+posy) <= (columnas-1) and
                   visitadas[agentes[i].x + posx][agentes[i].y + posy] == 0 and count<=9):
                    cont_temporal = 0
                    for j in range (cant_agentes):
                        if(i == j):
                            continue
                        elif(agentes[i].x + posx == agentes[j].x and agentes[i].y + posy == agentes[j].y):
                            cont_temporal += 1
                    if(cont_temporal == 0):
                        agentes[i].x += posx
                        agentes[i].y += posy
                        print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                        movimientos += 1
                        ciclo = False
                
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
                        cont_temporal = 0
                        for j in range (cant_agentes):
                            if(i == j):
                                continue
                            elif(agentes[i].x + posx == agentes[j].x and agentes[i].y + posy == agentes[j].y):
                                cont_temporal += 1
                        if(cont_temporal == 0):
                            agentes[i].x += rand_val_1
                            agentes[i].y += rand_val_2
                            print("Moviendo agente " +str(i+1)+ " a la casilla ("+str(agentes[i].x +1)+", "+str(agentes[i].y + 1)+")")
                            movimientos += 1
                            ciclo = False
                        else:
                            ciclo = False

                if(count%3 == 0):
                    posy= -1
                    posx += 1
                else:
                    posy += 1
                if(ciclo == True):
                    count += 1
                    
                    
    fin = time.time()
    tiempo += (fin-inicio)


print(habitaciones)
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
