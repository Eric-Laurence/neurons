# Eric's Neural Net library

class ArgumentError (Exception):
    pass

class Neuron:
    '''
    A single neuron.
    '''

    def __init__(self, bias, *weights):
        '''
        Be careful when passing in a list with
        splat--the first argument must be the
        bias, not a weight.
        '''
        self.bias = bias
        self.weights = weights

    def weightedSum (self, *inputs):
        if len(inputs) != len(self.weights):
            raise ArgumentError(
                "Had %s inputs, %s weights"
                % (len(inputs), len(self.weights)))

        sum = self.bias
        for i in range(len(inputs)):
            sum += inputs[i] * self.weights[i]

        return sum

    def activate (self, x):
        if x > 0.5:
            return 1
        else:
            return 0

    def output (self, *inputs):
        return self.activate(self.weightedSum(*inputs)) 

