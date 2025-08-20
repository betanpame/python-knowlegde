# File System Automation and Scripting - Practice 15

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn to create powerful automation scripts for file system operations and maintenance tasks.

## Objectives

- Build automated file management systems
- Create intelligent file organization scripts
- Implement file maintenance and cleanup automation
- Design configurable file processing workflows

## Your Tasks

1. **automated_file_organizer()** - Sort files by type, date, size automatically
2. **duplicate_file_finder()** - Find and manage duplicate files
3. **file_cleanup_scheduler()** - Automated cleanup of old/temporary files
4. **intelligent_backup_system()** - Smart backup with versioning
5. **file_synchronization_tool()** - Keep directories in sync
6. **batch_file_renamer()** - Rename files based on patterns
7. **content_based_organizer()** - Organize files by content analysis
8. **automated_file_reports()** - Generate file system reports

## Example

```python
import os
import shutil
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Set, Optional
import json
import re
from collections import defaultdict

class FileSystemAutomator:
    """Automated file system operations and maintenance."""
    
    def __init__(self, config_file: Path = None):
        self.config = self._load_config(config_file)
        self.operations_log = []
    
    def _load_config(self, config_file: Optional[Path]) -> Dict:
        """Load configuration from file or use defaults."""
        default_config = {
            'file_extensions': {
                'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'],
                'documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf'],
                'videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv'],
                'audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg'],
                'archives': ['.zip', '.rar', '.7z', '.tar', '.gz']
            },
            'cleanup_rules': {
                'temp_files_days': 7,
                'log_files_days': 30,
                'backup_retention_days': 90
            },
            'organization_rules': {
                'by_extension': True,
                'by_date': True,
                'by_size': False
            }
        }
        
        if config_file and config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    user_config = json.load(f)
                    default_config.update(user_config)
            except Exception as e:
                print(f"Error loading config: {e}, using defaults")
        
        return default_config
    
    def organize_files_by_type(self, source_dir: Path, target_dir: Path) -> Dict[str, int]:
        """Organize files into subdirectories by type."""
        
        if not source_dir.exists():
            raise ValueError(f"Source directory {source_dir} does not exist")
        
        target_dir.mkdir(parents=True, exist_ok=True)
        
        moved_files = defaultdict(int)
        file_types = self.config['file_extensions']
        
        for file_path in source_dir.rglob('*'):
            if file_path.is_file():
                # Determine file type
                file_extension = file_path.suffix.lower()
                file_type = 'other'
                
                for category, extensions in file_types.items():
                    if file_extension in extensions:
                        file_type = category
                        break
                
                # Create target directory
                type_dir = target_dir / file_type
                type_dir.mkdir(exist_ok=True)
                
                # Generate unique filename if conflict exists
                target_path = type_dir / file_path.name
                counter = 1
                while target_path.exists():
                    stem = file_path.stem
                    suffix = file_path.suffix
                    target_path = type_dir / f"{stem}_{counter}{suffix}"
                    counter += 1
                
                # Move file
                try:
                    shutil.move(str(file_path), str(target_path))
                    moved_files[file_type] += 1
                    self.operations_log.append({
                        'operation': 'move',
                        'source': str(file_path),
                        'target': str(target_path),
                        'timestamp': datetime.now().isoformat()
                    })
                except Exception as e:
                    print(f"Error moving {file_path}: {e}")
        
        return dict(moved_files)
    
    def find_duplicate_files(self, directory: Path) -> Dict[str, List[Path]]:
        """Find duplicate files based on content hash."""
        
        hash_to_files = defaultdict(list)
        
        for file_path in directory.rglob('*'):
            if file_path.is_file():
                try:
                    file_hash = self._calculate_file_hash(file_path)
                    hash_to_files[file_hash].append(file_path)
                except Exception as e:
                    print(f"Error hashing {file_path}: {e}")
        
        # Return only duplicates (groups with more than one file)
        duplicates = {
            hash_val: files for hash_val, files in hash_to_files.items()
            if len(files) > 1
        }
        
        return duplicates
    
    def cleanup_old_files(self, directory: Path, 
                         file_patterns: List[str], 
                         days_old: int) -> List[Path]:
        """Clean up files older than specified days."""
        
        cutoff_date = datetime.now() - timedelta(days=days_old)
        cleaned_files = []
        
        for pattern in file_patterns:
            for file_path in directory.rglob(pattern):
                if file_path.is_file():
                    # Check file modification time
                    mod_time = datetime.fromtimestamp(file_path.stat().st_mtime)
                    
                    if mod_time < cutoff_date:
                        try:
                            file_path.unlink()
                            cleaned_files.append(file_path)
                            self.operations_log.append({
                                'operation': 'delete',
                                'file': str(file_path),
                                'reason': f'older than {days_old} days',
                                'timestamp': datetime.now().isoformat()
                            })
                        except Exception as e:
                            print(f"Error deleting {file_path}: {e}")
        
        return cleaned_files
    
    def batch_rename_files(self, directory: Path, 
                          pattern: str, 
                          replacement: str,
                          dry_run: bool = True) -> List[Dict[str, str]]:
        """Batch rename files using regex patterns."""
        
        rename_operations = []
        
        for file_path in directory.iterdir():
            if file_path.is_file():
                old_name = file_path.name
                new_name = re.sub(pattern, replacement, old_name)
                
                if new_name != old_name:
                    new_path = file_path.parent / new_name
                    
                    # Check for conflicts
                    if new_path.exists():
                        print(f"Conflict: {new_path} already exists")
                        continue
                    
                    operation = {
                        'old_name': old_name,
                        'new_name': new_name,
                        'old_path': str(file_path),
                        'new_path': str(new_path)
                    }
                    
                    if not dry_run:
                        try:
                            file_path.rename(new_path)
                            operation['status'] = 'success'
                            self.operations_log.append({
                                'operation': 'rename',
                                'old_path': str(file_path),
                                'new_path': str(new_path),
                                'timestamp': datetime.now().isoformat()
                            })
                        except Exception as e:
                            operation['status'] = f'error: {e}'
                    else:
                        operation['status'] = 'dry_run'
                    
                    rename_operations.append(operation)
        
        return rename_operations
    
    def create_backup_with_versioning(self, source_dir: Path, 
                                    backup_dir: Path,
                                    max_versions: int = 5) -> Path:
        """Create versioned backup of directory."""
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_name = f"backup_{source_dir.name}_{timestamp}"
        backup_path = backup_dir / backup_name
        
        # Create backup
        try:
            shutil.copytree(source_dir, backup_path)
            
            # Clean up old backups
            self._cleanup_old_backups(backup_dir, source_dir.name, max_versions)
            
            self.operations_log.append({
                'operation': 'backup',
                'source': str(source_dir),
                'backup': str(backup_path),
                'timestamp': datetime.now().isoformat()
            })
            
            return backup_path
            
        except Exception as e:
            print(f"Error creating backup: {e}")
            raise
    
    def synchronize_directories(self, source_dir: Path, target_dir: Path,
                              delete_extra: bool = False) -> Dict[str, int]:
        """Synchronize two directories."""
        
        stats = {'copied': 0, 'updated': 0, 'deleted': 0, 'errors': 0}
        
        # Ensure target directory exists
        target_dir.mkdir(parents=True, exist_ok=True)
        
        # Copy/update files from source to target
        for source_file in source_dir.rglob('*'):
            if source_file.is_file():
                relative_path = source_file.relative_to(source_dir)
                target_file = target_dir / relative_path
                
                # Create target directory if needed
                target_file.parent.mkdir(parents=True, exist_ok=True)
                
                try:
                    if not target_file.exists():
                        shutil.copy2(source_file, target_file)
                        stats['copied'] += 1
                    elif source_file.stat().st_mtime > target_file.stat().st_mtime:
                        shutil.copy2(source_file, target_file)
                        stats['updated'] += 1
                except Exception as e:
                    print(f"Error syncing {source_file}: {e}")
                    stats['errors'] += 1
        
        # Delete extra files in target if requested
        if delete_extra:
            for target_file in target_dir.rglob('*'):
                if target_file.is_file():
                    relative_path = target_file.relative_to(target_dir)
                    source_file = source_dir / relative_path
                    
                    if not source_file.exists():
                        try:
                            target_file.unlink()
                            stats['deleted'] += 1
                        except Exception as e:
                            print(f"Error deleting {target_file}: {e}")
                            stats['errors'] += 1
        
        return stats
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file."""
        hasher = hashlib.sha256()
        
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)
        
        return hasher.hexdigest()
    
    def _cleanup_old_backups(self, backup_dir: Path, 
                           source_name: str, 
                           max_versions: int):
        """Clean up old backup versions."""
        
        # Find all backups for this source
        backup_pattern = f"backup_{source_name}_*"
        backups = list(backup_dir.glob(backup_pattern))
        
        # Sort by modification time (newest first)
        backups.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        
        # Remove excess backups
        for backup_path in backups[max_versions:]:
            try:
                shutil.rmtree(backup_path)
                self.operations_log.append({
                    'operation': 'cleanup_backup',
                    'path': str(backup_path),
                    'reason': f'exceeded max versions ({max_versions})',
                    'timestamp': datetime.now().isoformat()
                })
            except Exception as e:
                print(f"Error removing old backup {backup_path}: {e}")
    
    def generate_operations_report(self) -> Dict[str, any]:
        """Generate report of all operations performed."""
        
        operations_by_type = defaultdict(int)
        for operation in self.operations_log:
            operations_by_type[operation['operation']] += 1
        
        return {
            'total_operations': len(self.operations_log),
            'operations_by_type': dict(operations_by_type),
            'last_operation': self.operations_log[-1] if self.operations_log else None,
            'report_generated': datetime.now().isoformat()
        }
```

## Hints

- Use configuration files to make automation scripts flexible
- Implement dry-run modes for testing before actual operations
- Add comprehensive logging for audit trails
- Consider file locking for concurrent access scenarios

## Practice Cases

Your automation should handle:
- Large directories with thousands of files
- File conflicts and naming collisions
- Permission errors and access restrictions
- Configuration validation and error recovery

## Bonus Challenge

Create a complete file management system with a GUI that allows users to configure and schedule automated file operations!

Remember: Good automation saves time and reduces human error in repetitive tasks!