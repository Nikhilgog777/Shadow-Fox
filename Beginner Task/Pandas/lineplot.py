import pandas as pd
import matplotlib.pyplot as plt

# Sample time-series data
df = pd.DataFrame({
    'year': [2015, 2016, 2017, 2018, 2019, 2020],
    'sales': [250, 280, 310, 350, 400, 380],
    'profit': [30, 35, 40, 50, 65, 55]
})

# Line chart with two lines
df.plot.line(x='year', y=['sales', 'profit'], marker='o', title='Sales and Profit Over Time')
plt.xlabel('Year')
plt.ylabel('Amount (k$)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
