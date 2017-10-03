#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys


class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2

    def suma(self):
        return (self.valor1 + self.valor2)

    def resta(self):
        return (self.valor1 - self.valor2)

def operaciones(arg):
    operacion = Calculadora(int(sys.argv[1]), int(sys.argv[3]))
    if arg == "suma":
        result = operacion.suma()
    elif arg == "resta":
        result = operacion.resta()
    return(result)

if __name__ == "__main__":
    result = operaciones(sys.argv[2])
    print(result)
