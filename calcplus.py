#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calculadorahija
import csv

with open(sys.argv[1], newline="") as csvfile:
    operaciones = csv.reader(csvfile)
    result = 0
    for operacion in operaciones:
        try:
            operador = operacion[0]
        except IndexError:
            print("Can't read operation")
            sys.exit(0)

        operadores = operacion[1:]

        try:
            if operador == "suma":
                result = int(operacion[1])
                for operandos in operadores[1:]:
                    operar = calculadorahija.CalculadoraHija(result, int(operandos))
                    result = operar.suma()

                print(result)
            elif operador == "resta":
                result = int(operacion[1])
                for operandos in operadores[1:]:
                    operar = calculadorahija.CalculadoraHija(result, int(operandos))
                    result = operar.resta()

                print(result)
            elif operador == "multiplica":
                result = int(operacion[1])
                for operandos in operadores[1:]:
                    operar = calculadorahija.CalculadoraHija(result, int(operandos))
                    result = operar.multiplicacion()

                print(result)
            elif operador == "divide":
                result = int(operacion[1])
                try:
                    for operandos in operadores[1:]:
                        operar = calculadorahija.CalculadoraHija(result, int(operandos))
                        result = operar.division()
                    print(result)
                except TypeError:
                    sys.exit
        except ValueError:
            print("Error reading value")
            sys.exit
