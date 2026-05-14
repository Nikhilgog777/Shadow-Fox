import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Random data
np.random.seed(42)
x = np.random.randn(1000)
y = x * 0.5 + np.random.randn(1000) * 0.3

df = pd.DataFrame({'x': x, 'y': y})

plt.figure(figsize=(8, 6))
hb = plt.hexbin(df['x'], df['y'], gridsize=30, cmap='YlOrRd', edgecolors='gray', linewidths=0.2)
plt.colorbar(hb, label='Count in bin')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Hexbin Plot of Random Data')
plt.grid(alpha=0.3)
plt.show()
