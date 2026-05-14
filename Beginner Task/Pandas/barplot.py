import pandas as pd
import matplotlib.pyplot as plt

# Sample data: product sales
df = pd.DataFrame({
    'product': ['A', 'B', 'C', 'D', 'E'],
    'sales': [120, 95, 150, 80, 110],
    'profit': [30, 25, 40, 18, 35]
})

# Bar plot
df.plot.bar(x='product', y='sales', color='skyblue', edgecolor='black', legend=False)
plt.title('Product Sales', fontsize=14)
plt.xlabel('Product')
plt.ylabel('Sales (units)')
plt.xticks(rotation=45)  # Rotate x labels if needed
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
