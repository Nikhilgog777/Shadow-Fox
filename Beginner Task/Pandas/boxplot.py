import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame with numeric columns
df = pd.DataFrame({
    'species': ['Adelie']*4 + ['Chinstrap']*4 + ['Gentoo']*4,
    'flipper_length': [181, 185, 182, 188, 195, 198, 196, 200, 210, 212, 205, 208]
})

# Box plot grouped by species
df.boxplot(column='flipper_length', by='species', grid=True, patch_artist=True)
plt.title('Flipper Length Distribution by Species')
plt.suptitle('')  # Remove default "Boxplot grouped by..." title
plt.xlabel('Species')
plt.ylabel('Flipper Length (mm)')
plt.xticks(rotation=45)
plt.show()
