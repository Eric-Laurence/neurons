class Neuron:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
    

    def weightedSum (self, x, y):
        return self.a*x + self.b*y

    def activate (self, x):
        if x > 0.5:
            return 1
        else:
            return 0
    
    def output (self, x, y):
        return self.activate(self.weightedSum(x, y)) 

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

for (a, b) in coefficient_list:
    neuron_list.append(Neuron(a, b))
    
    
for neuron_i, neuron in enumerate(neuron_list):
    print("neuron " + str(neuron_i + 1))
    for (x, y) in input_list:
        print("    " + str(neuron.weightedSum(x, y)))
        print("    " + str(neuron.output(x, y)))


    