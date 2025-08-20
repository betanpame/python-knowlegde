# Data Cleaning and Preprocessing - Practice 3

**Difficulty:** ⭐ (Very Easy)

## Description

Learn essential data cleaning techniques including handling missing values, removing duplicates, and basic data type conversions. These are fundamental skills for any data science project.

## Objectives

- Identify and handle missing values
- Remove duplicate records
- Convert data types appropriately
- Clean string data and standardize formats
- Handle outliers in datasets

## Your Tasks

1. **handle_missing_values()** - Deal with NaN and missing data
2. **remove_duplicates()** - Identify and remove duplicate rows
3. **convert_data_types()** - Change column data types
4. **clean_string_data()** - Standardize text data
5. **handle_outliers()** - Detect and handle outliers

## Example

```python
import pandas as pd
import numpy as np

def handle_missing_values():
    """Learn to handle missing values in DataFrames."""
    
    # Create DataFrame with missing values
    data = {
        'Name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
        'Age': [25, np.nan, 35, 28, 32],
        'Salary': [50000, 60000, np.nan, 55000, None],
        'Department': ['Engineering', 'Marketing', 'Engineering', None, 'Marketing']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame with missing values:")
    print(df)
    print(f"\\nMissing values per column:\\n{df.isnull().sum()}")
    
    # Check for any missing values
    has_missing = df.isnull().any().any()
    print(f"\\nDataFrame has missing values: {has_missing}")
    
    # Drop rows with any missing values
    df_dropna = df.dropna()
    print(f"\\nAfter dropping rows with missing values:\\n{df_dropna}")
    
    # Drop columns with any missing values
    df_dropna_cols = df.dropna(axis=1)
    print(f"\\nAfter dropping columns with missing values:\\n{df_dropna_cols}")
    
    # Fill missing values with specific values
    df_filled = df.copy()
    df_filled['Name'] = df_filled['Name'].fillna('Unknown')
    df_filled['Age'] = df_filled['Age'].fillna(df_filled['Age'].mean())
    df_filled['Salary'] = df_filled['Salary'].fillna(df_filled['Salary'].median())
    df_filled['Department'] = df_filled['Department'].fillna('Unassigned')
    
    print(f"\\nAfter filling missing values:\\n{df_filled}")
    
    # Forward fill and backward fill
    df_ffill = df.fillna(method='ffill')
    print(f"\\nAfter forward fill:\\n{df_ffill}")
    
    return df, df_dropna, df_filled

def remove_duplicates():
    """Remove duplicate records from DataFrames."""
    
    # Create DataFrame with duplicates
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Diana', 'Bob', 'Eve'],
        'Age': [25, 30, 35, 25, 28, 30, 32],
        'Department': ['Engineering', 'Marketing', 'Engineering', 'Engineering', 'HR', 'Marketing', 'Marketing']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame with duplicates:")
    print(df)
    
    # Check for duplicates
    duplicates = df.duplicated()
    print(f"\\nDuplicate rows:\\n{df[duplicates]}")
    print(f"Number of duplicates: {duplicates.sum()}")
    
    # Remove duplicates (keep first occurrence)
    df_no_duplicates = df.drop_duplicates()
    print(f"\\nAfter removing duplicates (keep first):\\n{df_no_duplicates}")
    
    # Remove duplicates based on specific columns
    df_no_name_duplicates = df.drop_duplicates(subset=['Name'])
    print(f"\\nAfter removing name duplicates:\\n{df_no_name_duplicates}")
    
    # Keep last occurrence of duplicates
    df_keep_last = df.drop_duplicates(keep='last')
    print(f"\\nAfter removing duplicates (keep last):\\n{df_keep_last}")
    
    # Check specific columns for duplicates
    name_duplicates = df['Name'].duplicated()
    print(f"\\nDuplicate names: {name_duplicates.sum()}")
    
    return df, df_no_duplicates, df_no_name_duplicates

def convert_data_types():
    """Convert DataFrame column data types."""
    
    # Create DataFrame with mixed types
    data = {
        'ID': ['1', '2', '3', '4', '5'],
        'Price': ['10.50', '25.99', '15.75', '30.00', '8.25'],
        'Quantity': [10, 20, 15, 30, 5],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05'],
        'Is_Active': ['True', 'False', 'True', 'True', 'False']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame:")
    print(df)
    print(f"\\nOriginal data types:\\n{df.dtypes}")
    
    # Convert string to integer
    df['ID'] = df['ID'].astype(int)
    
    # Convert string to float
    df['Price'] = df['Price'].astype(float)
    
    # Convert string to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Convert string to boolean
    df['Is_Active'] = df['Is_Active'].astype(bool)
    
    print(f"\\nAfter type conversion:\\n{df}")
    print(f"\\nNew data types:\\n{df.dtypes}")
    
    # Convert with error handling
    data_with_errors = {
        'Numbers': ['1', '2', 'invalid', '4', '5.5']
    }
    df_errors = pd.DataFrame(data_with_errors)
    
    # Convert with errors='coerce' (invalid values become NaN)
    df_errors['Numbers_Clean'] = pd.to_numeric(df_errors['Numbers'], errors='coerce')
    print(f"\\nHandling conversion errors:\\n{df_errors}")
    
    return df, df_errors

def clean_string_data():
    """Clean and standardize string data."""
    
    # Create DataFrame with messy string data
    data = {
        'Name': ['  Alice Smith  ', 'BOB JONES', 'charlie brown', '  DIANA PRINCE'],
        'Email': ['ALICE@EXAMPLE.COM', 'bob@EXAMPLE.com  ', '  charlie@example.COM', 'diana@Example.Com'],
        'Phone': ['(555) 123-4567', '555.987.6543', '555-555-5555', '5551234567'],
        'Category': ['Category_A', 'category_b', 'CATEGORY_A', 'Category_C']
    }
    df = pd.DataFrame(data)
    
    print("Original DataFrame with messy strings:")
    print(df)
    
    # Clean names: strip whitespace and title case
    df['Name_Clean'] = df['Name'].str.strip().str.title()
    
    # Clean emails: strip whitespace and lowercase
    df['Email_Clean'] = df['Email'].str.strip().str.lower()
    
    # Clean phone numbers: remove special characters
    df['Phone_Clean'] = df['Phone'].str.replace(r'[^0-9]', '', regex=True)
    
    # Standardize categories: uppercase
    df['Category_Clean'] = df['Category'].str.upper()
    
    print(f"\\nAfter cleaning strings:")
    print(df[['Name_Clean', 'Email_Clean', 'Phone_Clean', 'Category_Clean']])
    
    # String operations examples
    print("\\nString operation examples:")
    
    # Check if string contains pattern
    contains_smith = df['Name_Clean'].str.contains('Smith')
    print(f"Names containing 'Smith': {df[contains_smith]['Name_Clean'].tolist()}")
    
    # Extract parts of strings
    first_names = df['Name_Clean'].str.split().str[0]
    print(f"First names: {first_names.tolist()}")
    
    # String length
    name_lengths = df['Name_Clean'].str.len()
    print(f"Name lengths: {name_lengths.tolist()}")
    
    return df, df[['Name_Clean', 'Email_Clean', 'Phone_Clean', 'Category_Clean']]

def handle_outliers():
    """Detect and handle outliers in data."""
    
    # Create data with outliers
    np.random.seed(42)
    normal_data = np.random.normal(100, 15, 95)
    outliers = [200, 250, 300, 50, 30]  # Add some outliers
    all_data = np.concatenate([normal_data, outliers])
    
    df = pd.DataFrame({
        'ID': range(1, len(all_data) + 1),
        'Value': all_data,
        'Category': np.random.choice(['A', 'B', 'C'], len(all_data))
    })
    
    print("DataFrame with outliers:")
    print(df.describe())
    
    # Detect outliers using IQR method
    Q1 = df['Value'].quantile(0.25)
    Q3 = df['Value'].quantile(0.75)
    IQR = Q3 - Q1
    
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    outliers_iqr = df[(df['Value'] < lower_bound) | (df['Value'] > upper_bound)]
    print(f"\\nOutliers detected using IQR method:")
    print(outliers_iqr)
    
    # Remove outliers
    df_no_outliers = df[(df['Value'] >= lower_bound) & (df['Value'] <= upper_bound)]
    print(f"\\nAfter removing outliers:")
    print(df_no_outliers.describe())
    
    # Cap outliers instead of removing
    df_capped = df.copy()
    df_capped['Value'] = np.where(df_capped['Value'] > upper_bound, upper_bound, df_capped['Value'])
    df_capped['Value'] = np.where(df_capped['Value'] < lower_bound, lower_bound, df_capped['Value'])
    
    print(f"\\nAfter capping outliers:")
    print(df_capped.describe())
    
    # Detect outliers using Z-score
    from scipy import stats
    z_scores = np.abs(stats.zscore(df['Value']))
    outliers_zscore = df[z_scores > 3]
    print(f"\\nOutliers using Z-score method (|z| > 3):")
    print(outliers_zscore)
    
    return df, df_no_outliers, outliers_iqr

# Practice all functions
if __name__ == "__main__":
    print("=== Data Cleaning and Preprocessing ===")
    
    print("\n1. Handling Missing Values:")
    missing_results = handle_missing_values()
    
    print("\n" + "="*50)
    print("2. Removing Duplicates:")
    duplicate_results = remove_duplicates()
    
    print("\n" + "="*50)
    print("3. Converting Data Types:")
    type_results = convert_data_types()
    
    print("\n" + "="*50)
    print("4. Cleaning String Data:")
    string_results = clean_string_data()
    
    print("\n" + "="*50)
    print("5. Handling Outliers:")
    outlier_results = handle_outliers()
    
    print("\n=== Data Cleaning Complete! ===")
```

## Hints

- Use `isnull()` and `notnull()` to identify missing values
- Use `fillna()` to replace missing values with specific values or statistics
- Use `drop_duplicates()` to remove duplicate rows
- Use `astype()` to convert data types, or `pd.to_numeric()` for numbers
- Use `.str` accessor for string operations on Series

## Practice Cases

Your functions should:

- Identify missing values and handle them appropriately
- Remove duplicate rows while preserving data integrity
- Convert string columns to appropriate numeric/datetime types
- Clean and standardize string data (trim whitespace, case conversion)
- Detect outliers using statistical methods (IQR, Z-score)

## Bonus Challenge

Create a comprehensive data cleaning pipeline that takes a messy dataset and returns a clean, analysis-ready DataFrame!