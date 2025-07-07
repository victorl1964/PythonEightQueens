# EightQueens

A python implementation of the famous EightQueens problem

This program finds all the solutions to the famous EightQueens problem, for any MxM
square matrix

- We first ask for the matrix dimension (how many rows and columns)

- Then, we ask which column the user wants to place a Queen in the first row

# Running th script

python3 OchoReinasV5.py
Introduzca un entero para indicar el tamaño del TABLERO: 8
Introduzca COLUMNA para REINA en 1era FILA (0 <= COLUMNA < 8): 7

La primera REINA va en la  FILA 0, COLUMNA 7
```
            [7 1 3 0 6 4 2 5]
            -----------------
            * * * * * * * R 
            * R * * * * * * 
            * * * R * * * * 
            R * * * * * * * 
            * * * * * * R * 
            * * * * R * * * 
            * * R * * * * * 
            * * * * * R * * 
            -----------------
            [7 1 4 2 0 6 3 5]
            -----------------
            * * * * * * * R 
            * R * * * * * * 
            * * * * R * * * 
            * * R * * * * * 
            R * * * * * * * 
            * * * * * * R * 
            * * * R * * * * 
            * * * * * R * * 
            -----------------
            [7 2 0 5 1 4 6 3]
            -----------------
            * * * * * * * R 
            * * R * * * * * 
            R * * * * * * * 
            * * * * * R * * 
            * R * * * * * * 
            * * * * R * * * 
            * * * * * * R * 
            * * * R * * * * 
            -----------------
            [7 3 0 2 5 1 6 4]
            -----------------
            * * * * * * * R 
            * * * R * * * * 
            R * * * * * * * 
            * * R * * * * * 
            * * * * * R * * 
            * R * * * * * * 
            * * * * * * R * 
            * * * * R * * * 
            -----------------
```
