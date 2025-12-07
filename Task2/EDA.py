import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for better visualizations
sns.set_style("whitegrid")
plt.rcParams['figure.dpi'] = 100

# Load cleaned data with error handling
file_path = 'E:/CodeAlpha_DataAnalytics_tasks/CodeAlpha_DataAnalytics_Tasks/Task1/cleaned_books.csv'

try:
    # Try the original path first
    if os.path.exists(file_path):
        books_eda = pd.read_csv(file_path)
    else:
        # Try relative path as fallback
        books_eda = pd.read_csv('cleaned_books.csv')
    
    print("Dataset loaded successfully!")
    print(f"Shape: {books_eda.shape}")
    print(f"\nColumns: {list(books_eda.columns)}")
    
except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
    print("Please update the file path or place 'cleaned_books.csv' in the current directory.")
    exit()

# --Part 1: Ask Meaningful Questions--

# 1. Pricing Trends: Average Price by Genre
if 'Genre' in books_eda.columns and 'Price' in books_eda.columns:
    print("\n" + "="*60)
    print("--- Average Price by Genre ---")
    genre_pricing = books_eda.groupby('Genre')['Price'].mean().sort_values(ascending=False)
    print(genre_pricing)
else:
    print("\nWarning: 'Genre' or 'Price' column not found.")

# 2. Inventory Efficiency: Relationship between Price and Stock
if 'Amount_Available' in books_eda.columns and 'Price' in books_eda.columns:
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=books_eda, x='Price', y='Amount_Available', 
                   hue='Genre' if 'Genre' in books_eda.columns else None, 
                   alpha=0.6)
    plt.title('Inventory Efficiency: Price vs. Amount Available')
    plt.xlabel('Price (£)')
    plt.ylabel('Stock Count')
    if 'Genre' in books_eda.columns:
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig('inventory_efficiency.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("\nPlot saved as 'inventory_efficiency.png'")
else:
    print("\nWarning: Required columns for inventory analysis not found.")

# --- Question 3: Inventory Balance ---
if 'Genre' in books_eda.columns:
    genre_share = books_eda['Genre'].value_counts(normalize=True) * 100
    
    print("\n" + "="*60)
    print("--- Inventory Market Share by Genre (%) ---")
    print(genre_share.head(5))
    
    # Visualization: Pie Chart for top 5 genres
    plt.figure(figsize=(8, 8))
    top_5_genres = genre_share[:5]
    if len(genre_share) > 5:
        other_share = pd.Series([genre_share[5:].sum()], index=['Others'])
        combined_share = pd.concat([top_5_genres, other_share])
    else:
        combined_share = top_5_genres
    
    plt.pie(combined_share, labels=combined_share.index, autopct='%1.1f%%', startangle=140)
    plt.title('Inventory Concentration: Share of Books by Genre')
    plt.savefig('genre_distribution.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Plot saved as 'genre_distribution.png'")

# --- Question 4: Capital Allocation (High-Value Assets) ---
if 'Amount_Available' in books_eda.columns and 'Price' in books_eda.columns:
    books_eda['Potential_Revenue'] = books_eda['Price'] * books_eda['Amount_Available']
    
    cols_to_show = ['Name', 'Price', 'Amount_Available', 'Potential_Revenue']
    if 'Genre' in books_eda.columns:
        cols_to_show.insert(1, 'Genre')
    
    top_assets = books_eda[cols_to_show].sort_values(by='Potential_Revenue', ascending=False).head(5)
    
    print("\n" + "="*60)
    print("--- Top 5 High-Value Assets (Books with most capital tied up) ---")
    print(top_assets.to_string(index=False))

print("\n" + "="*60)
# --Part 2: Explore the Data Structure & Redundancy Check--

print("\n" + "="*60)
print("--- DATA STRUCTURE ANALYSIS ---")

# 1. Redundancy Check: Is 'Type' always just "Books"?
if 'Type' in books_eda.columns:
    unique_types = books_eda['Type'].unique()
    print(f"\nUnique values in 'Type' column: {unique_types}")
    
    if len(unique_types) == 1 and unique_types[0] == 'Books':
        print("Result: The 'Type' column is redundant and can be dropped.")
else:
    print("\nNote: 'Type' column not found in dataset.")

# 2. Variable Consistency: Are Price and Price_Excl_Tax identical?
if 'Price_Excl_Tax' in books_eda.columns and 'Price' in books_eda.columns:
    inconsistent_rows = books_eda[books_eda['Price'] != books_eda['Price_Excl_Tax']]
    print(f"\nNumber of rows where Price != Price_Excl_Tax: {len(inconsistent_rows)}")
    
    if len(inconsistent_rows) == 0:
        print("Result: 'Price' and 'Price_Excl_Tax' are identical duplicates.")
    else:
        print(f"Result: Found {len(inconsistent_rows)} rows with differences.")
else:
    print("\nNote: 'Price_Excl_Tax' column not found in dataset.")

# --Part 3: Identify Trends, Patterns & Anomalies--

print("\n" + "="*60)
print("--- TRENDS, PATTERNS & ANOMALIES ---")

# 1. Category Domination: Total Inventory Value by Genre
if 'Amount_Available' in books_eda.columns and 'Price' in books_eda.columns and 'Genre' in books_eda.columns:
    books_eda['Total_Inventory_Value'] = books_eda['Price'] * books_eda['Amount_Available']
    top_genres_value = books_eda.groupby('Genre')['Total_Inventory_Value'].sum()\
        .sort_values(ascending=False).head(5)
    
    print("\n--- Top 5 Genres by Inventory Value ---")
    print(top_genres_value)

# 2. Outlier Detection: Finding luxury/anomalous book prices
if 'Genre' in books_eda.columns and 'Price' in books_eda.columns:
    plt.figure(figsize=(12, 6))
    
    # Limit to top 10 genres for readability
    top_genres = books_eda['Genre'].value_counts().head(10).index
    filtered_data = books_eda[books_eda['Genre'].isin(top_genres)]
    
    sns.boxplot(data=filtered_data, x='Genre', y='Price')
    plt.xticks(rotation=45, ha='right')
    plt.title('Outlier Detection: Price Distribution by Genre (Top 10 Genres)')
    plt.tight_layout()
    plt.savefig('price_outliers.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("Plot saved as 'price_outliers.png'")

# --Part 4: Test Hypotheses & Validate Assumptions--

print("\n" + "="*60)
print("--- HYPOTHESIS TESTING ---")

# 1. The Tax Hypothesis: "Tax is always 0"
if 'Tax' in books_eda.columns:
    total_tax = books_eda['Tax'].sum()
    print(f"\nSum of all Tax values: {total_tax:.2f}")
    
    if total_tax == 0:
        print("Hypothesis Confirmed: This dataset is tax-free (or tax is not recorded).")
    else:
        print("Hypothesis Rejected: Some books have tax applied.")
else:
    print("\nNote: 'Tax' column not found in dataset.")

# 2. UPC Uniqueness: "Every book has a unique code"
if 'Upc' in books_eda.columns:
    is_unique = books_eda['Upc'].is_unique
    print(f"\nIs the 'Upc' column unique? {is_unique}")
    
    if not is_unique:
        duplicates = books_eda[books_eda.duplicated('Upc', keep=False)]
        print("Warning: Duplicate UPCs found:")
        print(duplicates[['Upc', 'Name']].head(10))
else:
    print("\nNote: 'Upc' column not found in dataset.")

# --Part 5: Detect Potential Data Issues--

print("\n" + "="*60)
print("--- DATA QUALITY ISSUES ---")

# 1. Information Gap: Is Review_Num empty?
if 'Review_Num' in books_eda.columns:
    missing_reviews = (books_eda['Review_Num'] == 0).all() or books_eda['Review_Num'].isnull().all()
    
    if missing_reviews:
        print("\nData Issue: 'Review_Num' column is entirely empty or zero. It provides no value.")
    else:
        books_with_reviews = books_eda[books_eda['Review_Num'] > 0].shape[0]
        print(f"\nData OK: There are {books_with_reviews} books with reviews.")
        print(f"Average reviews per book: {books_eda['Review_Num'].mean():.2f}")
else:
    print("\nNote: 'Review_Num' column not found in dataset.")

# 2. Stock Issues: Books with 0 stock
if 'Amount_Available' in books_eda.columns:
    zero_stock = books_eda[books_eda['Amount_Available'] == 0]
    print(f"\nNumber of books with 0 Amount_Available: {len(zero_stock)}")
    
    if len(zero_stock) > 0:
        print("Potential Issue: We have listed items that are out of stock.")
        print("\nSample out-of-stock books:")
        print(zero_stock[['Name', 'Price', 'Amount_Available']].head(3).to_string(index=False))
    else:
        print("Good: All books have stock available.")
else:
    print("\nNote: 'Amount_Available' column not found in dataset.")

# --Summary Statistics--
print("\n" + "="*60)
print("--- SUMMARY STATISTICS ---")
print("\nNumeric columns summary:")
print(books_eda.describe())

# Missing data summary
print("\n--- Missing Data Summary ---")
missing_data = books_eda.isnull().sum()
if missing_data.sum() > 0:
    print(missing_data[missing_data > 0])
else:
    print("No missing values detected!")

print("\n" + "="*60)
print("Analysis complete!")
print(f"\nTotal records analyzed: {len(books_eda)}")
print(f"Total columns: {len(books_eda.columns)}")