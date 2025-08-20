# Working with Pandas DataFrames - Practice 2

**Difficulty:** ⭐ (Very Easy)

## Description

Learn the basics of Pandas DataFrames, the fundamental data structure for data analysis in Python. Practice creating, reading, and basic manipulation of DataFrames.

## Objectives

- Create DataFrames from different data sources
- Access and select data from DataFrames
- Perform basic DataFrame operations
- Understand DataFrame attributes and info
- Export DataFrames to different formats

## Your Tasks

1. **create_dataframes()** - Create DataFrames from various sources
2. **dataframe_selection()** - Select rows, columns, and specific data
3. **basic_dataframe_operations()** - Add, modify, and delete columns
4. **dataframe_info()** - Explore DataFrame properties and statistics
5. **dataframe_export()** - Save DataFrames to files

## Example

```python
import pandas as pd
import numpy as np

def create_dataframes():
    """Create DataFrames from different data sources."""
    
    # Create DataFrame from dictionary
    data_dict = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age': [25, 30, 35, 28, 32],
        'City': ['New York', 'London', 'Tokyo', 'Paris', 'Sydney'],
        'Salary': [50000, 60000, 70000, 55000, 65000]
    }
    df_from_dict = pd.DataFrame(data_dict)
    print("DataFrame from dictionary:")
    print(df_from_dict)
    
    # Create DataFrame from list of lists
    data_list = [
        ['Product A', 100, 25.99],
        ['Product B', 150, 19.99],
        ['Product C', 200, 35.50],
        ['Product D', 75, 42.00]
    ]
    df_from_list = pd.DataFrame(data_list, columns=['Product', 'Quantity', 'Price'])
    print("\nDataFrame from list of lists:")
    print(df_from_list)
    
    # Create DataFrame with custom index
    dates = pd.date_range('2023-01-01', periods=5, freq='D')
    df_with_index = pd.DataFrame({
        'Temperature': [20, 22, 19, 25, 23],
        'Humidity': [60, 55, 70, 50, 65]
    }, index=dates)
    print("\nDataFrame with date index:")
    print(df_with_index)
    
    # Create empty DataFrame and add data
    df_empty = pd.DataFrame(columns=['A', 'B', 'C'])
    df_empty.loc[0] = [1, 2, 3]
    df_empty.loc[1] = [4, 5, 6]
    print("\nDataFrame built incrementally:")
    print(df_empty)
    
    return df_from_dict, df_from_list, df_with_index, df_empty

def dataframe_selection():
    """Practice selecting data from DataFrames."""
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank'],
        'Age': [25, 30, 35, 28, 32, 45],
        'Department': ['Engineering', 'Marketing', 'Engineering', 'HR', 'Marketing', 'Engineering'],
        'Salary': [75000, 60000, 85000, 55000, 65000, 95000],
        'Years_Experience': [3, 5, 8, 2, 6, 15]
    })
    
    print("Original DataFrame:")
    print(df)
    
    # Select single column
    names = df['Name']
    print(f"\nNames column:\n{names}")
    
    # Select multiple columns
    basic_info = df[['Name', 'Age', 'Department']]
    print(f"\nBasic info:\n{basic_info}")
    
    # Select rows by index
    first_three = df.iloc[:3]
    print(f"\nFirst three rows:\n{first_three}")
    
    # Select rows by condition
    engineering = df[df['Department'] == 'Engineering']
    print(f"\nEngineering employees:\n{engineering}")
    
    # Select with multiple conditions
    young_high_earners = df[(df['Age'] < 35) & (df['Salary'] > 70000)]
    print(f"\nYoung high earners:\n{young_high_earners}")
    
    # Select specific cell
    alice_salary = df.loc[df['Name'] == 'Alice', 'Salary'].iloc[0]
    print(f"\nAlice's salary: ${alice_salary}")
    
    return names, basic_info, engineering, young_high_earners

def basic_dataframe_operations():
    """Perform basic operations on DataFrames."""
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor'],
        'Price': [1200, 25, 80, 300],
        'Quantity': [10, 50, 30, 15]
    })
    
    print("Original DataFrame:")
    print(df)
    
    # Add new column
    df['Total_Value'] = df['Price'] * df['Quantity']
    print(f"\nAfter adding Total_Value column:\n{df}")
    
    # Modify existing column
    df['Price'] = df['Price'] * 1.1  # 10% price increase
    print(f"\nAfter 10% price increase:\n{df}")
    
    # Add new row
    new_product = pd.DataFrame({
        'Product': ['Headphones'],
        'Price': [150],
        'Quantity': [20],
        'Total_Value': [3000]
    })
    df = pd.concat([df, new_product], ignore_index=True)
    print(f"\nAfter adding new product:\n{df}")
    
    # Delete column
    df_without_total = df.drop('Total_Value', axis=1)
    print(f"\nAfter removing Total_Value column:\n{df_without_total}")
    
    # Delete row
    df_without_mouse = df.drop(1)  # Remove row with index 1 (Mouse)
    print(f"\nAfter removing Mouse row:\n{df_without_mouse}")
    
    # Rename columns
    df_renamed = df.rename(columns={'Product': 'Item_Name', 'Price': 'Unit_Price'})
    print(f"\nAfter renaming columns:\n{df_renamed}")
    
    return df, df_without_total, df_renamed

def dataframe_info():
    """Explore DataFrame properties and statistics."""
    
    # Create sample DataFrame with various data types
    np.random.seed(42)
    df = pd.DataFrame({
        'ID': range(1, 101),
        'Name': [f'Person_{i}' for i in range(1, 101)],
        'Age': np.random.randint(18, 65, 100),
        'Salary': np.random.normal(60000, 15000, 100),
        'Department': np.random.choice(['Engineering', 'Marketing', 'HR', 'Finance'], 100),
        'Is_Manager': np.random.choice([True, False], 100, p=[0.2, 0.8])
    })
    
    print("Sample DataFrame (first 10 rows):")
    print(df.head(10))
    
    # Basic info
    print(f"\nDataFrame shape: {df.shape}")
    print(f"Column names: {list(df.columns)}")
    print(f"Data types:\n{df.dtypes}")
    
    # Statistical summary
    print(f"\nStatistical summary:\n{df.describe()}")
    
    # Info about missing values
    print(f"\nMissing values:\n{df.isnull().sum()}")
    
    # Value counts for categorical data
    print(f"\nDepartment distribution:\n{df['Department'].value_counts()}")
    print(f"\nManager distribution:\n{df['Is_Manager'].value_counts()}")
    
    # Memory usage
    print(f"\nMemory usage:\n{df.memory_usage(deep=True)}")
    
    # Correlation matrix for numeric columns
    numeric_cols = df.select_dtypes(include=[np.number])
    print(f"\nCorrelation matrix:\n{numeric_cols.corr()}")
    
    return df.shape, df.dtypes, df.describe()

def dataframe_export():
    """Save DataFrames to different file formats."""
    
    # Create sample DataFrame
    df = pd.DataFrame({
        'Date': pd.date_range('2023-01-01', periods=10, freq='D'),
        'Sales': [1200, 1500, 1100, 1800, 1600, 1300, 1700, 1400, 1900, 1550],
        'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South'],
        'Product': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']
    })
    
    print("DataFrame to export:")
    print(df)
    
    # Save to CSV
    df.to_csv('sales_data.csv', index=False)
    print("\\nExported to CSV: sales_data.csv")
    
    # Save to Excel (requires openpyxl)
    try:
        df.to_excel('sales_data.xlsx', index=False, sheet_name='Sales')
        print("Exported to Excel: sales_data.xlsx")
    except ImportError:
        print("Excel export requires openpyxl package")
    
    # Save to JSON
    df.to_json('sales_data.json', orient='records', date_format='iso')
    print("Exported to JSON: sales_data.json")
    
    # Save specific columns only
    df[['Date', 'Sales']].to_csv('sales_summary.csv', index=False)
    print("Exported summary to CSV: sales_summary.csv")
    
    # Read back from CSV
    df_read = pd.read_csv('sales_data.csv')
    print(f"\\nRead back from CSV:")
    print(df_read.head())
    
    return df, df_read

# Practice all functions
if __name__ == "__main__":
    print("=== Working with Pandas DataFrames ===")
    
    print("\n1. Creating DataFrames:")
    dataframes = create_dataframes()
    
    print("\n" + "="*50)
    print("2. DataFrame Selection:")
    selection_results = dataframe_selection()
    
    print("\n" + "="*50)
    print("3. Basic DataFrame Operations:")
    operation_results = basic_dataframe_operations()
    
    print("\n" + "="*50)
    print("4. DataFrame Info and Statistics:")
    info_results = dataframe_info()
    
    print("\n" + "="*50)
    print("5. DataFrame Export/Import:")
    export_results = dataframe_export()
    
    print("\n=== Pandas DataFrames Complete! ===")
```

## Hints

- Use `pd.DataFrame()` to create DataFrames from dictionaries or lists
- Use square brackets `[]` for column selection and boolean indexing for row filtering
- Use `.loc[]` for label-based indexing and `.iloc[]` for position-based indexing
- Chain conditions with `&` (and) and `|` (or) operators
- Use `.head()` and `.tail()` to view the first/last few rows

## Practice Cases

Your functions should:

- Create DataFrames from dictionaries, lists, and with custom indices
- Select single columns, multiple columns, and filtered rows
- Add/modify/delete columns and rows successfully
- Display DataFrame info including shape, dtypes, and statistics
- Export DataFrames to CSV, JSON formats and read them back

## Bonus Challenge

Create a function that loads a CSV file, cleans the data (handles missing values), and generates a summary report!