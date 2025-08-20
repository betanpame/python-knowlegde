# Cloud Storage Integration and Synchronization - Practice 18

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

## Description

Build a comprehensive cloud storage integration system that can synchronize files across multiple cloud providers with conflict resolution, encryption, and intelligent sync strategies.

## Objectives

- Implement multi-cloud storage integration
- Create intelligent synchronization algorithms
- Build conflict resolution systems
- Design secure cloud data handling

## Your Tasks

1. **multi_cloud_storage_adapter()** - Support multiple cloud providers
2. **intelligent_sync_engine()** - Smart bidirectional synchronization
3. **conflict_resolution_system()** - Handle sync conflicts automatically
4. **encrypted_cloud_storage()** - Secure data in transit and at rest
5. **bandwidth_optimization()** - Optimize data transfer efficiency
6. **cloud_backup_orchestration()** - Automated cloud backup strategies
7. **cross_cloud_migration()** - Move data between cloud providers
8. **cloud_storage_analytics()** - Monitor usage and performance

## Example

```python
import asyncio
import aiohttp
import aiofiles
import boto3
from azure.storage.blob import BlobServiceClient
from google.cloud import storage as gcs
import dropbox
import hashlib
import json
import time
from pathlib import Path
from typing import Dict, List, Optional, Any, Union, AsyncIterator
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import os
from enum import Enum
import threading
from concurrent.futures import ThreadPoolExecutor

class CloudProvider(Enum):
    AWS_S3 = "aws_s3"
    AZURE_BLOB = "azure_blob"
    GOOGLE_CLOUD = "google_cloud"
    DROPBOX = "dropbox"
    LOCAL = "local"

class ConflictResolution(Enum):
    LATEST_WINS = "latest_wins"
    SIZE_WINS = "size_wins"
    MANUAL = "manual"
    MERGE = "merge"
    KEEP_BOTH = "keep_both"

@dataclass
class CloudFile:
    """Represents a file in cloud storage."""
    path: str
    size: int
    last_modified: datetime
    etag: str
    provider: CloudProvider
    encrypted: bool = False
    metadata: Dict[str, Any] = None

@dataclass
class SyncConflict:
    """Represents a synchronization conflict."""
    local_file: CloudFile
    remote_file: CloudFile
    conflict_type: str
    resolution_strategy: ConflictResolution
    resolved: bool = False

class CloudStorageAdapter:
    """Base class for cloud storage adapters."""
    
    def __init__(self, provider: CloudProvider, config: Dict[str, Any]):
        self.provider = provider
        self.config = config
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize cloud provider client."""
        if self.provider == CloudProvider.AWS_S3:
            self.client = boto3.client(
                's3',
                aws_access_key_id=self.config['access_key'],
                aws_secret_access_key=self.config['secret_key'],
                region_name=self.config.get('region', 'us-east-1')
            )
            self.bucket = self.config['bucket']
        
        elif self.provider == CloudProvider.AZURE_BLOB:
            self.client = BlobServiceClient(
                account_url=f"https://{self.config['account_name']}.blob.core.windows.net",
                credential=self.config['account_key']
            )
            self.container = self.config['container']
        
        elif self.provider == CloudProvider.GOOGLE_CLOUD:
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.config['credentials_path']
            self.client = gcs.Client()
            self.bucket = self.client.bucket(self.config['bucket'])
        
        elif self.provider == CloudProvider.DROPBOX:
            self.client = dropbox.Dropbox(self.config['access_token'])
    
    async def upload_file(self, local_path: Path, remote_path: str, 
                         encrypt: bool = False) -> CloudFile:
        """Upload file to cloud storage."""
        
        if encrypt:
            encrypted_data = await self._encrypt_file(local_path)
            content = encrypted_data
            size = len(encrypted_data)
        else:
            async with aiofiles.open(local_path, 'rb') as f:
                content = await f.read()
            size = local_path.stat().st_size
        
        if self.provider == CloudProvider.AWS_S3:
            response = await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.put_object(
                    Bucket=self.bucket,
                    Key=remote_path,
                    Body=content,
                    Metadata={'encrypted': str(encrypt)}
                )
            )
            etag = response['ETag'].strip('"')
        
        elif self.provider == CloudProvider.AZURE_BLOB:
            blob_client = self.client.get_blob_client(
                container=self.container,
                blob=remote_path
            )
            await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: blob_client.upload_blob(
                    content,
                    overwrite=True,
                    metadata={'encrypted': str(encrypt)}
                )
            )
            properties = await asyncio.get_event_loop().run_in_executor(
                None,
                blob_client.get_blob_properties
            )
            etag = properties.etag
        
        elif self.provider == CloudProvider.GOOGLE_CLOUD:
            blob = self.bucket.blob(remote_path)
            blob.metadata = {'encrypted': str(encrypt)}
            await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: blob.upload_from_string(content)
            )
            etag = blob.etag
        
        elif self.provider == CloudProvider.DROPBOX:
            await asyncio.get_event_loop().run_in_executor(
                None,
                lambda: self.client.files_upload(content, f'/{remote_path}')
            )
            etag = hashlib.md5(content).hexdigest()
        
        return CloudFile(
            path=remote_path,
            size=size,
            last_modified=datetime.now(),
            etag=etag,
            provider=self.provider,
            encrypted=encrypt
        )
    
    async def download_file(self, remote_path: str, local_path: Path,
                           decrypt: bool = False) -> bool:
        """Download file from cloud storage."""
        
        try:
            if self.provider == CloudProvider.AWS_S3:
                response = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: self.client.get_object(Bucket=self.bucket, Key=remote_path)
                )
                content = response['Body'].read()
                encrypted = response.get('Metadata', {}).get('encrypted') == 'True'
            
            elif self.provider == CloudProvider.AZURE_BLOB:
                blob_client = self.client.get_blob_client(
                    container=self.container,
                    blob=remote_path
                )
                download_stream = await asyncio.get_event_loop().run_in_executor(
                    None,
                    blob_client.download_blob
                )
                content = download_stream.readall()
                properties = await asyncio.get_event_loop().run_in_executor(
                    None,
                    blob_client.get_blob_properties
                )
                encrypted = properties.metadata.get('encrypted') == 'True'
            
            elif self.provider == CloudProvider.GOOGLE_CLOUD:
                blob = self.bucket.blob(remote_path)
                content = await asyncio.get_event_loop().run_in_executor(
                    None,
                    blob.download_as_bytes
                )
                encrypted = blob.metadata.get('encrypted') == 'True' if blob.metadata else False
            
            elif self.provider == CloudProvider.DROPBOX:
                _, response = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: self.client.files_download(f'/{remote_path}')
                )
                content = response.content
                encrypted = False  # Dropbox doesn't support custom metadata easily
            
            # Decrypt if necessary
            if decrypt and encrypted:
                content = await self._decrypt_data(content)
            
            # Write to local file
            async with aiofiles.open(local_path, 'wb') as f:
                await f.write(content)
            
            return True
            
        except Exception as e:
            print(f"Error downloading {remote_path}: {e}")
            return False
    
    async def list_files(self, prefix: str = "") -> List[CloudFile]:
        """List files in cloud storage."""
        
        files = []
        
        try:
            if self.provider == CloudProvider.AWS_S3:
                paginator = self.client.get_paginator('list_objects_v2')
                async for page in self._async_paginate(paginator, Bucket=self.bucket, Prefix=prefix):
                    for obj in page.get('Contents', []):
                        files.append(CloudFile(
                            path=obj['Key'],
                            size=obj['Size'],
                            last_modified=obj['LastModified'],
                            etag=obj['ETag'].strip('"'),
                            provider=self.provider
                        ))
            
            elif self.provider == CloudProvider.AZURE_BLOB:
                container_client = self.client.get_container_client(self.container)
                blob_list = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: list(container_client.list_blobs(name_starts_with=prefix))
                )
                for blob in blob_list:
                    files.append(CloudFile(
                        path=blob.name,
                        size=blob.size,
                        last_modified=blob.last_modified,
                        etag=blob.etag,
                        provider=self.provider
                    ))
            
            elif self.provider == CloudProvider.GOOGLE_CLOUD:
                blobs = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: list(self.bucket.list_blobs(prefix=prefix))
                )
                for blob in blobs:
                    files.append(CloudFile(
                        path=blob.name,
                        size=blob.size,
                        last_modified=blob.time_created,
                        etag=blob.etag,
                        provider=self.provider
                    ))
            
            elif self.provider == CloudProvider.DROPBOX:
                result = await asyncio.get_event_loop().run_in_executor(
                    None,
                    lambda: self.client.files_list_folder(f'/{prefix}' if prefix else '', recursive=True)
                )
                for entry in result.entries:
                    if hasattr(entry, 'size'):  # It's a file
                        files.append(CloudFile(
                            path=entry.path_lower.lstrip('/'),
                            size=entry.size,
                            last_modified=entry.server_modified,
                            etag=entry.content_hash,
                            provider=self.provider
                        ))
        
        except Exception as e:
            print(f"Error listing files: {e}")
        
        return files
    
    async def _encrypt_file(self, file_path: Path) -> bytes:
        """Encrypt file content."""
        password = self.config.get('encryption_password', 'default_password').encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt',  # In production, use random salt
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        fernet = Fernet(key)
        
        async with aiofiles.open(file_path, 'rb') as f:
            content = await f.read()
        
        return fernet.encrypt(content)
    
    async def _decrypt_data(self, encrypted_data: bytes) -> bytes:
        """Decrypt data."""
        password = self.config.get('encryption_password', 'default_password').encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'stable_salt',  # Should match encryption salt
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        fernet = Fernet(key)
        
        return fernet.decrypt(encrypted_data)
    
    async def _async_paginate(self, paginator, **kwargs):
        """Async wrapper for boto3 paginator."""
        for page in paginator.paginate(**kwargs):
            yield page

class CloudSyncEngine:
    """Intelligent cloud synchronization engine."""
    
    def __init__(self, local_root: Path, adapters: List[CloudStorageAdapter]):
        self.local_root = Path(local_root)
        self.adapters = {adapter.provider: adapter for adapter in adapters}
        self.sync_state_file = self.local_root / '.sync_state.json'
        self.conflicts: List[SyncConflict] = []
        self.sync_stats = {
            'files_uploaded': 0,
            'files_downloaded': 0,
            'conflicts_resolved': 0,
            'bytes_transferred': 0
        }
    
    async def sync_all_providers(self, 
                               upload: bool = True,
                               download: bool = True,
                               conflict_resolution: ConflictResolution = ConflictResolution.LATEST_WINS):
        """Synchronize with all configured cloud providers."""
        
        sync_state = self._load_sync_state()
        
        for provider, adapter in self.adapters.items():
            print(f"Syncing with {provider.value}...")
            
            try:
                # Get remote files
                remote_files = await adapter.list_files()
                remote_file_map = {f.path: f for f in remote_files}
                
                # Get local files
                local_files = self._get_local_files()
                local_file_map = {str(f.relative_to(self.local_root)): f for f in local_files}
                
                # Upload new/modified local files
                if upload:
                    await self._upload_changes(adapter, local_file_map, remote_file_map, sync_state)
                
                # Download new/modified remote files
                if download:
                    await self._download_changes(adapter, remote_file_map, local_file_map, sync_state)
                
                # Resolve conflicts
                await self._resolve_conflicts(conflict_resolution)
                
                # Update sync state
                sync_state[provider.value] = {
                    'last_sync': datetime.now().isoformat(),
                    'file_states': {
                        path: {
                            'last_modified': file.last_modified.isoformat(),
                            'etag': file.etag,
                            'size': file.size
                        }
                        for path, file in remote_file_map.items()
                    }
                }
                
            except Exception as e:
                print(f"Error syncing with {provider.value}: {e}")
        
        self._save_sync_state(sync_state)
    
    async def _upload_changes(self, adapter: CloudStorageAdapter,
                             local_files: Dict[str, Path],
                             remote_files: Dict[str, CloudFile],
                             sync_state: Dict):
        """Upload changed local files."""
        
        provider_state = sync_state.get(adapter.provider.value, {})
        last_file_states = provider_state.get('file_states', {})
        
        for rel_path, local_path in local_files.items():
            try:
                local_stat = local_path.stat()
                local_modified = datetime.fromtimestamp(local_stat.st_mtime)
                
                should_upload = False
                
                if rel_path not in remote_files:
                    # New file
                    should_upload = True
                    print(f"Uploading new file: {rel_path}")
                
                elif rel_path in last_file_states:
                    # Check if file changed since last sync
                    last_state = last_file_states[rel_path]
                    last_modified = datetime.fromisoformat(last_state['last_modified'])
                    
                    if local_modified > last_modified or local_stat.st_size != last_state['size']:
                        should_upload = True
                        print(f"Uploading modified file: {rel_path}")
                
                if should_upload:
                    encrypt = adapter.config.get('encrypt_files', False)
                    cloud_file = await adapter.upload_file(local_path, rel_path, encrypt)
                    self.sync_stats['files_uploaded'] += 1
                    self.sync_stats['bytes_transferred'] += cloud_file.size
                    
            except Exception as e:
                print(f"Error uploading {rel_path}: {e}")
    
    async def _download_changes(self, adapter: CloudStorageAdapter,
                               remote_files: Dict[str, CloudFile],
                               local_files: Dict[str, Path],
                               sync_state: Dict):
        """Download changed remote files."""
        
        for rel_path, remote_file in remote_files.items():
            try:
                local_path = self.local_root / rel_path
                should_download = False
                
                if rel_path not in local_files:
                    # New remote file
                    should_download = True
                    print(f"Downloading new file: {rel_path}")
                
                else:
                    # Check if remote file is newer
                    local_stat = local_path.stat()
                    local_modified = datetime.fromtimestamp(local_stat.st_mtime)
                    
                    if remote_file.last_modified > local_modified:
                        # Potential conflict - add to conflicts list
                        conflict = SyncConflict(
                            local_file=CloudFile(
                                path=rel_path,
                                size=local_stat.st_size,
                                last_modified=local_modified,
                                etag="",
                                provider=CloudProvider.LOCAL
                            ),
                            remote_file=remote_file,
                            conflict_type="modified_both",
                            resolution_strategy=ConflictResolution.LATEST_WINS
                        )
                        self.conflicts.append(conflict)
                        continue
                
                if should_download:
                    # Ensure directory exists
                    local_path.parent.mkdir(parents=True, exist_ok=True)
                    
                    decrypt = adapter.config.get('encrypt_files', False)
                    success = await adapter.download_file(rel_path, local_path, decrypt)
                    
                    if success:
                        self.sync_stats['files_downloaded'] += 1
                        self.sync_stats['bytes_transferred'] += remote_file.size
                        
            except Exception as e:
                print(f"Error downloading {rel_path}: {e}")
    
    async def _resolve_conflicts(self, resolution_strategy: ConflictResolution):
        """Resolve synchronization conflicts."""
        
        for conflict in self.conflicts:
            if conflict.resolved:
                continue
            
            try:
                if resolution_strategy == ConflictResolution.LATEST_WINS:
                    if conflict.remote_file.last_modified > conflict.local_file.last_modified:
                        # Download remote version
                        local_path = self.local_root / conflict.remote_file.path
                        adapter = self.adapters[conflict.remote_file.provider]
                        await adapter.download_file(conflict.remote_file.path, local_path)
                        print(f"Conflict resolved: kept remote version of {conflict.remote_file.path}")
                    # else: keep local version (do nothing)
                
                elif resolution_strategy == ConflictResolution.SIZE_WINS:
                    if conflict.remote_file.size > conflict.local_file.size:
                        # Download remote version
                        local_path = self.local_root / conflict.remote_file.path
                        adapter = self.adapters[conflict.remote_file.provider]
                        await adapter.download_file(conflict.remote_file.path, local_path)
                        print(f"Conflict resolved: kept larger version of {conflict.remote_file.path}")
                
                elif resolution_strategy == ConflictResolution.KEEP_BOTH:
                    # Rename local file and download remote
                    local_path = self.local_root / conflict.local_file.path
                    backup_path = local_path.with_suffix(f".local_backup{local_path.suffix}")
                    local_path.rename(backup_path)
                    
                    adapter = self.adapters[conflict.remote_file.provider]
                    await adapter.download_file(conflict.remote_file.path, local_path)
                    print(f"Conflict resolved: kept both versions of {conflict.remote_file.path}")
                
                conflict.resolved = True
                self.sync_stats['conflicts_resolved'] += 1
                
            except Exception as e:
                print(f"Error resolving conflict for {conflict.remote_file.path}: {e}")
    
    def _get_local_files(self) -> List[Path]:
        """Get all local files recursively."""
        files = []
        for file_path in self.local_root.rglob('*'):
            if file_path.is_file() and not file_path.name.startswith('.'):
                files.append(file_path)
        return files
    
    def _load_sync_state(self) -> Dict:
        """Load synchronization state from file."""
        if self.sync_state_file.exists():
            try:
                with open(self.sync_state_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading sync state: {e}")
        return {}
    
    def _save_sync_state(self, state: Dict):
        """Save synchronization state to file."""
        try:
            with open(self.sync_state_file, 'w') as f:
                json.dump(state, f, indent=2, default=str)
        except Exception as e:
            print(f"Error saving sync state: {e}")
    
    def get_sync_statistics(self) -> Dict[str, Any]:
        """Get synchronization statistics."""
        return {
            **self.sync_stats,
            'unresolved_conflicts': len([c for c in self.conflicts if not c.resolved]),
            'total_conflicts': len(self.conflicts)
        }

# Example usage
async def example_cloud_sync():
    """Example of cloud synchronization."""
    
    # Configure cloud adapters
    aws_config = {
        'access_key': 'your_access_key',
        'secret_key': 'your_secret_key',
        'bucket': 'your_bucket',
        'region': 'us-west-2',
        'encrypt_files': True,
        'encryption_password': 'your_encryption_password'
    }
    
    azure_config = {
        'account_name': 'your_account',
        'account_key': 'your_key',
        'container': 'your_container',
        'encrypt_files': True,
        'encryption_password': 'your_encryption_password'
    }
    
    # Create adapters
    aws_adapter = CloudStorageAdapter(CloudProvider.AWS_S3, aws_config)
    azure_adapter = CloudStorageAdapter(CloudProvider.AZURE_BLOB, azure_config)
    
    # Create sync engine
    sync_engine = CloudSyncEngine(
        local_root=Path('./sync_folder'),
        adapters=[aws_adapter, azure_adapter]
    )
    
    # Perform synchronization
    await sync_engine.sync_all_providers(
        upload=True,
        download=True,
        conflict_resolution=ConflictResolution.LATEST_WINS
    )
    
    # Print statistics
    stats = sync_engine.get_sync_statistics()
    print(f"Sync completed: {json.dumps(stats, indent=2)}")

if __name__ == "__main__":
    asyncio.run(example_cloud_sync())
```

## Hints

- Use async/await for efficient I/O operations with multiple cloud providers
- Implement proper error handling and retry logic for network operations
- Consider bandwidth optimization with compression and delta sync
- Design conflict resolution strategies based on business requirements

## Practice Cases

Your cloud integration should handle:
- Multiple cloud providers simultaneously
- Network failures and retry scenarios
- Large file uploads and downloads
- Conflict resolution edge cases
- Encryption and security requirements

## Bonus Challenge

Create a complete cloud storage orchestration platform with automatic failover, load balancing across providers, and intelligent data placement based on cost and performance!

Remember: Cloud integration requires robust error handling, security considerations, and efficient bandwidth usage!