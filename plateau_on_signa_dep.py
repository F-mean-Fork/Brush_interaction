import data_preparation as dp
import matplotlib.pyplot as plt
import glob
import os
import numpy as np

X = dp.ans
Y = []
for i in range(61):
    for filename in glob.glob(f'C:\\Users\\ivanl\\Desktop\\ITMO\\Brush_interaction\\{i}.txt'):
        with open(os.path.join(os.getcwd(), filename), 'r') as f:
            data = []
            for line in f.readlines():
                data.append(list(map(float, line.split())))
        data = np.array(data)
        y = data[:, 0]
        Y.append(y[-3])

X = np.array(X)  # sigma
Y = np.array(Y)  # energy value
Y = (Y + 2.0 * dp.theta) / (2.0 * X)  # normalized value

plt.plot(X, Y, color='black', marker='.')
plt.ylabel('Plateau value', size=18)
plt.xlabel(r'$\sigma$', size=18)
plt.title(r'Plateau value on $\sigma$ value dependence')
plt.show()
