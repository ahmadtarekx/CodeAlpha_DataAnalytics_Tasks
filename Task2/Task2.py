import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#load data
books = pd.read_csv('E:/CodeAlpha_DataAnalytics_tasks/CodeAlpha_DataAnalytics_Tasks/Task1/books.csv')

#Data Cleaning

#know the colomn types
print(books.dtypes)

#update colomn headers to standard format
new_names = ['Genre', 'Name', 'price', 'status', 'upc', 'type', 'price_excl_tax', 'price incl tax', 'tax', 'review num']
standard_names = [name.title().replace(' ', '_') for name in new_names]
def rename_columns(df, new_names):

    # Check if the number of new column names matches the existing columns
    if len(df.columns) != len(new_names):
        print("\n--- ERROR: COLUMN COUNT MISMATCH ---")
        print(f"File has {len(df.columns)} columns.")
        print(f"You provided {len(new_names)} new column names.")
        print("Please ensure the 'NEW_COLUMN_NAMES' list matches the exact column count in your CSV.")
        return df # Return original df on error to avoid crashing
    
    df.columns = standard_names
    print(f"Columns renamed successfully.")
    return df

rename_columns(books, new_names)

#convert data types of colomns to appropriate types
def convert_column_types(df):

    print("\n--- converting column types ---")
    
    # 1. String Conversions
    str_cols = ['Genre', 'Name', 'status', 'upc', 'type']
    for col in str_cols:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    print("Converted string columns.")

    # 2. Float Conversions (Handling currency symbols like '£')
    float_cols = ['price', 'price_excl_tax', 'price incl tax', 'tax']
    for col in float_cols:
        if col in df.columns:
            # Remove '£' and ',' before converting to float
            # errors='coerce' turns non-convertible values into NaN
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace('£', '').str.replace(',', ''), 
                errors='coerce'
            )
    print("Converted float columns (currency symbols removed).")

    # 3. Integer Conversion
    int_col = 'review num'
    if int_col in df.columns:
        # Convert to numeric first (coercing errors), fill NaNs with 0, then cast to int
        df[int_col] = pd.to_numeric(df[int_col], errors='coerce').fillna(0).astype(int)
    print("Converted integer columns.")

    return df

convert_column_types(books)

#check for missing values in critical colomns and handle them(if in critical colomns remove the rows with null values)
exempt_columns = ['Upc','Type','Review_Num'] 
def handle_null_values(df, exempt_columns):

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
    # We want to check ALL columns EXCEPT the ones in the exempt list
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

handle_null_values(books, exempt_columns)



#clean Data Preview
print(books)
