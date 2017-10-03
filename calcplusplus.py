#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import calcoohija
import csv

with open(sys.argv[1], newline="") as csvfile:
    operaciones = csv.reader(csvfile)
    for operacion in operaciones:
        try:
            operador = operacion[0]
        except IndexError:
            sys.exit("Can't read operation")
        operadores = operacion[1:]
        result = int(operacion[1])
        for operandos in operadores[1:]:
            operar = calcoohija.CalculadoraHija(result, int(operandos))
            result = operar.operaciones(operador)
        print(result)
