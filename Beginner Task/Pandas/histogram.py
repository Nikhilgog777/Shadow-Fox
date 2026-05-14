import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame with a numeric column
df = pd.DataFrame({
    'flipper_length_mm': [181, 195, 210, 185, 198, 205, 182, 212, 196, 188,
                          190, 193, 200, 202, 186, 189, 194, 208, 213, 180]
})

# Histogram using pandas
df['flipper_length_mm'].plot.hist(
    bins=10,                # number of bins
    edgecolor='black',     # bar borders
    color='skyblue',
    alpha=0.7,
    title='Distribution of Flipper Length'
)

plt.xlabel('Flipper Length (mm)')
plt.ylabel('Frequency')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()
