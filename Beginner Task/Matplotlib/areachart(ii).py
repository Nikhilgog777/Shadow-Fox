import numpy as np
import matplotlib.pyplot as plt

x = [1,3,5,7,9]
y1 = [2,3,4,5,6]
y2 = [3,4,5,6,7]
y3 = [2,4,6,8,10]

plt.stackplot(x, y1, y2, y3)
plt.show()
