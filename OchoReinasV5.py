#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 1) Descripción del PROBLEMA

# Este programa se encarga de encontrar una solución al probrema de las Ocho
# REINAS, que consiste en colocar 1 REINA en cada fila del tablero (matriz 8x8)
# sin que ninguna REINA pueda atacar a otra. Para ello:
#
# 1.- Generaremos un múmero RANDOM entre 0 y 7, para colocar una reina en
# una columna de la 1era fila de la matriz
#
# 2.- A partir de la 2da fila, desde la primera columna, buscaremos si hay
# alguna REINA en direcciones NorOESTE, NORTE y NorESTE. En caso negativo
# (NO HAY REINAS), colocamos una REINA en esa fila/columna, de lo contrario,
# avanzamos de columna ...
# Nota: no se busca en direcciones:
# -oeste
# -este
# -sur
# -sureste
# -suroeste
#.............porque el algoritmo no puede haber puesto una REINA en ellas
#
# 3) En esta solución el problema se extiende a un TABLERO de M filas y COLUMNAS
# M>=2
#
# 4) Muestra todas las soluciones encontradas cuando una reina se coloca en
#    la posición determinada en 1)
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




