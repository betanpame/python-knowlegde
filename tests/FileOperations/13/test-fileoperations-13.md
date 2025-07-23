# Database File Integration - Test 13

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn to work with database files and integrate file operations with database systems.

## Objectives

- Work with SQLite database files
- Import/export data between files and databases
- Handle database file operations safely
- Create efficient data pipelines

## Your Tasks

1. **create_sqlite_database()** - Create and initialize SQLite databases
2. **import_csv_to_database()** - Load CSV data into database tables
3. **export_database_to_files()** - Export database data to various formats
4. **backup_database_files()** - Create database backups safely
5. **migrate_data_between_formats()** - Convert between file and database formats
6. **validate_database_integrity()** - Check database file consistency
7. **batch_insert_from_files()** - Efficiently load large files into databases
8. **create_data_synchronization()** - Keep files and databases in sync

## Example

```python
import sqlite3
import csv
import json
from pathlib import Path
from typing import List, Dict, Any, Optional
import shutil
from datetime import datetime

class DatabaseFileManager:
    """Manage integration between database files and other formats."""
    
    def __init__(self, db_path: Path):
        self.db_path = Path(db_path)
        self.connection: Optional[sqlite3.Connection] = None
    
    def __enter__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.connection.row_factory = sqlite3.Row  # Enable column access by name
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.close()
    
    def create_table_from_csv_structure(self, csv_path: Path, table_name: str) -> bool:
        """Create database table based on CSV file structure."""
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                headers = next(reader)
                
                # Sample first few rows to infer data types
                sample_rows = []
                for i, row in enumerate(reader):
                    if i >= 10:  # Sample first 10 rows
                        break
                    sample_rows.append(row)
            
            # Infer column types
            columns = []
            for i, header in enumerate(headers):
                # Simple type inference
                column_type = "TEXT"  # Default
                
                if sample_rows:
                    sample_values = [row[i] for row in sample_rows if i < len(row)]
                    
                    # Check if all values are integers
                    if all(self._is_integer(val) for val in sample_values if val):
                        column_type = "INTEGER"
                    # Check if all values are floats
                    elif all(self._is_float(val) for val in sample_values if val):
                        column_type = "REAL"
                
                columns.append(f'"{header}" {column_type}')
            
            # Create table
            create_sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({", ".join(columns)})'
            self.connection.execute(create_sql)
            self.connection.commit()
            
            return True
            
        except Exception as e:
            print(f"Error creating table: {e}")
            return False
    
    def import_csv_to_table(self, csv_path: Path, table_name: str, batch_size: int = 1000) -> int:
        """Import CSV data into database table in batches."""
        
        try:
            with open(csv_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                
                # Get column names
                columns = reader.fieldnames
                placeholders = ', '.join(['?' for _ in columns])
                insert_sql = f'INSERT INTO "{table_name}" ({", ".join(f\'"{col}"\' for col in columns)}) VALUES ({placeholders})'
                
                batch = []
                total_inserted = 0
                
                for row in reader:
                    # Convert row dict to tuple in correct order
                    values = tuple(row[col] for col in columns)
                    batch.append(values)
                    
                    if len(batch) >= batch_size:
                        self.connection.executemany(insert_sql, batch)
                        self.connection.commit()
                        total_inserted += len(batch)
                        batch = []
                
                # Insert remaining rows
                if batch:
                    self.connection.executemany(insert_sql, batch)
                    self.connection.commit()
                    total_inserted += len(batch)
                
                return total_inserted
                
        except Exception as e:
            print(f"Error importing CSV: {e}")
            return 0
    
    def export_table_to_csv(self, table_name: str, output_path: Path) -> bool:
        """Export database table to CSV file."""
        
        try:
            cursor = self.connection.execute(f'SELECT * FROM "{table_name}"')
            
            # Get column names
            columns = [description[0] for description in cursor.description]
            
            with open(output_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                
                # Write header
                writer.writerow(columns)
                
                # Write data
                while True:
                    rows = cursor.fetchmany(1000)  # Process in batches
                    if not rows:
                        break
                    writer.writerows(rows)
            
            return True
            
        except Exception as e:
            print(f"Error exporting to CSV: {e}")
            return False
    
    def export_table_to_json(self, table_name: str, output_path: Path) -> bool:
        """Export database table to JSON file."""
        
        try:
            cursor = self.connection.execute(f'SELECT * FROM "{table_name}"')
            
            # Convert rows to dictionaries
            data = []
            for row in cursor:
                data.append(dict(row))
            
            with open(output_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, default=str)
            
            return True
            
        except Exception as e:
            print(f"Error exporting to JSON: {e}")
            return False
    
    def backup_database(self, backup_path: Path) -> bool:
        """Create a backup of the database file."""
        
        try:
            # Close current connection
            if self.connection:
                self.connection.close()
            
            # Copy database file
            shutil.copy2(self.db_path, backup_path)
            
            # Reopen connection
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
            
            return True
            
        except Exception as e:
            print(f"Error creating backup: {e}")
            return False
    
    def _is_integer(self, value: str) -> bool:
        """Check if string represents an integer."""
        try:
            int(value)
            return True
        except ValueError:
            return False
    
    def _is_float(self, value: str) -> bool:
        """Check if string represents a float."""
        try:
            float(value)
            return True
        except ValueError:
            return False
```

## Hints

- Use transactions for batch operations to improve performance
- Implement proper error handling for database operations
- Consider data types when creating tables from files
- Use connection context managers for safe database access

## Test Cases

Your database integration should handle:
- Large CSV files with efficient batch processing
- Various data types and formats
- Database backup and restore operations
- Data validation and integrity checks

## Bonus Challenge

Create a complete ETL (Extract, Transform, Load) pipeline that can process multiple file formats and load them into databases with automatic schema detection!

Remember: Database operations require careful transaction management and error handling!
