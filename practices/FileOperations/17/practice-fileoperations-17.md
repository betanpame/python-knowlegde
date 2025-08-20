# High-Performance File Processing Pipeline - Practice 17

**Difficulty:** ⭐⭐⭐ (Medium)

## Description

Build a high-performance file processing pipeline that can handle massive datasets efficiently using parallel processing, memory mapping, and optimized I/O operations.

## Objectives

- Implement parallel file processing architectures
- Use memory mapping for efficient large file handling
- Create optimized I/O pipelines with buffering
- Design scalable data transformation workflows

## Your Tasks

1. **parallel_file_processor()** - Process files using multiple CPU cores
2. **memory_mapped_file_handler()** - Handle huge files with memory mapping
3. **streaming_data_pipeline()** - Process data streams efficiently
4. **compressed_file_processor()** - Handle compressed data on-the-fly
5. **distributed_file_processing()** - Scale processing across machines
6. **real_time_file_monitor()** - Process files as they arrive
7. **optimized_io_operations()** - Minimize I/O overhead
8. **performance_monitoring_system()** - Track processing metrics

## Example

```python
import multiprocessing as mp
import mmap
import gzip
import lz4.frame
import threading
import queue
import time
from pathlib import Path
from typing import Callable, Iterator, List, Dict, Any, Optional
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from dataclasses import dataclass
import psutil
import io

@dataclass
class ProcessingStats:
    """Performance statistics for file processing."""
    files_processed: int = 0
    bytes_processed: int = 0
    processing_time: float = 0.0
    throughput_mbps: float = 0.0
    peak_memory_usage: int = 0
    errors: int = 0

class HighPerformanceFileProcessor:
    """High-performance file processing with parallel execution."""
    
    def __init__(self, 
                 max_workers: int = None,
                 chunk_size: int = 64 * 1024,  # 64KB chunks
                 buffer_size: int = 8 * 1024 * 1024):  # 8MB buffer
        self.max_workers = max_workers or mp.cpu_count()
        self.chunk_size = chunk_size
        self.buffer_size = buffer_size
        self.stats = ProcessingStats()
        self._monitor_thread = None
        self._stop_monitoring = threading.Event()
    
    def process_files_parallel(self, 
                             file_paths: List[Path],
                             processor_func: Callable,
                             use_processes: bool = True) -> List[Any]:
        """Process multiple files in parallel."""
        
        start_time = time.time()
        initial_memory = psutil.Process().memory_info().rss
        
        # Start performance monitoring
        self._start_monitoring()
        
        try:
            if use_processes:
                # Use processes for CPU-bound tasks
                with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
                    # Submit all tasks
                    future_to_file = {
                        executor.submit(self._process_single_file, file_path, processor_func): file_path
                        for file_path in file_paths
                    }
                    
                    results = []
                    for future in as_completed(future_to_file):
                        file_path = future_to_file[future]
                        try:
                            result = future.result()
                            results.append(result)
                            self.stats.files_processed += 1
                            if file_path.exists():
                                self.stats.bytes_processed += file_path.stat().st_size
                        except Exception as e:
                            print(f"Error processing {file_path}: {e}")
                            self.stats.errors += 1
                            results.append(None)
            else:
                # Use threads for I/O-bound tasks
                with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                    future_to_file = {
                        executor.submit(self._process_single_file, file_path, processor_func): file_path
                        for file_path in file_paths
                    }
                    
                    results = []
                    for future in as_completed(future_to_file):
                        file_path = future_to_file[future]
                        try:
                            result = future.result()
                            results.append(result)
                            self.stats.files_processed += 1
                            if file_path.exists():
                                self.stats.bytes_processed += file_path.stat().st_size
                        except Exception as e:
                            print(f"Error processing {file_path}: {e}")
                            self.stats.errors += 1
                            results.append(None)
            
            # Update statistics
            self.stats.processing_time = time.time() - start_time
            self.stats.peak_memory_usage = max(
                self.stats.peak_memory_usage,
                psutil.Process().memory_info().rss - initial_memory
            )
            
            if self.stats.processing_time > 0:
                self.stats.throughput_mbps = (
                    self.stats.bytes_processed / (1024 * 1024) / self.stats.processing_time
                )
            
            return results
            
        finally:
            self._stop_monitoring.set()
    
    def process_large_file_mmap(self, 
                               file_path: Path,
                               processor_func: Callable,
                               chunk_size: int = None) -> Any:
        """Process large file using memory mapping."""
        
        chunk_size = chunk_size or self.chunk_size
        
        with open(file_path, 'rb') as file:
            # Memory map the file
            with mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as mmapped_file:
                file_size = len(mmapped_file)
                results = []
                
                # Process file in chunks
                for offset in range(0, file_size, chunk_size):
                    end_offset = min(offset + chunk_size, file_size)
                    chunk = mmapped_file[offset:end_offset]
                    
                    # Process chunk
                    try:
                        result = processor_func(chunk, offset, end_offset)
                        if result is not None:
                            results.append(result)
                    except Exception as e:
                        print(f"Error processing chunk at offset {offset}: {e}")
                        self.stats.errors += 1
                
                return results
    
    def create_streaming_pipeline(self, 
                                input_source: Iterator,
                                transformers: List[Callable],
                                output_sink: Callable,
                                queue_size: int = 1000) -> None:
        """Create a streaming data processing pipeline."""
        
        # Create queues for pipeline stages
        queues = [queue.Queue(maxsize=queue_size) for _ in range(len(transformers) + 1)]
        
        def producer():
            """Producer thread - reads from input source."""
            try:
                for item in input_source:
                    queues[0].put(item)
            except Exception as e:
                print(f"Producer error: {e}")
            finally:
                queues[0].put(None)  # Sentinel value
        
        def transformer_worker(stage_idx: int, transformer: Callable):
            """Transformer worker thread."""
            input_queue = queues[stage_idx]
            output_queue = queues[stage_idx + 1]
            
            try:
                while True:
                    item = input_queue.get()
                    if item is None:  # Sentinel value
                        output_queue.put(None)
                        break
                    
                    try:
                        transformed = transformer(item)
                        output_queue.put(transformed)
                    except Exception as e:
                        print(f"Transformer {stage_idx} error: {e}")
                        self.stats.errors += 1
                    finally:
                        input_queue.task_done()
            except Exception as e:
                print(f"Transformer worker {stage_idx} error: {e}")
        
        def consumer():
            """Consumer thread - writes to output sink."""
            final_queue = queues[-1]
            
            try:
                while True:
                    item = final_queue.get()
                    if item is None:  # Sentinel value
                        break
                    
                    try:
                        output_sink(item)
                    except Exception as e:
                        print(f"Consumer error: {e}")
                        self.stats.errors += 1
                    finally:
                        final_queue.task_done()
            except Exception as e:
                print(f"Consumer error: {e}")
        
        # Start all threads
        threads = []
        
        # Producer thread
        producer_thread = threading.Thread(target=producer)
        threads.append(producer_thread)
        producer_thread.start()
        
        # Transformer threads
        for i, transformer in enumerate(transformers):
            transformer_thread = threading.Thread(
                target=transformer_worker, 
                args=(i, transformer)
            )
            threads.append(transformer_thread)
            transformer_thread.start()
        
        # Consumer thread
        consumer_thread = threading.Thread(target=consumer)
        threads.append(consumer_thread)
        consumer_thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join()
    
    def process_compressed_files(self, 
                               file_paths: List[Path],
                               processor_func: Callable) -> List[Any]:
        """Process compressed files efficiently."""
        
        def decompress_and_process(file_path: Path) -> Any:
            """Decompress file and process contents."""
            
            suffix = file_path.suffix.lower()
            
            try:
                if suffix == '.gz':
                    with gzip.open(file_path, 'rb') as compressed_file:
                        # Process in chunks to avoid loading entire file
                        results = []
                        buffer = io.BytesIO()
                        
                        while True:
                            chunk = compressed_file.read(self.chunk_size)
                            if not chunk:
                                break
                            
                            buffer.write(chunk)
                            
                            # Process when buffer is full or at end
                            if buffer.tell() >= self.buffer_size or len(chunk) < self.chunk_size:
                                buffer.seek(0)
                                result = processor_func(buffer.read())
                                if result:
                                    results.append(result)
                                buffer = io.BytesIO()
                        
                        return results
                
                elif suffix == '.lz4':
                    with lz4.frame.open(file_path, 'rb') as compressed_file:
                        content = compressed_file.read()
                        return processor_func(content)
                
                else:
                    # Uncompressed file
                    with open(file_path, 'rb') as file:
                        content = file.read()
                        return processor_func(content)
                        
            except Exception as e:
                print(f"Error processing compressed file {file_path}: {e}")
                self.stats.errors += 1
                return None
        
        return self.process_files_parallel(file_paths, decompress_and_process)
    
    def monitor_and_process_directory(self, 
                                    watch_directory: Path,
                                    processor_func: Callable,
                                    file_pattern: str = "*",
                                    poll_interval: float = 1.0) -> None:
        """Monitor directory and process new files as they arrive."""
        
        processed_files = set()
        
        print(f"Monitoring {watch_directory} for new files...")
        
        try:
            while not self._stop_monitoring.is_set():
                # Find new files
                current_files = set(watch_directory.glob(file_pattern))
                new_files = current_files - processed_files
                
                if new_files:
                    print(f"Found {len(new_files)} new files")
                    
                    # Process new files
                    results = self.process_files_parallel(
                        list(new_files), 
                        processor_func,
                        use_processes=False  # Use threads for file monitoring
                    )
                    
                    # Mark files as processed
                    processed_files.update(new_files)
                    
                    print(f"Processed {len([r for r in results if r is not None])} files successfully")
                
                # Wait before next check
                self._stop_monitoring.wait(poll_interval)
                
        except KeyboardInterrupt:
            print("Monitoring stopped by user")
        finally:
            self._stop_monitoring.set()
    
    def _process_single_file(self, file_path: Path, processor_func: Callable) -> Any:
        """Process a single file with error handling."""
        try:
            return processor_func(file_path)
        except Exception as e:
            print(f"Error processing {file_path}: {e}")
            self.stats.errors += 1
            return None
    
    def _start_monitoring(self):
        """Start performance monitoring thread."""
        if self._monitor_thread is None or not self._monitor_thread.is_alive():
            self._stop_monitoring.clear()
            self._monitor_thread = threading.Thread(target=self._monitor_performance)
            self._monitor_thread.daemon = True
            self._monitor_thread.start()
    
    def _monitor_performance(self):
        """Monitor performance metrics."""
        while not self._stop_monitoring.is_set():
            try:
                current_memory = psutil.Process().memory_info().rss
                self.stats.peak_memory_usage = max(self.stats.peak_memory_usage, current_memory)
            except Exception:
                pass
            
            self._stop_monitoring.wait(0.1)
    
    def get_performance_stats(self) -> ProcessingStats:
        """Get current performance statistics."""
        return self.stats
    
    def reset_stats(self):
        """Reset performance statistics."""
        self.stats = ProcessingStats()

# Example usage functions
def example_text_processor(file_path: Path) -> Dict[str, Any]:
    """Example processor that counts words in text files."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return {
                'file': str(file_path),
                'word_count': len(words),
                'char_count': len(content),
                'line_count': content.count('\n') + 1
            }
    except Exception as e:
        return {'file': str(file_path), 'error': str(e)}

def example_data_transformer(data: bytes) -> str:
    """Example transformer for streaming pipeline."""
    # Convert bytes to string and uppercase
    try:
        return data.decode('utf-8').upper()
    except:
        return ""

def example_output_sink(data: str):
    """Example output sink for streaming pipeline."""
    # Just print the data (in real use, might write to file/database)
    print(f"Processed: {data[:50]}...")

# Usage example
if __name__ == "__main__":
    processor = HighPerformanceFileProcessor(max_workers=4)
    
    # Example: Process multiple files in parallel
    file_paths = [Path(f"file_{i}.txt") for i in range(10)]
    results = processor.process_files_parallel(file_paths, example_text_processor)
    
    # Print performance statistics
    stats = processor.get_performance_stats()
    print(f"Processed {stats.files_processed} files")
    print(f"Throughput: {stats.throughput_mbps:.2f} MB/s")
    print(f"Peak memory: {stats.peak_memory_usage / (1024*1024):.2f} MB")
```

## Hints

- Use multiprocessing for CPU-bound tasks and threading for I/O-bound tasks
- Implement memory mapping for very large files to avoid loading them entirely
- Consider using queue-based pipelines for streaming data processing
- Monitor memory usage and performance metrics

## Practice Cases

Your high-performance system should handle:
- Processing thousands of files efficiently
- Large files that don't fit in memory
- Real-time processing of incoming files
- Various compressed file formats

## Bonus Challenge

Create a distributed file processing system that can scale across multiple machines using message queues and load balancing!

Remember: High-performance systems require careful optimization of I/O, memory usage, and parallel processing!