# Enterprise File Management System - Practice 16

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Design and implement an enterprise-grade file management system with advanced features like metadata management, versioning, access control, and audit trails.

## Objectives

- Build scalable file storage architecture
- Implement comprehensive metadata management
- Create advanced versioning and revision control
- Design enterprise security and audit systems

## Your Tasks

1. **metadata_management_system()** - Store and query file metadata
2. **version_control_for_files()** - Track file versions and changes
3. **access_control_matrix()** - Role-based file access permissions
4. **audit_trail_system()** - Complete file operation logging
5. **distributed_file_storage()** - Scale across multiple storage backends
6. **file_lifecycle_management()** - Automated archival and retention
7. **search_and_indexing_engine()** - Fast content and metadata search
8. **disaster_recovery_system()** - Backup and recovery automation

## Example

```python
import sqlite3
import json
import hashlib
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Set
from dataclasses import dataclass, asdict
from enum import Enum
import uuid
import shutil
import threading
from contextlib import contextmanager
import logging

class FileStatus(Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DELETED = "deleted"
    QUARANTINED = "quarantined"

class AccessLevel(Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"

@dataclass
class FileMetadata:
    """Complete file metadata structure."""
    file_id: str
    original_name: str
    storage_path: str
    content_hash: str
    size_bytes: int
    mime_type: str
    created_at: datetime
    modified_at: datetime
    created_by: str
    version: int
    status: FileStatus
    tags: List[str]
    custom_metadata: Dict[str, Any]
    parent_version: Optional[str] = None

@dataclass
class AccessPermission:
    """File access permission structure."""
    user_id: str
    role: str
    access_levels: Set[AccessLevel]
    granted_at: datetime
    granted_by: str
    expires_at: Optional[datetime] = None

class EnterpriseFileManager:
    """Enterprise-grade file management system."""
    
    def __init__(self, 
                 storage_root: Path,
                 db_path: Path,
                 index_path: Path = None):
        self.storage_root = Path(storage_root)
        self.db_path = Path(db_path)
        self.index_path = Path(index_path) if index_path else self.storage_root / "index"
        
        # Create directories
        self.storage_root.mkdir(parents=True, exist_ok=True)
        self.index_path.mkdir(parents=True, exist_ok=True)
        
        # Initialize database
        self._initialize_database()
        
        # Setup logging
        self.logger = self._setup_logging()
        
        # Thread safety
        self._lock = threading.RLock()
    
    def _initialize_database(self):
        """Initialize the metadata database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript('''
                CREATE TABLE IF NOT EXISTS files (
                    file_id TEXT PRIMARY KEY,
                    original_name TEXT NOT NULL,
                    storage_path TEXT NOT NULL,
                    content_hash TEXT NOT NULL,
                    size_bytes INTEGER NOT NULL,
                    mime_type TEXT,
                    created_at TIMESTAMP NOT NULL,
                    modified_at TIMESTAMP NOT NULL,
                    created_by TEXT NOT NULL,
                    version INTEGER NOT NULL,
                    status TEXT NOT NULL,
                    tags TEXT,
                    custom_metadata TEXT,
                    parent_version TEXT,
                    FOREIGN KEY (parent_version) REFERENCES files (file_id)
                );
                
                CREATE TABLE IF NOT EXISTS access_permissions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    file_id TEXT NOT NULL,
                    user_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    access_levels TEXT NOT NULL,
                    granted_at TIMESTAMP NOT NULL,
                    granted_by TEXT NOT NULL,
                    expires_at TIMESTAMP,
                    FOREIGN KEY (file_id) REFERENCES files (file_id)
                );
                
                CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TIMESTAMP NOT NULL,
                    user_id TEXT NOT NULL,
                    operation TEXT NOT NULL,
                    file_id TEXT,
                    details TEXT,
                    ip_address TEXT,
                    user_agent TEXT
                );
                
                CREATE INDEX IF NOT EXISTS idx_files_hash ON files (content_hash);
                CREATE INDEX IF NOT EXISTS idx_files_status ON files (status);
                CREATE INDEX IF NOT EXISTS idx_files_created_by ON files (created_by);
                CREATE INDEX IF NOT EXISTS idx_audit_timestamp ON audit_log (timestamp);
                CREATE INDEX IF NOT EXISTS idx_audit_user ON audit_log (user_id);
            ''')
    
    def _setup_logging(self) -> logging.Logger:
        """Setup enterprise logging."""
        logger = logging.getLogger('enterprise_file_manager')
        logger.setLevel(logging.INFO)
        
        # File handler
        log_file = self.storage_root / 'system.log'
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(logging.INFO)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        return logger
    
    @contextmanager
    def _db_connection(self):
        """Thread-safe database connection."""
        with self._lock:
            conn = sqlite3.connect(self.db_path)
            conn.row_factory = sqlite3.Row
            try:
                yield conn
            finally:
                conn.close()
    
    def store_file(self, 
                   file_path: Path,
                   original_name: str,
                   user_id: str,
                   tags: List[str] = None,
                   custom_metadata: Dict[str, Any] = None) -> str:
        """Store file with complete metadata management."""
        
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} does not exist")
        
        # Generate unique file ID
        file_id = str(uuid.uuid4())
        
        # Calculate content hash
        content_hash = self._calculate_file_hash(file_path)
        
        # Check for duplicates
        existing_file = self._find_file_by_hash(content_hash)
        if existing_file:
            self.logger.info(f"Duplicate file detected: {content_hash}")
            # Could implement deduplication logic here
        
        # Determine storage path
        storage_subdir = self.storage_root / content_hash[:2] / content_hash[2:4]
        storage_subdir.mkdir(parents=True, exist_ok=True)
        storage_path = storage_subdir / f"{file_id}_{original_name}"
        
        # Copy file to storage
        shutil.copy2(file_path, storage_path)
        
        # Create metadata
        metadata = FileMetadata(
            file_id=file_id,
            original_name=original_name,
            storage_path=str(storage_path),
            content_hash=content_hash,
            size_bytes=file_path.stat().st_size,
            mime_type=self._detect_mime_type(file_path),
            created_at=datetime.now(),
            modified_at=datetime.now(),
            created_by=user_id,
            version=1,
            status=FileStatus.ACTIVE,
            tags=tags or [],
            custom_metadata=custom_metadata or {}
        )
        
        # Store metadata
        self._store_metadata(metadata)
        
        # Log operation
        self._log_operation(user_id, 'store_file', file_id, {
            'original_name': original_name,
            'size': metadata.size_bytes,
            'hash': content_hash
        })
        
        self.logger.info(f"File stored: {file_id} by {user_id}")
        return file_id
    
    def create_file_version(self,
                           file_id: str,
                           new_file_path: Path,
                           user_id: str,
                           version_notes: str = None) -> str:
        """Create new version of existing file."""
        
        # Get current file metadata
        current_metadata = self._get_metadata(file_id)
        if not current_metadata:
            raise ValueError(f"File {file_id} not found")
        
        # Check permissions
        if not self._check_permission(file_id, user_id, AccessLevel.WRITE):
            raise PermissionError(f"User {user_id} lacks write permission for {file_id}")
        
        # Generate new version ID
        new_version_id = str(uuid.uuid4())
        
        # Calculate new content hash
        new_content_hash = self._calculate_file_hash(new_file_path)
        
        # Create storage path for new version
        storage_subdir = self.storage_root / new_content_hash[:2] / new_content_hash[2:4]
        storage_subdir.mkdir(parents=True, exist_ok=True)
        new_storage_path = storage_subdir / f"{new_version_id}_{current_metadata['original_name']}"
        
        # Copy new file version
        shutil.copy2(new_file_path, new_storage_path)
        
        # Create new version metadata
        new_metadata = FileMetadata(
            file_id=new_version_id,
            original_name=current_metadata['original_name'],
            storage_path=str(new_storage_path),
            content_hash=new_content_hash,
            size_bytes=new_file_path.stat().st_size,
            mime_type=self._detect_mime_type(new_file_path),
            created_at=datetime.fromisoformat(current_metadata['created_at']),
            modified_at=datetime.now(),
            created_by=current_metadata['created_by'],
            version=current_metadata['version'] + 1,
            status=FileStatus.ACTIVE,
            tags=json.loads(current_metadata['tags']) if current_metadata['tags'] else [],
            custom_metadata=json.loads(current_metadata['custom_metadata']) if current_metadata['custom_metadata'] else {},
            parent_version=file_id
        )
        
        # Store new version metadata
        self._store_metadata(new_metadata)
        
        # Update original file status to indicate it has newer version
        with self._db_connection() as conn:
            conn.execute(
                'UPDATE files SET status = ? WHERE file_id = ?',
                (FileStatus.ARCHIVED.value, file_id)
            )
            conn.commit()
        
        # Log operation
        self._log_operation(user_id, 'create_version', new_version_id, {
            'parent_version': file_id,
            'version_notes': version_notes,
            'new_hash': new_content_hash
        })
        
        return new_version_id
    
    def grant_permission(self,
                        file_id: str,
                        target_user_id: str,
                        role: str,
                        access_levels: Set[AccessLevel],
                        granted_by: str,
                        expires_at: Optional[datetime] = None):
        """Grant access permission to user for file."""
        
        # Check if granter has admin permission
        if not self._check_permission(file_id, granted_by, AccessLevel.ADMIN):
            raise PermissionError(f"User {granted_by} lacks admin permission for {file_id}")
        
        permission = AccessPermission(
            user_id=target_user_id,
            role=role,
            access_levels=access_levels,
            granted_at=datetime.now(),
            granted_by=granted_by,
            expires_at=expires_at
        )
        
        with self._db_connection() as conn:
            conn.execute('''
                INSERT INTO access_permissions 
                (file_id, user_id, role, access_levels, granted_at, granted_by, expires_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                file_id,
                permission.user_id,
                permission.role,
                json.dumps([level.value for level in permission.access_levels]),
                permission.granted_at,
                permission.granted_by,
                permission.expires_at
            ))
            conn.commit()
        
        # Log operation
        self._log_operation(granted_by, 'grant_permission', file_id, {
            'target_user': target_user_id,
            'role': role,
            'access_levels': [level.value for level in access_levels]
        })
    
    def search_files(self,
                    query: str = None,
                    tags: List[str] = None,
                    user_id: str = None,
                    status: FileStatus = None,
                    created_after: datetime = None,
                    created_before: datetime = None) -> List[Dict[str, Any]]:
        """Advanced file search with multiple criteria."""
        
        with self._db_connection() as conn:
            sql_parts = ['SELECT * FROM files WHERE 1=1']
            params = []
            
            if query:
                sql_parts.append('AND (original_name LIKE ? OR custom_metadata LIKE ?)')
                params.extend([f'%{query}%', f'%{query}%'])
            
            if tags:
                for tag in tags:
                    sql_parts.append('AND tags LIKE ?')
                    params.append(f'%{tag}%')
            
            if user_id:
                sql_parts.append('AND created_by = ?')
                params.append(user_id)
            
            if status:
                sql_parts.append('AND status = ?')
                params.append(status.value)
            
            if created_after:
                sql_parts.append('AND created_at >= ?')
                params.append(created_after)
            
            if created_before:
                sql_parts.append('AND created_at <= ?')
                params.append(created_before)
            
            sql_parts.append('ORDER BY modified_at DESC')
            
            cursor = conn.execute(' '.join(sql_parts), params)
            return [dict(row) for row in cursor.fetchall()]
    
    def _calculate_file_hash(self, file_path: Path) -> str:
        """Calculate SHA-256 hash of file."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def _detect_mime_type(self, file_path: Path) -> str:
        """Detect MIME type of file."""
        import mimetypes
        mime_type, _ = mimetypes.guess_type(str(file_path))
        return mime_type or 'application/octet-stream'
    
    def _store_metadata(self, metadata: FileMetadata):
        """Store file metadata in database."""
        with self._db_connection() as conn:
            conn.execute('''
                INSERT INTO files 
                (file_id, original_name, storage_path, content_hash, size_bytes,
                 mime_type, created_at, modified_at, created_by, version, status,
                 tags, custom_metadata, parent_version)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                metadata.file_id,
                metadata.original_name,
                metadata.storage_path,
                metadata.content_hash,
                metadata.size_bytes,
                metadata.mime_type,
                metadata.created_at,
                metadata.modified_at,
                metadata.created_by,
                metadata.version,
                metadata.status.value,
                json.dumps(metadata.tags),
                json.dumps(metadata.custom_metadata),
                metadata.parent_version
            ))
            conn.commit()
    
    def _get_metadata(self, file_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve file metadata."""
        with self._db_connection() as conn:
            cursor = conn.execute('SELECT * FROM files WHERE file_id = ?', (file_id,))
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def _find_file_by_hash(self, content_hash: str) -> Optional[Dict[str, Any]]:
        """Find file by content hash."""
        with self._db_connection() as conn:
            cursor = conn.execute(
                'SELECT * FROM files WHERE content_hash = ? AND status = ?',
                (content_hash, FileStatus.ACTIVE.value)
            )
            row = cursor.fetchone()
            return dict(row) if row else None
    
    def _check_permission(self, file_id: str, user_id: str, required_level: AccessLevel) -> bool:
        """Check if user has required permission for file."""
        with self._db_connection() as conn:
            cursor = conn.execute('''
                SELECT access_levels, expires_at FROM access_permissions 
                WHERE file_id = ? AND user_id = ? AND (expires_at IS NULL OR expires_at > ?)
            ''', (file_id, user_id, datetime.now()))
            
            for row in cursor:
                access_levels = json.loads(row['access_levels'])
                if required_level.value in access_levels:
                    return True
            
            return False
    
    def _log_operation(self, user_id: str, operation: str, file_id: str = None, details: Dict = None):
        """Log operation to audit trail."""
        with self._db_connection() as conn:
            conn.execute('''
                INSERT INTO audit_log (timestamp, user_id, operation, file_id, details)
                VALUES (?, ?, ?, ?, ?)
            ''', (
                datetime.now(),
                user_id,
                operation,
                file_id,
                json.dumps(details) if details else None
            ))
            conn.commit()
```

## Hints

- Design database schema for scalability and performance
- Implement proper indexing for fast searches
- Use transactions for data consistency
- Consider implementing caching for frequently accessed metadata

## Practice Cases

Your enterprise system should handle:
- High-volume file operations with concurrent users
- Complex permission scenarios and access control
- Large-scale search and indexing operations
- Data integrity and consistency requirements

## Bonus Challenge

Create a complete enterprise file management platform with web interface, REST API, and microservices architecture!

Remember: Enterprise systems require robust architecture, security, and scalability!