import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# Create random data
np.random.seed(42)
df = pd.DataFrame({
    'height': np.random.normal(170, 10, 100),
    'weight': np.random.normal(70, 15, 100),
    'age': np.random.randint(18, 70, 100)
})

# Customized scatter plot
df.plot.scatter(
    x='height',
    y='weight',
    c='age',              # color points by 'age' column
    colormap='viridis',   # color map for 'c'
    s=50,                 # marker size
    alpha=0.6,            # transparency
    title='Height vs Weight colored by Age',
    xlabel='Height (cm)',
    ylabel='Weight (kg)',
    edgecolors='black',
    linewidth=0.5
)
plt.show()
