import math

def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b

def subtraction(a,b):
    a = int(a)
    b = int(b)
    return b - a

def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = a * b
    return c




class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def sub(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def mul(self, a, b):
        self.result = multiplication(a, b)
        return self.result



