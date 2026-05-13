import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.normal(100, 50, 100)
y1 = np.random.normal(100, 50, 100)
x2 = np.random.normal(120, 60, 100)
y2 = np.random.normal(120, 60, 100)
fig = plt.figure(figsize=(3, 3))
plt.scatter(x1, y1, color='blue', label='Group 1')
plt.scatter(x2, y2, color='red', label='Group 2')
plt.title('Scatter Plot of Two Groups')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend(["plt1", "plt2"])
plt.show()