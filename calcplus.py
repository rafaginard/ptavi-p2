#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

with open("fichero.csv", newline = "") as csvfile:
    operaciones = csv.reader(csvfile)
    result = 0
    for operacion in operaciones:
        operador = operacion[0]
        operadores = operacion[1:]

        if operador == "suma":
            result = int(operacion[1])
            for operandos in operadores[1:]:
                result += int(operandos)

            print (result)
        elif operador == "resta":
            result = int(operacion[1])
            for operandos in operadores[1:]:
                result -= int(operandos)

            print (result)
        elif operador == "multiplica":
            result = int(operacion[1])
            for operandos in operadores[1:]:
                result *= int(operandos)

            print (result)
        elif operador == "divide":
            result = int(operacion[1])
            for operandos in operadores[1:]:
                result /= int(operandos)
                
            print (result)
