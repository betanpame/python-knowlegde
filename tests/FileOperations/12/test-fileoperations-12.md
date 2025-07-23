# File Security and Permissions - Test 12

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn to handle file security, permissions, and access control in Python applications.

## Objectives

- Implement secure file operations
- Manage file permissions properly
- Handle access control and user validation
- Protect sensitive file operations

## Your Tasks

1. **check_file_permissions()** - Verify read/write/execute permissions
2. **set_file_permissions()** - Modify file access permissions
3. **secure_file_operations()** - Implement safe file handling
4. **validate_file_paths()** - Prevent path traversal attacks
5. **encrypt_sensitive_files()** - Basic file encryption/decryption
6. **audit_file_access()** - Log file access for security
7. **implement_file_locking()** - Prevent concurrent file access
8. **sanitize_file_inputs()** - Clean and validate file inputs

## Example

```python
import os
import stat
import hashlib
import fcntl
from pathlib import Path
from typing import Optional, Dict
import logging

class SecureFileManager:
    """Secure file operations with proper validation and logging."""
    
    def __init__(self, base_directory: Path, log_file: Path = None):
        self.base_directory = Path(base_directory).resolve()
        self.logger = self._setup_logging(log_file)
    
    def _setup_logging(self, log_file: Optional[Path]) -> logging.Logger:
        """Set up security logging."""
        logger = logging.getLogger('secure_file_manager')
        logger.setLevel(logging.INFO)
        
        if log_file:
            handler = logging.FileHandler(log_file)
            formatter = logging.Formatter(
                '%(asctime)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def validate_path(self, file_path: str) -> Path:
        """Validate file path to prevent directory traversal."""
        
        # Convert to Path object and resolve
        path = Path(file_path).resolve()
        
        # Ensure path is within base directory
        try:
            path.relative_to(self.base_directory)
        except ValueError:
            raise ValueError(f"Path {path} is outside allowed directory")
        
        return path
    
    def secure_read_file(self, file_path: str, user_id: str = None) -> Optional[str]:
        """Securely read file with validation and logging."""
        
        try:
            validated_path = self.validate_path(file_path)
            
            # Check if file exists and is readable
            if not validated_path.exists():
                self.logger.warning(f"Attempted access to non-existent file: {file_path}")
                return None
            
            if not os.access(validated_path, os.R_OK):
                self.logger.warning(f"Insufficient permissions to read: {file_path}")
                return None
            
            # Log access
            self.logger.info(f"File read: {file_path} by user: {user_id}")
            
            with open(validated_path, 'r', encoding='utf-8') as file:
                return file.read()
                
        except Exception as e:
            self.logger.error(f"Error reading file {file_path}: {e}")
            return None
    
    def secure_write_file(self, 
                         file_path: str, 
                         content: str, 
                         user_id: str = None,
                         backup: bool = True) -> bool:
        """Securely write file with backup and validation."""
        
        try:
            validated_path = self.validate_path(file_path)
            
            # Create backup if file exists
            if backup and validated_path.exists():
                backup_path = validated_path.with_suffix(
                    validated_path.suffix + '.backup'
                )
                validated_path.rename(backup_path)
                self.logger.info(f"Created backup: {backup_path}")
            
            # Write with secure permissions
            with open(validated_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            # Set restrictive permissions (owner read/write only)
            os.chmod(validated_path, stat.S_IRUSR | stat.S_IWUSR)
            
            self.logger.info(f"File written: {file_path} by user: {user_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error writing file {file_path}: {e}")
            return False
    
    def get_file_hash(self, file_path: str) -> Optional[str]:
        """Calculate SHA-256 hash of file for integrity checking."""
        
        try:
            validated_path = self.validate_path(file_path)
            
            hasher = hashlib.sha256()
            with open(validated_path, 'rb') as file:
                for chunk in iter(lambda: file.read(4096), b""):
                    hasher.update(chunk)
            
            return hasher.hexdigest()
            
        except Exception as e:
            self.logger.error(f"Error calculating hash for {file_path}: {e}")
            return None

def set_secure_permissions(file_path: Path, owner_only: bool = True):
    """Set secure file permissions."""
    
    if owner_only:
        # Owner: read/write, Group/Other: no access
        permissions = stat.S_IRUSR | stat.S_IWUSR
    else:
        # Owner: read/write, Group/Other: read only
        permissions = stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH
    
    os.chmod(file_path, permissions)
```

## Hints

- Always validate file paths to prevent security vulnerabilities
- Use proper file permissions to protect sensitive data
- Implement logging for security auditing
- Consider using file locking for concurrent access

## Test Cases

Your security implementation should handle:
- Path traversal attack attempts
- Permission validation and enforcement
- Secure file creation and modification
- Audit logging of file operations

## Bonus Challenge

Create a complete file access control system with user authentication and role-based permissions!

Remember: Security should be built into file operations from the beginning!
