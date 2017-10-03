#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora

class CalculadoraHija(Calculadora):

    def multiplicacion(self):
        return self.valor1 * self.valor2

    def division(self):
        try:
            return self.valor1 / self.valor2
        except ZeroDivisionError:
            print("Division by zero is not allowed")

    def operaciones(self, cuenta):
        try:
            if cuenta == "suma":
                result = self.suma()
            elif cuenta == "resta":
                result = self.resta()
            elif cuenta == "multiplica":
                result = self.multiplicacion()
            elif cuenta == "divide":
                result = self.division()
            return(result)
        except NameError:
            sys.exit("Can only: suma, resta, por, dividido")

if __name__ == "__main__":
    operacion = CalculadoraHija(int(sys.argv[1]), int(sys.argv[3]))
    result = operacion.operaciones(sys.argv[2])
    print(result)
