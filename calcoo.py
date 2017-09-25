#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Calculadora:
    def __init__(self, valor1, valor2):
        self.valor1 = valor1
        self.valor2 = valor2
    def suma(self):
        return (self.valor1 + self.valor2)


if __name__ == "__main__":
    op1 = Calculadora("2", "3")
    result = op1.suma()
    print (result)
    print ("Este va a ser la calculadora")
