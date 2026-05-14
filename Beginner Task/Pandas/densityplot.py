import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Sample DataFrame with multiple numeric features (columns)
np.random.seed(42)
df = pd.DataFrame({
    'sepal_length': np.random.normal(5.8, 0.5, 300),
    'sepal_width': np.random.normal(3.0, 0.4, 300),
    'petal_length': np.random.normal(4.0, 1.2, 300),
    'petal_width': np.random.normal(1.2, 0.6, 300)
})

# Density plot for all features
df.plot.density(
    linewidth=2,
    alpha=0.7,
    title='Density Distribution of Multiple Features'
)

# Customization using matplotlib
plt.xlabel('Value')
plt.ylabel('Density')
plt.grid(True, linestyle='--', alpha=0.3)
plt.legend(title='Features', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
