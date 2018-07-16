a = 2
b = 4

def weightedSum (x, y):
    return a*x + b*y

def activate (x):
    if x > 0.5:
        return 1
    else:
        return 0
    
def output (x, y):
    return activate(weightedSum(x, y)) 
    
#print("%d" % weightedSum(5, 3))
print(weightedSum(5, 3)) 
print(activate(weightedSum(5, 3)))
print(output(5, 3))

    