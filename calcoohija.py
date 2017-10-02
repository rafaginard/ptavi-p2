#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

# Se puede poner la clase directamente en le archivo o bien importarlo
# con comando from **** import **** ###

# class Calculadora:
#     def __init__(self, valor1, valor2):
#        self.valor1 = valor1
#        self.valor2 = valor2
#    def suma(self):
#        return (self.valor1 + self.valor2)
#    def resta(self):
#        return (self.valor1 - self.valor2)
#


class CalculadoraHija(Calculadora):

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        try:
            return self.valor1 / self.valor2
        except ZeroDivisionError:
            print("Division by zero is not allowed")


if __name__ == "__main__":
    operacion = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))
try:
    if sys.argv[2] == "suma":
        result = operacion.suma()
    elif sys.argv[2] == "resta":
        result = operacion.resta()
    elif sys.argv[2] == "por":
        result = operacion.multiplicacion()
    elif sys.argv[2] == "dividido":
        result = operacion.division()
    print(result)
except NameError:
    sys.exit("Can only: suma, resta, por, dividido")
