import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Setup: Make the charts look professional
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (10, 6)

# --- Visual 1: Price Distribution (Histogram) ---
plt.figure()
sns.histplot(data=df, x='Price', kde=True, color='teal', bins=20)
plt.title('Market Overview: Distribution of Book Prices', fontsize=16)
plt.xlabel('Price (£)')
plt.ylabel('Count of Books')
plt.show()

# --- Visual 2: Top 10 Genres by Stock Count (Bar Chart) ---
plt.figure()
# We count the books per genre, take the top 10, and plot them
top_genres = df['Genre'].value_counts().head(10).index
sns.countplot(data=df[df['Genre'].isin(top_genres)], y='Genre', order=top_genres, palette='viridis')
plt.title('Inventory Composition: Top 10 Genres', fontsize=16)
plt.xlabel('Number of Unique Books')
plt.ylabel('Genre')
plt.show()

# --- Visual 3: Price Ranges by Genre (Box Plot) ---
plt.figure()
# We use the same 'top_genres' to keep the chart readable
sns.boxplot(data=df[df['Genre'].isin(top_genres)], x='Price', y='Genre', palette='coolwarm')
plt.title('Pricing Strategy: Price Ranges by Top Genres', fontsize=16)
plt.xlabel('Price (£)')
plt.show()

# --- Visual 4: Inventory Risk (Scatter Plot) ---
plt.figure()
# Scatter plot to see if expensive books are stocked in high quantities
sns.scatterplot(data=df, x='Price', y='Amount_Available', hue='Genre', alpha=0.7, size='Price')
plt.title('Inventory Risk: Price vs. Availability', fontsize=16)
plt.xlabel('Price per Book (£)')
plt.ylabel('Stock Count')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left') # Moves legend outside
plt.tight_layout()
plt.show()