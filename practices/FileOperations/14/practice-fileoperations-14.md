# Asynchronous File Operations - Practice 14

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn to perform file operations asynchronously for better performance in I/O-intensive applications.

## Objectives

- Implement async file reading and writing
- Handle multiple file operations concurrently
- Create efficient async file processing pipelines
- Manage async file streaming

## Your Tasks

1. **async_file_reader()** - Read files asynchronously
2. **async_file_writer()** - Write files without blocking
3. **concurrent_file_processing()** - Process multiple files simultaneously
4. **async_file_streaming()** - Stream large files asynchronously
5. **async_directory_operations()** - Handle directory operations concurrently
6. **async_file_monitoring()** - Monitor file changes asynchronously
7. **async_batch_operations()** - Batch process files efficiently
8. **async_file_synchronization()** - Sync files between locations

## Example

```python
import asyncio
import aiofiles
import aiohttp
from pathlib import Path
from typing import List, Dict, Any, AsyncIterator
import time
from concurrent.futures import ThreadPoolExecutor

class AsyncFileManager:
    """Asynchronous file operations manager."""
    
    def __init__(self, max_concurrent: int = 10):
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.executor = ThreadPoolExecutor(max_workers=4)
    
    async def read_file_async(self, file_path: Path) -> str:
        """Read file asynchronously."""
        async with self.semaphore:
            try:
                async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
                    content = await file.read()
                    return content
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                return ""
    
    async def write_file_async(self, file_path: Path, content: str) -> bool:
        """Write file asynchronously."""
        async with self.semaphore:
            try:
                async with aiofiles.open(file_path, 'w', encoding='utf-8') as file:
                    await file.write(content)
                    return True
            except Exception as e:
                print(f"Error writing {file_path}: {e}")
                return False
    
    async def process_files_concurrently(self, 
                                       file_paths: List[Path],
                                       processor_func) -> List[Any]:
        """Process multiple files concurrently."""
        
        async def process_single_file(path: Path):
            content = await self.read_file_async(path)
            return await processor_func(path, content)
        
        # Create tasks for all files
        tasks = [process_single_file(path) for path in file_paths]
        
        # Execute concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results
    
    async def stream_large_file(self, 
                              file_path: Path, 
                              chunk_size: int = 8192) -> AsyncIterator[str]:
        """Stream large file in chunks asynchronously."""
        async with self.semaphore:
            try:
                async with aiofiles.open(file_path, 'r', encoding='utf-8') as file:
                    while True:
                        chunk = await file.read(chunk_size)
                        if not chunk:
                            break
                        yield chunk
            except Exception as e:
                print(f"Error streaming {file_path}: {e}")
    
    async def copy_files_async(self, 
                             source_paths: List[Path], 
                             destination_dir: Path) -> Dict[Path, bool]:
        """Copy multiple files asynchronously."""
        
        results = {}
        
        async def copy_single_file(source: Path) -> bool:
            try:
                destination = destination_dir / source.name
                content = await self.read_file_async(source)
                success = await self.write_file_async(destination, content)
                return success
            except Exception as e:
                print(f"Error copying {source}: {e}")
                return False
        
        # Create tasks for all copy operations
        tasks = []
        for source_path in source_paths:
            task = copy_single_file(source_path)
            tasks.append(task)
        
        # Execute all copy operations concurrently
        copy_results = await asyncio.gather(*tasks)
        
        # Map results back to source paths
        for source_path, success in zip(source_paths, copy_results):
            results[source_path] = success
        
        return results
    
    async def download_files_async(self, urls_and_paths: List[tuple]) -> Dict[str, bool]:
        """Download files from URLs asynchronously."""
        
        results = {}
        
        async def download_single_file(url: str, file_path: Path) -> bool:
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url) as response:
                        if response.status == 200:
                            content = await response.text()
                            success = await self.write_file_async(file_path, content)
                            return success
                        else:
                            print(f"HTTP {response.status} for {url}")
                            return False
            except Exception as e:
                print(f"Error downloading {url}: {e}")
                return False
        
        # Create tasks for all downloads
        tasks = []
        for url, file_path in urls_and_paths:
            task = download_single_file(url, file_path)
            tasks.append(task)
        
        # Execute downloads concurrently
        download_results = await asyncio.gather(*tasks)
        
        # Map results back to URLs
        for (url, _), success in zip(urls_and_paths, download_results):
            results[url] = success
        
        return results
    
    async def monitor_directory_changes(self, 
                                      directory: Path, 
                                      callback,
                                      interval: float = 1.0):
        """Monitor directory for changes asynchronously."""
        
        last_state = {}
        
        def get_directory_state():
            """Get current state of directory."""
            state = {}
            if directory.exists():
                for file_path in directory.rglob('*'):
                    if file_path.is_file():
                        stat = file_path.stat()
                        state[str(file_path)] = {
                            'size': stat.st_size,
                            'mtime': stat.st_mtime
                        }
            return state
        
        # Get initial state
        last_state = await asyncio.get_event_loop().run_in_executor(
            self.executor, get_directory_state
        )
        
        while True:
            await asyncio.sleep(interval)
            
            # Get current state
            current_state = await asyncio.get_event_loop().run_in_executor(
                self.executor, get_directory_state
            )
            
            # Compare states
            changes = []
            
            # Check for new or modified files
            for file_path, info in current_state.items():
                if file_path not in last_state:
                    changes.append(('created', file_path))
                elif last_state[file_path] != info:
                    changes.append(('modified', file_path))
            
            # Check for deleted files
            for file_path in last_state:
                if file_path not in current_state:
                    changes.append(('deleted', file_path))
            
            # Notify of changes
            if changes:
                await callback(changes)
            
            last_state = current_state

# Example usage
async def example_async_file_operations():
    """Example of using async file operations."""
    
    manager = AsyncFileManager(max_concurrent=5)
    
    # Example 1: Process multiple files concurrently
    async def word_counter(file_path: Path, content: str) -> Dict[str, Any]:
        word_count = len(content.split())
        return {
            'file': str(file_path),
            'word_count': word_count,
            'size': len(content)
        }
    
    file_paths = [
        Path('file1.txt'),
        Path('file2.txt'),
        Path('file3.txt')
    ]
    
    # Process all files concurrently
    results = await manager.process_files_concurrently(file_paths, word_counter)
    print("Processing results:", results)
    
    # Example 2: Stream large file
    async for chunk in manager.stream_large_file(Path('large_file.txt')):
        # Process chunk
        processed_chunk = chunk.upper()
        # Could write to another file, send over network, etc.
    
    # Example 3: Monitor directory changes
    async def change_handler(changes):
        for change_type, file_path in changes:
            print(f"File {change_type}: {file_path}")
    
    # Start monitoring (this would run indefinitely)
    # await manager.monitor_directory_changes(Path('./watched_dir'), change_handler)
```

## Hints

- Use aiofiles for async file I/O operations
- Implement semaphores to limit concurrent operations
- Consider using asyncio.gather for parallel execution
- Use ThreadPoolExecutor for CPU-bound file operations

## Practice Cases

Your async implementation should handle:
- Multiple concurrent file operations
- Large file streaming without memory issues
- Proper error handling in async contexts
- Efficient resource management with semaphores

## Bonus Challenge

Create an async file processing pipeline that can handle thousands of files efficiently with progress tracking and error recovery!

Remember: Async file operations can significantly improve performance for I/O-intensive applications!