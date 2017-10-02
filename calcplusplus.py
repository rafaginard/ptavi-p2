#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if len(sys.argv) != 2:
    sys.exit("Try: ./calcplusplus.py file")
try:
    with open(sys.argv[1], newline="") as csvfile:
        operaciones = csv.reader(csvfile)
        result = 0
#  Busco la operacion en la primera posicion de cada linea del fichero.
        for operacion in operaciones:
            try:
                operador = operacion[0]
            except IndexError:
                sys.exit("Can't read operation")
#  Me quedo con la parte de la lista de los operadores.
            operadores = operacion[1:]
            result = int(operacion[1])
            for operandos in operadores[1:]:
                try:
                    operar = calcoohija.CalculadoraHija(result, int(operandos))
                except ValueError:
                    sys.exit("Error reading value")

                if operador == "suma":
                    result = operar.suma()
                elif operador == "resta":
                    result = operar.resta()
                elif operador == "multiplica":
                    result = operar.multiplicacion()
                elif operador == "divide":
                    try:
                        result = operar.division()
                    except TypeError:
                        sys.exit
            print(result)
except FileNotFoundError:
    sys.exit("File not found")
