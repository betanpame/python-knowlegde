# Distributed File System Architecture - Practice 19

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

## Description

Design and implement a distributed file system with replication, consistency guarantees, fault tolerance, and automatic recovery mechanisms.

## Objectives

- Build a scalable distributed storage architecture
- Implement data replication and consistency protocols
- Create fault-tolerant file operations
- Design automatic recovery and healing systems

## Your Tasks

1. **distributed_storage_nodes()** - Create network of storage nodes
2. **data_replication_manager()** - Handle file replication across nodes
3. **consistency_protocol()** - Ensure data consistency across replicas
4. **fault_detection_system()** - Monitor node health and failures
5. **automatic_recovery_engine()** - Self-healing file system
6. **load_balancing_coordinator()** - Distribute load across nodes
7. **distributed_metadata_service()** - Manage file metadata globally
8. **network_partition_handling()** - Handle split-brain scenarios

## Example

```python
import asyncio
import aiohttp
import json
import hashlib
import time
import random
from pathlib import Path
from typing import Dict, List, Set, Optional, Tuple, Any
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from enum import Enum
import socket
import threading
import logging
from concurrent.futures import ThreadPoolExecutor
import pickle
import struct
import uuid

class NodeStatus(Enum):
    HEALTHY = "healthy"
    DEGRADED = "degraded"
    FAILED = "failed"
    RECOVERING = "recovering"

class ConsistencyLevel(Enum):
    ONE = "one"          # Write to one replica
    QUORUM = "quorum"    # Write to majority of replicas
    ALL = "all"          # Write to all replicas

@dataclass
class StorageNode:
    """Represents a storage node in the distributed system."""
    node_id: str
    host: str
    port: int
    status: NodeStatus
    last_heartbeat: datetime
    storage_path: Path
    capacity_bytes: int
    used_bytes: int
    load_factor: float = 0.0

@dataclass
class FileMetadata:
    """Metadata for distributed files."""
    file_id: str
    filename: str
    size: int
    checksum: str
    created_at: datetime
    modified_at: datetime
    replica_nodes: List[str]
    version: int
    consistency_level: ConsistencyLevel

@dataclass
class ReplicationTask:
    """Task for replicating data across nodes."""
    file_id: str
    source_node: str
    target_nodes: List[str]
    priority: int
    created_at: datetime
    retries: int = 0

class DistributedStorageNode:
    """Individual storage node in the distributed file system."""
    
    def __init__(self, 
                 node_id: str,
                 host: str,
                 port: int,
                 storage_path: Path,
                 capacity_gb: int = 100):
        self.node_id = node_id
        self.host = host
        self.port = port
        self.storage_path = Path(storage_path)
        self.capacity_bytes = capacity_gb * 1024 * 1024 * 1024
        
        # Ensure storage directory exists
        self.storage_path.mkdir(parents=True, exist_ok=True)
        
        # Node state
        self.status = NodeStatus.HEALTHY
        self.peers: Dict[str, StorageNode] = {}
        self.metadata_cache: Dict[str, FileMetadata] = {}
        self.replication_queue: List[ReplicationTask] = []
        
        # Network and threading
        self.server = None
        self.executor = ThreadPoolExecutor(max_workers=10)
        self.running = False
        
        # Logging
        self.logger = self._setup_logging()
        
        # Heartbeat and monitoring
        self.last_heartbeat = datetime.now()
        self.heartbeat_interval = 10  # seconds
        
    def _setup_logging(self) -> logging.Logger:
        """Setup node-specific logging."""
        logger = logging.getLogger(f'storage_node_{self.node_id}')
        logger.setLevel(logging.INFO)
        
        handler = logging.FileHandler(self.storage_path / f'node_{self.node_id}.log')
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        
        return logger
    
    async def start(self):
        """Start the storage node server."""
        self.running = True
        
        # Start HTTP server for node communication
        app = aiohttp.web.Application()
        self._setup_routes(app)
        
        self.server = aiohttp.web.AppRunner(app)
        await self.server.setup()
        
        site = aiohttp.web.TCPSite(self.server, self.host, self.port)
        await site.start()
        
        self.logger.info(f"Storage node {self.node_id} started on {self.host}:{self.port}")
        
        # Start background tasks
        asyncio.create_task(self._heartbeat_loop())
        asyncio.create_task(self._replication_worker())
        asyncio.create_task(self._health_monitor())
    
    async def stop(self):
        """Stop the storage node."""
        self.running = False
        if self.server:
            await self.server.cleanup()
        self.executor.shutdown(wait=True)
        self.logger.info(f"Storage node {self.node_id} stopped")
    
    def _setup_routes(self, app):
        """Setup HTTP routes for node communication."""
        app.router.add_post('/store', self._handle_store_file)
        app.router.add_get('/retrieve/{file_id}', self._handle_retrieve_file)
        app.router.add_delete('/delete/{file_id}', self._handle_delete_file)
        app.router.add_post('/replicate', self._handle_replicate)
        app.router.add_get('/heartbeat', self._handle_heartbeat)
        app.router.add_get('/status', self._handle_status)
        app.router.add_post('/metadata', self._handle_metadata_update)
    
    async def _handle_store_file(self, request):
        """Handle file storage request."""
        try:
            data = await request.json()
            file_id = data['file_id']
            filename = data['filename']
            content = data['content'].encode() if isinstance(data['content'], str) else data['content']
            
            # Store file locally
            file_path = self.storage_path / f"{file_id}_{filename}"
            
            async with aiohttp.ClientSession() as session:
                async with session.post(file_path, data=content) as resp:
                    pass
            
            # Calculate checksum
            checksum = hashlib.sha256(content).hexdigest()
            
            # Create metadata
            metadata = FileMetadata(
                file_id=file_id,
                filename=filename,
                size=len(content),
                checksum=checksum,
                created_at=datetime.now(),
                modified_at=datetime.now(),
                replica_nodes=[self.node_id],
                version=1,
                consistency_level=ConsistencyLevel.QUORUM
            )
            
            self.metadata_cache[file_id] = metadata
            
            # Schedule replication
            await self._schedule_replication(file_id, content, metadata)
            
            self.logger.info(f"Stored file {file_id} ({len(content)} bytes)")
            
            return aiohttp.web.json_response({
                'status': 'success',
                'file_id': file_id,
                'checksum': checksum
            })
            
        except Exception as e:
            self.logger.error(f"Error storing file: {e}")
            return aiohttp.web.json_response({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    async def _handle_retrieve_file(self, request):
        """Handle file retrieval request."""
        try:
            file_id = request.match_info['file_id']
            
            if file_id not in self.metadata_cache:
                return aiohttp.web.json_response({
                    'status': 'error',
                    'message': 'File not found'
                }, status=404)
            
            metadata = self.metadata_cache[file_id]
            file_path = self.storage_path / f"{file_id}_{metadata.filename}"
            
            if not file_path.exists():
                # Try to retrieve from other replicas
                content = await self._retrieve_from_replicas(file_id)
                if not content:
                    return aiohttp.web.json_response({
                        'status': 'error',
                        'message': 'File not available'
                    }, status=404)
            else:
                with open(file_path, 'rb') as f:
                    content = f.read()
            
            # Verify checksum
            calculated_checksum = hashlib.sha256(content).hexdigest()
            if calculated_checksum != metadata.checksum:
                self.logger.error(f"Checksum mismatch for file {file_id}")
                return aiohttp.web.json_response({
                    'status': 'error',
                    'message': 'File corrupted'
                }, status=500)
            
            self.logger.info(f"Retrieved file {file_id} ({len(content)} bytes)")
            
            return aiohttp.web.Response(
                body=content,
                headers={'Content-Type': 'application/octet-stream'}
            )
            
        except Exception as e:
            self.logger.error(f"Error retrieving file: {e}")
            return aiohttp.web.json_response({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    async def _handle_replicate(self, request):
        """Handle replication request from other nodes."""
        try:
            data = await request.json()
            file_id = data['file_id']
            filename = data['filename']
            content = bytes(data['content'])
            checksum = data['checksum']
            
            # Verify checksum
            calculated_checksum = hashlib.sha256(content).hexdigest()
            if calculated_checksum != checksum:
                return aiohttp.web.json_response({
                    'status': 'error',
                    'message': 'Checksum verification failed'
                }, status=400)
            
            # Store replica
            file_path = self.storage_path / f"{file_id}_{filename}"
            with open(file_path, 'wb') as f:
                f.write(content)
            
            # Update metadata
            if file_id in self.metadata_cache:
                metadata = self.metadata_cache[file_id]
                if self.node_id not in metadata.replica_nodes:
                    metadata.replica_nodes.append(self.node_id)
            
            self.logger.info(f"Replicated file {file_id} from peer")
            
            return aiohttp.web.json_response({'status': 'success'})
            
        except Exception as e:
            self.logger.error(f"Error replicating file: {e}")
            return aiohttp.web.json_response({
                'status': 'error',
                'message': str(e)
            }, status=500)
    
    async def _handle_heartbeat(self, request):
        """Handle heartbeat request."""
        self.last_heartbeat = datetime.now()
        
        return aiohttp.web.json_response({
            'node_id': self.node_id,
            'status': self.status.value,
            'timestamp': self.last_heartbeat.isoformat(),
            'load_factor': self._calculate_load_factor()
        })
    
    async def _handle_status(self, request):
        """Handle status request."""
        used_bytes = sum(
            f.stat().st_size 
            for f in self.storage_path.rglob('*') 
            if f.is_file()
        )
        
        return aiohttp.web.json_response({
            'node_id': self.node_id,
            'status': self.status.value,
            'capacity_bytes': self.capacity_bytes,
            'used_bytes': used_bytes,
            'free_bytes': self.capacity_bytes - used_bytes,
            'file_count': len(self.metadata_cache),
            'peer_count': len(self.peers),
            'replication_queue_size': len(self.replication_queue)
        })
    
    async def _schedule_replication(self, file_id: str, content: bytes, metadata: FileMetadata):
        """Schedule file replication to other nodes."""
        
        # Determine target replica count based on consistency level
        target_replicas = 3  # Default replication factor
        
        if metadata.consistency_level == ConsistencyLevel.ALL:
            target_replicas = len(self.peers)
        elif metadata.consistency_level == ConsistencyLevel.QUORUM:
            target_replicas = max(3, len(self.peers) // 2 + 1)
        
        # Select target nodes (exclude current node)
        available_nodes = [
            node for node in self.peers.values()
            if node.status == NodeStatus.HEALTHY and node.node_id != self.node_id
        ]
        
        # Sort by load factor and select least loaded nodes
        available_nodes.sort(key=lambda n: n.load_factor)
        target_nodes = available_nodes[:target_replicas-1]  # -1 because we already have one copy
        
        # Create replication tasks
        for target_node in target_nodes:
            task = ReplicationTask(
                file_id=file_id,
                source_node=self.node_id,
                target_nodes=[target_node.node_id],
                priority=1,
                created_at=datetime.now()
            )
            self.replication_queue.append(task)
        
        self.logger.info(f"Scheduled replication of {file_id} to {len(target_nodes)} nodes")
    
    async def _replication_worker(self):
        """Background worker for processing replication tasks."""
        while self.running:
            try:
                if self.replication_queue:
                    task = self.replication_queue.pop(0)
                    await self._execute_replication_task(task)
                else:
                    await asyncio.sleep(1)
            except Exception as e:
                self.logger.error(f"Replication worker error: {e}")
                await asyncio.sleep(5)
    
    async def _execute_replication_task(self, task: ReplicationTask):
        """Execute a replication task."""
        try:
            # Get file metadata and content
            if task.file_id not in self.metadata_cache:
                self.logger.error(f"Cannot replicate {task.file_id}: metadata not found")
                return
            
            metadata = self.metadata_cache[task.file_id]
            file_path = self.storage_path / f"{task.file_id}_{metadata.filename}"
            
            if not file_path.exists():
                self.logger.error(f"Cannot replicate {task.file_id}: file not found locally")
                return
            
            with open(file_path, 'rb') as f:
                content = f.read()
            
            # Replicate to target nodes
            successful_replications = 0
            
            for target_node_id in task.target_nodes:
                if target_node_id in self.peers:
                    target_node = self.peers[target_node_id]
                    
                    success = await self._replicate_to_node(
                        target_node, task.file_id, metadata.filename, content, metadata.checksum
                    )
                    
                    if success:
                        successful_replications += 1
                        # Update metadata to include new replica
                        if target_node_id not in metadata.replica_nodes:
                            metadata.replica_nodes.append(target_node_id)
            
            if successful_replications > 0:
                self.logger.info(f"Successfully replicated {task.file_id} to {successful_replications} nodes")
            else:
                # Retry task if it failed
                task.retries += 1
                if task.retries < 3:
                    self.replication_queue.append(task)
                    self.logger.warning(f"Replication of {task.file_id} failed, scheduled for retry")
                else:
                    self.logger.error(f"Replication of {task.file_id} failed after 3 retries")
            
        except Exception as e:
            self.logger.error(f"Error executing replication task: {e}")
    
    async def _replicate_to_node(self, target_node: StorageNode, 
                                file_id: str, filename: str, 
                                content: bytes, checksum: str) -> bool:
        """Replicate file to a specific node."""
        try:
            url = f"http://{target_node.host}:{target_node.port}/replicate"
            
            payload = {
                'file_id': file_id,
                'filename': filename,
                'content': list(content),  # Convert bytes to list for JSON
                'checksum': checksum
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=payload, timeout=30) as response:
                    if response.status == 200:
                        return True
                    else:
                        self.logger.error(f"Replication to {target_node.node_id} failed: {response.status}")
                        return False
                        
        except Exception as e:
            self.logger.error(f"Error replicating to {target_node.node_id}: {e}")
            return False
    
    async def _retrieve_from_replicas(self, file_id: str) -> Optional[bytes]:
        """Retrieve file from replica nodes if local copy is missing."""
        if file_id not in self.metadata_cache:
            return None
        
        metadata = self.metadata_cache[file_id]
        
        for replica_node_id in metadata.replica_nodes:
            if replica_node_id == self.node_id:
                continue
                
            if replica_node_id in self.peers:
                replica_node = self.peers[replica_node_id]
                
                try:
                    url = f"http://{replica_node.host}:{replica_node.port}/retrieve/{file_id}"
                    
                    async with aiohttp.ClientSession() as session:
                        async with session.get(url, timeout=30) as response:
                            if response.status == 200:
                                content = await response.read()
                                
                                # Verify checksum
                                calculated_checksum = hashlib.sha256(content).hexdigest()
                                if calculated_checksum == metadata.checksum:
                                    # Store locally for future access
                                    file_path = self.storage_path / f"{file_id}_{metadata.filename}"
                                    with open(file_path, 'wb') as f:
                                        f.write(content)
                                    
                                    self.logger.info(f"Retrieved {file_id} from replica {replica_node_id}")
                                    return content
                                else:
                                    self.logger.error(f"Checksum mismatch when retrieving from {replica_node_id}")
                                    
                except Exception as e:
                    self.logger.error(f"Error retrieving from replica {replica_node_id}: {e}")
        
        return None
    
    async def _heartbeat_loop(self):
        """Send heartbeats to peer nodes."""
        while self.running:
            try:
                # Send heartbeats to all peers
                for peer_id, peer in list(self.peers.items()):
                    try:
                        url = f"http://{peer.host}:{peer.port}/heartbeat"
                        
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url, timeout=5) as response:
                                if response.status == 200:
                                    data = await response.json()
                                    peer.last_heartbeat = datetime.fromisoformat(data['timestamp'])
                                    peer.status = NodeStatus(data['status'])
                                    peer.load_factor = data['load_factor']
                                else:
                                    peer.status = NodeStatus.FAILED
                                    
                    except Exception as e:
                        self.logger.warning(f"Heartbeat failed for peer {peer_id}: {e}")
                        peer.status = NodeStatus.FAILED
                
                await asyncio.sleep(self.heartbeat_interval)
                
            except Exception as e:
                self.logger.error(f"Heartbeat loop error: {e}")
                await asyncio.sleep(self.heartbeat_interval)
    
    async def _health_monitor(self):
        """Monitor overall cluster health and trigger recovery if needed."""
        while self.running:
            try:
                # Check for failed nodes
                failed_nodes = [
                    peer for peer in self.peers.values()
                    if peer.status == NodeStatus.FAILED
                ]
                
                if failed_nodes:
                    self.logger.warning(f"Detected {len(failed_nodes)} failed nodes")
                    await self._trigger_recovery(failed_nodes)
                
                await asyncio.sleep(30)  # Check every 30 seconds
                
            except Exception as e:
                self.logger.error(f"Health monitor error: {e}")
                await asyncio.sleep(30)
    
    async def _trigger_recovery(self, failed_nodes: List[StorageNode]):
        """Trigger recovery procedures for failed nodes."""
        # Find files that need re-replication due to failed nodes
        files_needing_replication = []
        
        for file_id, metadata in self.metadata_cache.items():
            # Count healthy replicas
            healthy_replicas = 0
            for replica_node_id in metadata.replica_nodes:
                if replica_node_id in self.peers:
                    peer = self.peers[replica_node_id]
                    if peer.status == NodeStatus.HEALTHY:
                        healthy_replicas += 1
                elif replica_node_id == self.node_id:
                    healthy_replicas += 1
            
            # Check if we need more replicas
            required_replicas = 3  # Default
            if metadata.consistency_level == ConsistencyLevel.ALL:
                required_replicas = len([p for p in self.peers.values() if p.status == NodeStatus.HEALTHY]) + 1
            elif metadata.consistency_level == ConsistencyLevel.QUORUM:
                required_replicas = max(3, (len([p for p in self.peers.values() if p.status == NodeStatus.HEALTHY]) + 1) // 2 + 1)
            
            if healthy_replicas < required_replicas:
                files_needing_replication.append(file_id)
        
        if files_needing_replication:
            self.logger.info(f"Scheduling re-replication for {len(files_needing_replication)} files")
            
            # Create high-priority replication tasks
            for file_id in files_needing_replication:
                metadata = self.metadata_cache[file_id]
                
                # Find healthy nodes that don't already have the file
                available_nodes = [
                    node for node in self.peers.values()
                    if (node.status == NodeStatus.HEALTHY and 
                        node.node_id not in metadata.replica_nodes)
                ]
                
                if available_nodes:
                    # Sort by load factor and select least loaded
                    available_nodes.sort(key=lambda n: n.load_factor)
                    target_node = available_nodes[0]
                    
                    task = ReplicationTask(
                        file_id=file_id,
                        source_node=self.node_id,
                        target_nodes=[target_node.node_id],
                        priority=10,  # High priority for recovery
                        created_at=datetime.now()
                    )
                    
                    # Insert at beginning for high priority
                    self.replication_queue.insert(0, task)
    
    def _calculate_load_factor(self) -> float:
        """Calculate current load factor of the node."""
        try:
            used_bytes = sum(
                f.stat().st_size 
                for f in self.storage_path.rglob('*') 
                if f.is_file()
            )
            
            storage_load = used_bytes / self.capacity_bytes
            queue_load = len(self.replication_queue) / 100.0  # Normalize queue size
            
            return min(1.0, storage_load + queue_load)
            
        except Exception:
            return 0.5  # Default load factor
    
    def add_peer(self, peer: StorageNode):
        """Add a peer node to the cluster."""
        self.peers[peer.node_id] = peer
        self.logger.info(f"Added peer node {peer.node_id}")
    
    def remove_peer(self, node_id: str):
        """Remove a peer node from the cluster."""
        if node_id in self.peers:
            del self.peers[node_id]
            self.logger.info(f"Removed peer node {node_id}")

# Example usage
async def example_distributed_filesystem():
    """Example of distributed filesystem setup and usage."""
    
    # Create storage nodes
    node1 = DistributedStorageNode("node1", "localhost", 8001, Path("./storage/node1"))
    node2 = DistributedStorageNode("node2", "localhost", 8002, Path("./storage/node2"))
    node3 = DistributedStorageNode("node3", "localhost", 8003, Path("./storage/node3"))
    
    # Setup peer relationships
    peer1 = StorageNode("node1", "localhost", 8001, NodeStatus.HEALTHY, datetime.now(), Path("./storage/node1"), 100*1024*1024*1024, 0)
    peer2 = StorageNode("node2", "localhost", 8002, NodeStatus.HEALTHY, datetime.now(), Path("./storage/node2"), 100*1024*1024*1024, 0)
    peer3 = StorageNode("node3", "localhost", 8003, NodeStatus.HEALTHY, datetime.now(), Path("./storage/node3"), 100*1024*1024*1024, 0)
    
    node1.add_peer(peer2)
    node1.add_peer(peer3)
    node2.add_peer(peer1)
    node2.add_peer(peer3)
    node3.add_peer(peer1)
    node3.add_peer(peer2)
    
    # Start all nodes
    await asyncio.gather(
        node1.start(),
        node2.start(),
        node3.start()
    )
    
    print("Distributed filesystem started successfully!")
    
    # Example: Store a file
    # This would typically be done through a client interface
    # For demonstration, we'll simulate it here
    
    try:
        # Keep the system running
        await asyncio.sleep(3600)  # Run for 1 hour
    finally:
        # Cleanup
        await asyncio.gather(
            node1.stop(),
            node2.stop(),
            node3.stop()
        )

if __name__ == "__main__":
    asyncio.run(example_distributed_filesystem())
```

## Hints

- Implement consensus algorithms like Raft for metadata consistency
- Use vector clocks or logical timestamps for conflict resolution
- Design proper failure detection with configurable timeouts
- Consider network partitions and split-brain scenarios

## Practice Cases

Your distributed system should handle:
- Node failures and automatic recovery
- Network partitions and consistency guarantees
- Concurrent read/write operations
- Large-scale replication scenarios
- Byzantine failure scenarios

## Bonus Challenge

Create a complete distributed filesystem with support for transactions, snapshots, and geographic distribution across data centers!

Remember: Distributed systems require careful handling of consistency, availability, and partition tolerance (CAP theorem)!