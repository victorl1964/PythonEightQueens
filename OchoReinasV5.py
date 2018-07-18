#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 1) La descripción del PROBLEMA OCHO REINAS se encuentra en la versión 1
#
# 2) En esta versión, generalizamos el problema a un TABLERO de M filas y COLUMNAS
# M>=2
#
# 3) UNA SOLUCION MAS EFICIENTE que la implementada en OchoReinasV4
#    a) dos reinas no deben compartir la misma diagonal
#    b) dos reinas no deben compartir la misma columna
#
#    Para verificar si dos reinas comparten la misma diagonal se hace lo sig:
#    i es la fila o posición del arreglo donde quiero colocar una REINA en una columna (j)
#    k es cualquier fila < i (las ocupadas hasta ahora)
#
#    si abs(i-k) == abs (j-SOLUTIONf[k]) entonces
#          las reinas en las posiciones i y k comparten la misma diagonal
#    ejemplo:
#    La solucion
#        0,2,4,6,1,3,5,7 no es viable porque para i=0, j=7
#            j-i = 7, y SOLUTIONf[j]-SOLUTIONf[i]=7
#    Luego, al intentar  colocar una columna en una posición del
#    arreglo, se debe verificar,contra todas las posiciones
#    anteriores:
#          Que no compartan la misma diagonal :
#          Que no compartan la misma columna  :
#
import numpy as arreglo
import math
import time

def mostrar_solucion(FILAS):
    print(FILAS)
    print("-"*(2*M+1))
    for i in range(M):
        linea=" "
        for j in range(M):
            if j==FILAS[i]:
                linea+="R "
            else:
                linea+="* "
        print(linea)
    print("-"*(2*M+1))


def posicion_nueva_reina(FILAS,i,col):
    columna=-1
    j=col
    while j < M:
        k=0
        matched=False
        while k < i and not matched:
            """ j representa el valor (columna) que quiero colocar en FILAS """
            """ Si ya existe en alguna fila entre k e i-1 (j==FILAS[k]) """
            """ o si la DIFERENCIA entre FILAS es igual a la DIFERENCIA entre """
            """ columnas,!!! HAY QUE BUSCAR OTRA COLUMNA !!! """
            if FILAS[k]==j or  math.fabs(i-k) == math.fabs(j-FILAS[k]):
                matched=True
            else:
                k+=1
        if not matched:
            columna=j
            j=M
        else:
            j+=1
    return columna

#
# LEEMOS LA DIMENSIÓN DEL TABLERO
#
M=int(input("Introduzca un entero para indicar el tamaño del TABLERO: "))
#
columna = int(input("Introduzca COLUMNA para REINA en 1era FILA (0 <= COLUMNA < " + str(M) + "): "))
#
while columna < 0 or columna > M-1:
    columna=int(input("COLUMNA fuera de rango...Introduzca otro número :"))

print ("La primera REINA va en la  FILA 0, COLUMNA " + str(columna))
t0 = time.clock()

#
#CREAMOS LOS ARREGLOS DONDE MANTENDREMOS LA SOLUCIÓN PARCIAL.
# FILAS mantendrá las columnas ocupadas en cada fila
# Si FILAS[0]=3 significa que en la fila 0 está ocupada la columna 3
#
FILAS=arreglo.empty((M), dtype='int')
#
#Inicializamos TABLERO y SOLUCION con "-1" y "*"
#
for i in range(M):
    FILAS[i]=-1

#Colocamos en la primera fila, la columna introducida por el usuario
FILAS[0]=columna



i=1
j=0
while i > 0 and i < M:
    columna=posicion_nueva_reina(FILAS,i,j)
    if columna != -1:
        FILAS[i]=columna
        i+=1
        j=0
    else:
        """Me regreso de fila, elimino la solución para esa fila"""
        """y pruebo con la siguiente columna en esa fila"""
        i-=1
        j=FILAS[i]+1
        FILAS[i]=-1
    """Si hay una solución, la muestro, me regreso de fila para buscar mas"""
    """soluciones..."""
    if i==M and FILAS[i-1] != -1:
        mostrar_solucion(FILAS)
        i-=1
        j=FILAS[i]+1
        FILAS[i]=-1


t1 = time.clock()
print("TIEMPO TOTAL {0:.4f} SEGUNDOS...".format(t1-t0))

