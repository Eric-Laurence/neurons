#!/usr/bin/python3

from neuron import Neuron

input_list = [
    (5, 3),
    (7, 0),
    (3, 5),
    (-5, 3)
]

weights_list = [
    (0, 2, 4),
    (0, 9, 3),
    (0, 5, 2),
    (0, 8, 5)
]

neuron_list = []

for weights in weights_list:
    neuron_list.append(Neuron(*weights))
    
    
for neuron_i, neuron in enumerate(neuron_list):
    print()
    print("neuron " + str(neuron_i + 1))
    for x, y in input_list:
        print("    weighted sum: " + str(neuron.weightedSum(x, y)))
        print("    output: " + str(neuron.output(x, y)))
        

print()
print("Test three inputs:")
neuron1 = Neuron(0, 3, 2, 1)
print("    weighted sum: " + str(neuron1.weightedSum(1, 2, 3)))
print("    output: " + str(neuron1.output(1, 2, 3)))


    