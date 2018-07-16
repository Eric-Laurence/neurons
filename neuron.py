#!/usr/bin/python3

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

input_list = [
    (5, 3),
    (7, 0),
    (3, 5),
    (-5, 3)
]

coefficient_list = [
    (2, 4),
    (9, 3),
    (5, 2),
    (8, 5)
]

neuron_list = []

for a, b in coefficient_list:
    neuron_list.append(Neuron(a, b))
    
    
for neuron_i, neuron in enumerate(neuron_list):
    print()
    print("neuron " + str(neuron_i + 1))
    for x, y in input_list:
        print("    weighted sum: " + str(neuron.weightedSum(x, y)))
        print("    output: " + str(neuron.output(x, y)))
        

print()
print("Test three inputs:")
neuron1 = Neuron(3, 2, 1)
print("    weighted sum: " + str(neuron1.weightedSum(1, 2, 3)))
print("    output: " + str(neuron1.output(1, 2, 3)))


    