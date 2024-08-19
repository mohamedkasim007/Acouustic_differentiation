import numpy as np
from matplotlib.pyplot import step, show

def binary_data(data):
    return [1 if x in data else 0 for x in range(data[-1] + 1)]

data = [1, 2, 4, 5, 9]
bindata = binary_data(data)
xaxis = np.arange(0, data[-1] + 1)
yaxis = np.array(bindata)
step(xaxis, yaxis)
show()
