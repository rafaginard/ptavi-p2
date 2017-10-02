#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

if len(sys.argv) != 2:
    sys.exit("Try: ./calcplusplus.py fichero")

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

        try:
            if operador == "suma":
                result = int(operacion[1])
                for operandos in operadores[1:]:
                    operar = calcoohija.CalculadoraHija(result, int(operandos))
                    result = operar.suma()

                print(result)
            elif operador == "resta":
                result = int(operacion[1])
                for operandos in operadores[1:]:
                    operar = calcoohija.CalculadoraHija(result, int(operandos))
                    result = operar.resta()

                print(result)
            elif operador == "multiplica":
                result = int(operacion[1])
                for operandos in operadores[1:]:
                    operar = calcoohija.CalculadoraHija(result, int(operandos))
                    result = operar.multiplicacion()

                print(result)
            elif operador == "divide":
                result = int(operacion[1])
                try:
                    for operandos in operadores[1:]:
                        operar = calcoohija.CalculadoraHija(result,
                                                            int(operandos))
                        result = operar.division()
                    print(result)
                except TypeError:
                    sys.exit
        except ValueError:
            sys.exit("Error reading value")
