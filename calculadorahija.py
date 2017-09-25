#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

### Se puede poner la clase directamente en le archivo o bien importarlo
### con comando from **** import **** ###

#class Calculadora:
    #def __init__(self, valor1, valor2):
    #    self.valor1 = valor1
    #    self.valor2 = valor2
##    def suma(self):
##        return (self.valor1 + self.valor2)
##    def resta(self):
##        return (self.valor1 - self.valor2)
##
class CalculadoraHija(Calculadora):
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        return self.valor1 / self.valor2

if __name__ == "__main__":
    operacion = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))

    if sys.argv[2] == "suma":
        result = operacion.suma()
    elif sys.argv[2] == "resta":
        result = operacion.resta()
    elif sys.argv[2] == "por":
        result = operacion.multiplicacion()
    elif sys.argv[2] == "dividido":
        result = operacion.division()

    print (result)
