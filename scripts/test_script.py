from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

X = [0, 1, 7, 3, 8]
Y = [5, 4, 7, 8, 9]
Z = [1, 3, 2, 7, 1]

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

ax.scatter(X, Y, Z, c = 'c', marker = 'o')
plt.show()
