import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(100, 50, 1000)
fig = plt.figure(figsize=(3, 3))
plt.hist(x, bins=50, color='blue', edgecolor='black')
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()
