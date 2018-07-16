# Eric's Neural Net library

class ArgumentError (Exception):
    pass

class Neuron:

    def __init__(self, *coefficients):
        self.coefficients = coefficients

    def weightedSum (self, *inputs):
        if len(inputs) != len(self.coefficients):
            raise ArgumentError

        sum = 0
        for i in range(len(inputs)):
            sum += inputs[i] * self.coefficients[i]

        return sum

    def activate (self, x):
        if x > 0.5:
            return 1
        else:
            return 0

    def output (self, *inputs):
        return self.activate(self.weightedSum(*inputs)) 

