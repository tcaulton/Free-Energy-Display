import matplotlib.pyplot as plt
from matplotlib import style
import csv
from csv import reader

with open('testData.csv', 'r') as f:
    data = list(reader(f))

def getGib(variable1, variable2):
    hydroFreeE = int(data[variable1][variable2])
    return hydroFreeE

def graph():
    x = []
    y = []
    for i in range(40):
        x.append(i)
    for i in range(40):
        pressure = (i * getGib(2, 3)) + 20
        y.append(pressure)
    print(x)
    print(y)
    plt.plot(x, y)
    plt.savefig('foo.png', bbox_inches='tight')



graph()
