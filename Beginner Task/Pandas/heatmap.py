import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate random DataFrame with numeric and categorical columns
np.random.seed(42)
n = 100
df = pd.DataFrame({
    'length': np.random.normal(40, 5, n),
    'depth': np.random.normal(15, 2, n),
    'weight': np.random.normal(4000, 500, n),
    'species': np.random.choice(['Adelie', 'Chinstrap', 'Gentoo'], n),
    'island': np.random.choice(['Torgersen', 'Biscoe', 'Dream'], n),
    'sex': np.random.choice(['Male', 'Female'], n)
})

# Encode categoricals and plot correlation heatmap
df_encoded = pd.get_dummies(df, drop_first=True)
plt.figure(figsize=(6, 6))
sns.heatmap(df_encoded.corr(), annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Random Data")
plt.tight_layout()
plt.show()
