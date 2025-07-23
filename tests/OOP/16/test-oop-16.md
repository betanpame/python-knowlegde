# Context Managers and Resource Management - Test 16

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Learn to create context managers using `__enter__` and `__exit__` methods or the `contextlib` module to properly manage resources like files, database connections, and locks.

## Objectives

- Implement `__enter__` and `__exit__` methods
- Create context managers using `@contextmanager` decorator
- Handle exceptions in context managers
- Build reusable resource management classes

## Your Tasks

1. **create_file_manager()** - Create custom file manager context
2. **implement_database_connection()** - Build database connection manager
3. **create_timing_context()** - Build performance timing context
4. **handle_exceptions()** - Properly handle exceptions in context managers

## Example

```python
import contextlib
import time
import threading
import tempfile
import os
import sqlite3
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileManager:
    """Context manager for safe file operations."""
    
    def __init__(self, filename, mode='r', encoding='utf-8', backup=False):
        """Initialize file manager."""
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.backup = backup
        self.file = None
        self.backup_file = None
        self.original_content = None
    
    def __enter__(self):
        """Enter context - open file and create backup if needed."""
        logging.info(f"Opening file: {self.filename} in mode: {self.mode}")
        
        # Create backup if writing and file exists
        if self.backup and 'w' in self.mode and os.path.exists(self.filename):
            self._create_backup()
        
        # Store original content for restoration on error
        if os.path.exists(self.filename) and 'w' in self.mode:
            try:
                with open(self.filename, 'r', encoding=self.encoding) as f:
                    self.original_content = f.read()
            except Exception as e:
                logging.warning(f"Could not read original content: {e}")
        
        try:
            self.file = open(self.filename, self.mode, encoding=self.encoding)
            return self.file
        except Exception as e:
            logging.error(f"Failed to open file {self.filename}: {e}")
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context - close file and handle errors."""
        if self.file:
            try:
                self.file.close()
                logging.info(f"Closed file: {self.filename}")
            except Exception as e:
                logging.error(f"Error closing file: {e}")
        
        # Handle exceptions that occurred in the with block
        if exc_type is not None:
            logging.error(f"Exception in file context: {exc_type.__name__}: {exc_value}")
            
            # If writing failed and we have original content, restore it
            if 'w' in self.mode and self.original_content is not None:
                try:
                    with open(self.filename, 'w', encoding=self.encoding) as f:
                        f.write(self.original_content)
                    logging.info(f"Restored original content to {self.filename}")
                except Exception as restore_error:
                    logging.error(f"Failed to restore original content: {restore_error}")
            
            # Return False to propagate the exception
            return False
        
        return True
    
    def _create_backup(self):
        """Create backup of the file."""
        backup_filename = f"{self.filename}.backup"
        try:
            import shutil
            shutil.copy2(self.filename, backup_filename)
            self.backup_file = backup_filename
            logging.info(f"Created backup: {backup_filename}")
        except Exception as e:
            logging.warning(f"Failed to create backup: {e}")

class DatabaseConnection:
    """Context manager for database connections with transaction support."""
    
    def __init__(self, database_path, auto_commit=True):
        """Initialize database connection manager."""
        self.database_path = database_path
        self.auto_commit = auto_commit
        self.connection = None
        self.transaction_active = False
    
    def __enter__(self):
        """Enter context - establish database connection."""
        try:
            self.connection = sqlite3.connect(self.database_path)
            self.connection.row_factory = sqlite3.Row  # Enable dict-like access
            
            if not self.auto_commit:
                # Start transaction
                self.connection.execute("BEGIN")
                self.transaction_active = True
            
            logging.info(f"Connected to database: {self.database_path}")
            return self.connection
        except Exception as e:
            logging.error(f"Failed to connect to database: {e}")
            raise
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context - handle transaction and close connection."""
        if self.connection:
            try:
                if exc_type is not None:
                    # Exception occurred - rollback if transaction is active
                    if self.transaction_active:
                        self.connection.rollback()
                        logging.info("Transaction rolled back due to exception")
                    logging.error(f"Database context exception: {exc_type.__name__}: {exc_value}")
                else:
                    # No exception - commit if transaction is active
                    if self.transaction_active:
                        self.connection.commit()
                        logging.info("Transaction committed successfully")
                    elif self.auto_commit:
                        self.connection.commit()
                
                self.connection.close()
                logging.info("Database connection closed")
            except Exception as e:
                logging.error(f"Error during database cleanup: {e}")
        
        # Return False to propagate any exception
        return False

class ThreadLock:
    """Context manager for thread synchronization."""
    
    def __init__(self, lock_name="unnamed"):
        """Initialize thread lock manager."""
        self.lock = threading.RLock()  # Reentrant lock
        self.lock_name = lock_name
        self.acquired = False
    
    def __enter__(self):
        """Enter context - acquire lock."""
        logging.info(f"Attempting to acquire lock: {self.lock_name}")
        self.acquired = self.lock.acquire(timeout=5.0)  # 5 second timeout
        
        if not self.acquired:
            raise TimeoutError(f"Failed to acquire lock '{self.lock_name}' within timeout")
        
        logging.info(f"Acquired lock: {self.lock_name}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Exit context - release lock."""
        if self.acquired:
            self.lock.release()
            logging.info(f"Released lock: {self.lock_name}")
        
        if exc_type is not None:
            logging.error(f"Exception in lock context: {exc_type.__name__}: {exc_value}")
        
        return False

# Context managers using @contextmanager decorator
@contextlib.contextmanager
def timer(operation_name="Operation"):
    """Context manager to time operations."""
    start_time = time.perf_counter()
    logging.info(f"Starting: {operation_name}")
    
    try:
        yield start_time
    except Exception as e:
        logging.error(f"Exception during {operation_name}: {e}")
        raise
    finally:
        end_time = time.perf_counter()
        duration = end_time - start_time
        logging.info(f"Completed: {operation_name} in {duration:.4f} seconds")

@contextlib.contextmanager
def temporary_directory(cleanup=True):
    """Context manager for temporary directory."""
    temp_dir = tempfile.mkdtemp()
    logging.info(f"Created temporary directory: {temp_dir}")
    
    try:
        yield Path(temp_dir)
    except Exception as e:
        logging.error(f"Exception in temporary directory: {e}")
        raise
    finally:
        if cleanup:
            try:
                import shutil
                shutil.rmtree(temp_dir)
                logging.info(f"Cleaned up temporary directory: {temp_dir}")
            except Exception as e:
                logging.warning(f"Failed to cleanup temporary directory: {e}")

@contextlib.contextmanager
def suppress_output():
    """Context manager to suppress stdout/stderr."""
    import sys
    from io import StringIO
    
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    
    try:
        sys.stdout = StringIO()
        sys.stderr = StringIO()
        yield
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

class ResourcePool:
    """Context manager for managing a pool of resources."""
    
    def __init__(self, resource_factory, pool_size=5):
        """Initialize resource pool."""
        self.resource_factory = resource_factory
        self.pool_size = pool_size
        self.available_resources = []
        self.in_use_resources = set()
        self.lock = threading.Lock()
        
        # Pre-populate the pool
        for _ in range(pool_size):
            resource = self.resource_factory()
            self.available_resources.append(resource)
    
    @contextlib.contextmanager
    def get_resource(self, timeout=5.0):
        """Get a resource from the pool."""
        resource = None
        start_time = time.time()
        
        while resource is None:
            with self.lock:
                if self.available_resources:
                    resource = self.available_resources.pop()
                    self.in_use_resources.add(resource)
                    break
            
            if time.time() - start_time > timeout:
                raise TimeoutError("No resources available in pool")
            
            time.sleep(0.1)
        
        logging.info(f"Acquired resource from pool: {id(resource)}")
        
        try:
            yield resource
        except Exception as e:
            logging.error(f"Exception with pooled resource: {e}")
            raise
        finally:
            with self.lock:
                if resource in self.in_use_resources:
                    self.in_use_resources.remove(resource)
                    self.available_resources.append(resource)
                    logging.info(f"Returned resource to pool: {id(resource)}")

# Example usage
def create_file_manager():
    """Demonstrate FileManager context manager."""
    print("=== FileManager Context Manager ===")
    
    test_file = "test_context.txt"
    
    # Test normal file operations
    print("1. Normal file write:")
    with FileManager(test_file, 'w', backup=True) as f:
        f.write("Hello, World!\n")
        f.write("This is a test file.\n")
    
    # Test file read
    print("2. Normal file read:")
    with FileManager(test_file, 'r') as f:
        content = f.read()
        print(f"Content: {content.strip()}")
    
    # Test exception handling
    print("3. Exception handling:")
    try:
        with FileManager(test_file, 'w', backup=True) as f:
            f.write("Starting to write...\n")
            raise ValueError("Simulated error!")
            f.write("This won't be written\n")
    except ValueError as e:
        print(f"Caught exception: {e}")
    
    # Check if file was restored
    with FileManager(test_file, 'r') as f:
        restored_content = f.read()
        print(f"Restored content: {restored_content.strip()}")
    
    # Cleanup
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(f"{test_file}.backup"):
        os.remove(f"{test_file}.backup")

def demonstrate_database_context():
    """Demonstrate DatabaseConnection context manager."""
    print("\n=== DatabaseConnection Context Manager ===")
    
    db_file = "test_context.db"
    
    # Test database operations
    print("1. Database setup and operations:")
    with DatabaseConnection(db_file, auto_commit=False) as conn:
        # Create table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT UNIQUE
            )
        """)
        
        # Insert data
        conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                    ("Alice", "alice@example.com"))
        conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                    ("Bob", "bob@example.com"))
    
    # Test transaction rollback
    print("2. Transaction rollback test:")
    try:
        with DatabaseConnection(db_file, auto_commit=False) as conn:
            conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                        ("Charlie", "charlie@example.com"))
            
            # This will cause a constraint violation
            conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", 
                        ("David", "alice@example.com"))  # Duplicate email
    except sqlite3.IntegrityError as e:
        print(f"Transaction rolled back due to: {e}")
    
    # Check final state
    print("3. Final database state:")
    with DatabaseConnection(db_file) as conn:
        cursor = conn.execute("SELECT * FROM users")
        for row in cursor.fetchall():
            print(f"  User: {row['name']} ({row['email']})")
    
    # Cleanup
    if os.path.exists(db_file):
        os.remove(db_file)

def test_timing_and_threading():
    """Test timing and threading context managers."""
    print("\n=== Timing and Threading Context Managers ===")
    
    # Test timer context
    print("1. Timing operations:")
    with timer("File I/O operation"):
        with temporary_directory() as temp_dir:
            test_file = temp_dir / "test.txt"
            with open(test_file, 'w') as f:
                for i in range(1000):
                    f.write(f"Line {i}\n")
            
            with open(test_file, 'r') as f:
                lines = f.readlines()
                print(f"   Read {len(lines)} lines")
    
    # Test thread lock
    print("2. Thread synchronization:")
    shared_resource = {'counter': 0}
    
    def worker(worker_id, iterations):
        with ThreadLock(f"worker_{worker_id}"):
            for _ in range(iterations):
                current = shared_resource['counter']
                time.sleep(0.001)  # Simulate work
                shared_resource['counter'] = current + 1
    
    threads = []
    for i in range(3):
        thread = threading.Thread(target=worker, args=(i, 10))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()
    
    print(f"   Final counter value: {shared_resource['counter']}")

def test_resource_pool():
    """Test resource pool context manager."""
    print("\n=== Resource Pool Context Manager ===")
    
    # Create a simple resource factory
    def create_connection():
        """Simulate creating a database connection."""
        return {"id": id(object()), "active": True}
    
    pool = ResourcePool(create_connection, pool_size=2)
    
    print("1. Using resources from pool:")
    
    def use_resource(user_id):
        try:
            with pool.get_resource(timeout=2.0) as resource:
                print(f"   User {user_id} got resource {resource['id']}")
                time.sleep(1)  # Simulate work
                print(f"   User {user_id} finished with resource {resource['id']}")
        except TimeoutError as e:
            print(f"   User {user_id} failed to get resource: {e}")
    
    # Test concurrent access
    threads = []
    for i in range(4):  # More users than pool size
        thread = threading.Thread(target=use_resource, args=(i,))
        threads.append(thread)
        thread.start()
    
    for thread in threads:
        thread.join()

# Test the implementation
if __name__ == "__main__":
    # Test file manager
    create_file_manager()
    
    # Test database context
    demonstrate_database_context()
    
    # Test timing and threading
    test_timing_and_threading()
    
    # Test resource pool
    test_resource_pool()
    
    # Test context manager suppression
    print("\n=== Output Suppression Test ===")
    print("Before suppression")
    
    with suppress_output():
        print("This will not be printed")
        print("Neither will this")
    
    print("After suppression")
    
    print("\n=== All Context Manager Tests Completed ===")
```

## Hints

- Always implement both `__enter__` and `__exit__` methods
- Return the resource from `__enter__` method
- Handle exceptions properly in `__exit__` method
- Return `False` from `__exit__` to propagate exceptions
- Use `@contextmanager` decorator for simpler implementations

## Test Cases

Your context managers should:

- Properly acquire and release resources
- Handle exceptions gracefully with cleanup
- Support nested context manager usage
- Provide meaningful error messages
- Work correctly with threading and concurrency

## Bonus Challenge

Create a `WebScrapingSession` context manager that handles HTTP sessions, rate limiting, and automatic retry logic with proper cleanup!
