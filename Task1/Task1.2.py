import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
books = pd.read_csv('E:/CodeAlpha_DataAnalytics_tasks/CodeAlpha_DataAnalytics_Tasks/Task1/books.csv')

# Data Cleaning

# Know the column types
print(books.dtypes)

# Update column headers to standard format
new_names = ['Genre', 'Name', 'price', 'status', 'upc', 'type', 'price_excl_tax', 'price_incl_tax', 'tax', 'review_num']
standard_names = [name.title().replace(' ', '_') for name in new_names]

def rename_columns(df, new_names):
    """Rename columns to standardized format"""
    # Check if the number of new column names matches the existing columns
    if len(df.columns) != len(new_names):
        print("\n--- ERROR: COLUMN COUNT MISMATCH ---")
        print(f"File has {len(df.columns)} columns.")
        print(f"You provided {len(new_names)} new column names.")
        print("Please ensure the 'new_names' list matches the exact column count in your CSV.")
        return df  # Return original df on error to avoid crashing
    
    df.columns = standard_names
    print(f"\nColumns renamed successfully.")
    return df

# IMPORTANT: Assign the result back to books
books = rename_columns(books, new_names)

# Convert data types of columns to appropriate types
def convert_column_types(df):
    """Convert columns to appropriate data types"""
    print("\n--- Converting column types ---")
    
    # 1. String Conversions
    str_cols = ['Genre', 'Name', 'Status', 'Upc', 'Type']
    for col in str_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    print("Converted string columns.")

    # 2. Float Conversions (Handling ANY currency symbols)
    float_cols = ['Price', 'Price_Excl_Tax', 'Price_Incl_Tax', 'Tax']
    for col in float_cols:
        if col in df.columns:
            # Use regex to replace anything that is NOT a digit or a dot with empty string
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(r'[^\d.]', '', regex=True), 
                errors='coerce'
            )
    print("Converted float columns (currency symbols removed via regex).")

    # 3. Integer Conversion
    int_col = 'Review_Num'
    if int_col in df.columns:
        # Convert to numeric first (coercing errors), fill NaNs with 0, then cast to int
        df[int_col] = pd.to_numeric(df[int_col], errors='coerce').fillna(0).astype(int)
    print("Converted integer columns.")

    return df

# IMPORTANT: Assign the result back to books
books = convert_column_types(books)


#after consideration i found that converting Status to Amount_Available would be more useful
#so i created a function to do that and display only the integer values
def convert_status_to_amount(df):
    """Convert 'Status' column to 'Amount_Available' with integer values"""
    print("\n--- Converting Status to Amount_Available ---")
    
    if 'Status' not in df.columns:
        print("Warning: Column 'Status' not found.")
        return df
    
    # Extract numbers from status column
    # This will extract any digits from strings like "In stock (19 available)"
    df['Amount_Available'] = df['Status'].astype(str).str.extract(r'(\d+)', expand=False)
    
    # Convert to integer, filling any NaN values with 0
    df['Amount_Available'] = pd.to_numeric(df['Amount_Available'], errors='coerce').fillna(0).astype(int)
    
    # Drop the original Status column
    df = df.drop('Status', axis=1)
    
    print(f"Successfully converted Status to Amount_Available.")
    print(f"Sample values: {df['Amount_Available'].head().tolist()}")
    
    return df


books = convert_status_to_amount(books)

# Check for missing values in critical columns and handle them
exempt_columns = ['Upc', 'Type', 'Review_Num'] 

def handle_null_values(df, exempt_columns=None):
    """Remove rows with null values in non-exempt columns"""
    if exempt_columns is None:
        exempt_columns = []
        
    print("\n--- Null Value Check ---")
    
    # 1. Report counts
    null_counts = df.isnull().sum()
    if null_counts.sum() == 0:
        print("No null values found in the dataset.")
        return df
        
    print("Null values found per column:")
    print(null_counts[null_counts > 0])
    
    # 2. Determine which columns to check for dropping rows
    cols_to_check = [col for col in df.columns if col not in exempt_columns]
    
    if not cols_to_check:
        print("All columns are exempt. No rows will be dropped.")
        return df
        
    # 3. Drop rows
    initial_rows = len(df)
    df_cleaned = df.dropna(subset=cols_to_check)
    rows_removed = initial_rows - len(df_cleaned)
    
    print(f"Dropping rows based on nulls in columns: {cols_to_check}")
    print(f"Removed {rows_removed} rows containing null values.")
    print(f"Remaining rows: {len(df_cleaned)}")
    
    return df_cleaned

# IMPORTANT: Assign the result back to books
books = handle_null_values(books, exempt_columns)

# Remove rows where Name is 'next' (from web scraping artifacts)
def remove_next_rows(df):
    """Remove rows where 'Name' column contains 'next'"""
    print("\n--- Filtering 'next' rows ---")
    if 'Name' not in df.columns:
        print("Warning: Column 'Name' not found.")
        return df

    initial_rows = len(df)
    # Filter out rows where Name is 'next'
    df = df[df['Name'].astype(str).str.strip().str.lower() != 'next']
    
    rows_removed = initial_rows - len(df)
    print(f"Removed {rows_removed} rows where Name was 'next'.")
    return df

# IMPORTANT: Assign the result back to books
books = remove_next_rows(books)

# Save cleaned data to new csv file
def save_data(df, output_path):
    """Save dataframe to CSV file"""
    try:
        df.to_csv(output_path, index=False)
        print(f"\nSuccessfully saved cleaned data to '{output_path}'.")
        print(f"Final dataset shape: {df.shape}")
    except Exception as e:
        print(f"Error saving data: {e}")

save_data(books, 'E:/CodeAlpha_DataAnalytics_tasks/CodeAlpha_DataAnalytics_Tasks/Task1/cleaned_books.csv')

# Load and display cleaned data
print("\n--- Cleaned Data Preview ---")
cleaned_books = pd.read_csv('E:/CodeAlpha_DataAnalytics_tasks/CodeAlpha_DataAnalytics_Tasks/Task1/cleaned_books.csv')
print(cleaned_books)
print(f"\nDataset info:")
print(cleaned_books.info())