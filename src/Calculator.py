import math

def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b



class Calculator:
    result = 0

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result



