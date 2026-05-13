import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(42)
x = np.linspace(0, 10, 50)
y = 2 * x + 1 + np.random.normal(0, 2, size=len(x))

# Create DataFrame
df = pd.DataFrame({'x': x, 'y': y})

# Fit regression line
slope, intercept = np.polyfit(df['x'], df['y'], 1)
reg_line = slope * df['x'] + intercept

# Plot
plt.scatter(df['x'], df['y'], label='Data')
plt.plot(df['x'], reg_line, color='red', label=f'Regression (y={slope:.2f}x+{intercept:.2f})')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Regression Plot')
plt.legend()
plt.show()