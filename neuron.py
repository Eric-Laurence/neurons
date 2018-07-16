a = 2
b = 4


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


neuron1 = Neuron(a, b)


#print("%d" % weightedSum(5, 3))
print(neuron1.weightedSum(5, 3)) 
print(neuron1.activate(neuron1.weightedSum(5, 3)))
print(neuron1.output(5, 3))

    