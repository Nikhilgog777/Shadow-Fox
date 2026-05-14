import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])


fig = plt.figure(figsize=(4, 4))
plt.bar(x, y, width = 0.5, color = 'lightblue')
plt.title('Bar Chart Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
