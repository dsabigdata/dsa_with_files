import math
import numpy as np

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def square(self, a):
        return a * a
    
    def square_root(self, a):
        return math.sqrt(a)
    
    def matrix_multiply(self, a, b):
        return np.dot(a, b)
    
    #test the calculator
    def test_calculator(self):
        assert self.add(1, 2) == 5
        assert self.subtract(1, 2) == -1
        assert self.multiply(1, 2) == 2
        assert self.divide(1, 2) == 0.5
        assert self.square(2) == 4
        assert self.square_root(4) == 2
        assert self.matrix_multiply(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]])) == np.array([[19, 22], [43, 50]])