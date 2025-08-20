# Distributed Module Systems and Microservices - Practice 19

**Difficulty:** ⭐⭐⭐⭐ (Medium-Hard)

## Description

Design and implement distributed module systems that work across microservices architectures with service discovery, load balancing, and fault tolerance.

## Objectives

- Build distributed module loading systems
- Implement service discovery for modules
- Create fault-tolerant module communication
- Design scalable module distribution networks

## Your Tasks

1. **distributed_module_registry()** - Centralized module discovery service
2. **service_mesh_integration()** - Integrate with service mesh architectures
3. **load_balanced_module_access()** - Distribute module load across instances
4. **fault_tolerant_module_loading()** - Handle network failures gracefully
5. **cross_service_module_sharing()** - Share modules between microservices
6. **module_caching_layer()** - Distributed caching for module data
7. **real_time_module_synchronization()** - Keep modules in sync across services
8. **monitoring_and_observability()** - Track distributed module performance

## Example

```python
import asyncio
import aiohttp
import json
import hashlib
from typing import Dict, List, Optional, Any, Callable
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
import consul
import redis
from prometheus_client import Counter, Histogram, Gauge
import logging

# Metrics for monitoring
MODULE_REQUESTS = Counter('module_requests_total', 'Total module requests', ['module_name', 'service_name'])
MODULE_LOAD_TIME = Histogram('module_load_duration_seconds', 'Module load time')
ACTIVE_MODULES = Gauge('active_modules_count', 'Number of active modules')

@dataclass
class ModuleMetadata:
    """Metadata for distributed modules."""
    name: str
    version: str
    service_url: str
    checksum: str
    size_bytes: int
    dependencies: List[str]
    tags: List[str]
    health_check_url: str
    last_updated: datetime
    load_balancer_weight: int = 100

@dataclass
class ServiceInstance:
    """Represents a service instance hosting modules."""
    service_id: str
    host: str
    port: int
    health_status: str
    modules: List[str]
    load: float
    last_heartbeat: datetime

class DistributedModuleRegistry:
    """Distributed registry for module discovery and management."""
    
    def __init__(self, consul_host='localhost', consul_port=8500, redis_host='localhost', redis_port=6379):
        self.consul = consul.Consul(host=consul_host, port=consul_port)
        self.redis = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
        self.local_cache: Dict[str, ModuleMetadata] = {}
        self.circuit_breaker_state: Dict[str, Dict] = {}
        self.retry_policies: Dict[str, int] = {}
        
    async def register_module(self, module: ModuleMetadata, service_instance: ServiceInstance):
        """Register a module with the distributed registry."""
        
        # Store in Consul for service discovery
        service_name = f"module-{module.name}"
        service_id = f"{service_name}-{service_instance.service_id}"
        
        await asyncio.get_event_loop().run_in_executor(
            None,
            self.consul.agent.service.register,
            service_name,
            service_id,
            address=service_instance.host,
            port=service_instance.port,
            tags=module.tags + [f"version:{module.version}"],
            check=consul.Check.http(module.health_check_url, interval="10s")
        )
        
        # Store metadata in Redis
        module_key = f"module:{module.name}:{module.version}"
        await asyncio.get_event_loop().run_in_executor(
            None,
            self.redis.hset,
            module_key,
            mapping=asdict(module)
        )
        
        # Update local cache
        self.local_cache[f"{module.name}:{module.version}"] = module
        
        ACTIVE_MODULES.inc()
        logging.info(f"Registered module {module.name}:{module.version} at {service_instance.host}:{service_instance.port}")
    
    async def discover_modules(self, module_name: str, version_constraint: str = None) -> List[ModuleMetadata]:
        """Discover available modules matching criteria."""
        
        # First check local cache
        cached_modules = [
            module for key, module in self.local_cache.items()
            if module.name == module_name and (not version_constraint or self._version_matches(module.version, version_constraint))
        ]
        
        if cached_modules:
            return cached_modules
        
        # Query Consul for services
        service_name = f"module-{module_name}"
        try:
            _, services = await asyncio.get_event_loop().run_in_executor(
                None,
                self.consul.health.service,
                service_name,
                passing=True
            )
            
            modules = []
            for service in services:
                # Get module metadata from Redis
                version = None
                for tag in service['Service']['Tags']:
                    if tag.startswith('version:'):
                        version = tag.split(':', 1)[1]
                        break
                
                if version:
                    module_key = f"module:{module_name}:{version}"
                    metadata = await asyncio.get_event_loop().run_in_executor(
                        None,
                        self.redis.hgetall,
                        module_key
                    )
                    
                    if metadata:
                        module = ModuleMetadata(**metadata)
                        modules.append(module)
                        # Update local cache
                        self.local_cache[f"{module.name}:{module.version}"] = module
            
            return modules
            
        except Exception as e:
            logging.error(f"Failed to discover modules: {e}")
            return []
    
    def _version_matches(self, version: str, constraint: str) -> bool:
        """Check if version matches constraint (simplified)."""
        if not constraint:
            return True
        # Implement semver matching logic
        return version == constraint  # Simplified for example

class LoadBalancedModuleClient:
    """Client for accessing modules with load balancing and fault tolerance."""
    
    def __init__(self, registry: DistributedModuleRegistry):
        self.registry = registry
        self.session: Optional[aiohttp.ClientSession] = None
        self.circuit_breakers: Dict[str, Dict] = {}
        self.retry_counts: Dict[str, int] = {}
        
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def call_module_function(self, 
                                 module_name: str, 
                                 function_name: str, 
                                 args: List = None, 
                                 kwargs: Dict = None,
                                 timeout: float = 30.0) -> Any:
        """Call a function on a distributed module with load balancing."""
        
        MODULE_REQUESTS.labels(module_name=module_name, service_name='unknown').inc()
        
        with MODULE_LOAD_TIME.time():
            # Discover available module instances
            modules = await self.registry.discover_modules(module_name)
            if not modules:
                raise RuntimeError(f"No instances of module {module_name} found")
            
            # Select instance using load balancing
            selected_module = self._select_instance(modules)
            
            # Check circuit breaker
            if self._is_circuit_open(selected_module.service_url):
                raise RuntimeError(f"Circuit breaker open for {selected_module.service_url}")
            
            try:
                # Make the remote call
                result = await self._make_remote_call(
                    selected_module, function_name, args or [], kwargs or {}, timeout
                )
                
                # Success - reset circuit breaker
                self._reset_circuit_breaker(selected_module.service_url)
                return result
                
            except Exception as e:
                # Handle failure
                self._record_failure(selected_module.service_url)
                
                # Try other instances if available
                remaining_modules = [m for m in modules if m != selected_module]
                for fallback_module in remaining_modules:
                    if not self._is_circuit_open(fallback_module.service_url):
                        try:
                            result = await self._make_remote_call(
                                fallback_module, function_name, args, kwargs, timeout
                            )
                            self._reset_circuit_breaker(fallback_module.service_url)
                            return result
                        except Exception:
                            self._record_failure(fallback_module.service_url)
                            continue
                
                raise RuntimeError(f"All instances of {module_name} failed: {e}")
    
    def _select_instance(self, modules: List[ModuleMetadata]) -> ModuleMetadata:
        """Select instance using weighted round-robin load balancing."""
        # For simplicity, just return the first healthy instance
        # In production, implement proper load balancing algorithm
        return modules[0]
    
    def _is_circuit_open(self, service_url: str) -> bool:
        """Check if circuit breaker is open for service."""
        if service_url not in self.circuit_breakers:
            return False
            
        breaker = self.circuit_breakers[service_url]
        if breaker['state'] == 'open':
            # Check if we should try half-open
            if datetime.now() > breaker['next_attempt']:
                breaker['state'] = 'half-open'
                return False
            return True
        
        return False
    
    def _record_failure(self, service_url: str):
        """Record a failure for circuit breaker logic."""
        if service_url not in self.circuit_breakers:
            self.circuit_breakers[service_url] = {
                'failure_count': 0,
                'state': 'closed',
                'next_attempt': None
            }
        
        breaker = self.circuit_breakers[service_url]
        breaker['failure_count'] += 1
        
        # Open circuit after 5 failures
        if breaker['failure_count'] >= 5:
            breaker['state'] = 'open'
            breaker['next_attempt'] = datetime.now() + timedelta(seconds=60)
            logging.warning(f"Circuit breaker opened for {service_url}")
    
    def _reset_circuit_breaker(self, service_url: str):
        """Reset circuit breaker on successful call."""
        if service_url in self.circuit_breakers:
            self.circuit_breakers[service_url] = {
                'failure_count': 0,
                'state': 'closed',
                'next_attempt': None
            }
    
    async def _make_remote_call(self, 
                              module: ModuleMetadata, 
                              function_name: str, 
                              args: List, 
                              kwargs: Dict,
                              timeout: float) -> Any:
        """Make the actual remote call to module service."""
        
        url = f"{module.service_url}/api/v1/modules/{module.name}/functions/{function_name}"
        
        payload = {
            'args': args,
            'kwargs': kwargs,
            'module_version': module.version
        }
        
        async with self.session.post(
            url, 
            json=payload, 
            timeout=aiohttp.ClientTimeout(total=timeout)
        ) as response:
            if response.status == 200:
                result = await response.json()
                return result['return_value']
            else:
                error_msg = await response.text()
                raise RuntimeError(f"Remote call failed: {response.status} - {error_msg}")

class ModuleCacheLayer:
    """Distributed caching layer for module data and results."""
    
    def __init__(self, redis_cluster_nodes: List[Dict]):
        import rediscluster
        self.redis_cluster = rediscluster.RedisCluster(
            startup_nodes=redis_cluster_nodes,
            decode_responses=True,
            skip_full_coverage_check=True
        )
        self.cache_stats = {
            'hits': 0,
            'misses': 0,
            'evictions': 0
        }
    
    async def get_cached_result(self, 
                              module_name: str, 
                              function_name: str, 
                              args_hash: str) -> Optional[Any]:
        """Get cached function result."""
        cache_key = f"result:{module_name}:{function_name}:{args_hash}"
        
        try:
            cached_data = await asyncio.get_event_loop().run_in_executor(
                None,
                self.redis_cluster.get,
                cache_key
            )
            
            if cached_data:
                self.cache_stats['hits'] += 1
                return json.loads(cached_data)
            else:
                self.cache_stats['misses'] += 1
                return None
                
        except Exception as e:
            logging.error(f"Cache get error: {e}")
            self.cache_stats['misses'] += 1
            return None
    
    async def cache_result(self, 
                         module_name: str, 
                         function_name: str, 
                         args_hash: str, 
                         result: Any,
                         ttl: int = 3600):
        """Cache function result."""
        cache_key = f"result:{module_name}:{function_name}:{args_hash}"
        
        try:
            await asyncio.get_event_loop().run_in_executor(
                None,
                self.redis_cluster.setex,
                cache_key,
                ttl,
                json.dumps(result)
            )
        except Exception as e:
            logging.error(f"Cache set error: {e}")
    
    def get_cache_stats(self) -> Dict:
        """Get cache performance statistics."""
        total_requests = self.cache_stats['hits'] + self.cache_stats['misses']
        hit_rate = self.cache_stats['hits'] / total_requests if total_requests > 0 else 0
        
        return {
            **self.cache_stats,
            'hit_rate': hit_rate,
            'total_requests': total_requests
        }
```

## Hints

- Use service discovery tools like Consul or etcd
- Implement circuit breaker patterns for fault tolerance
- Consider using message queues for asynchronous communication
- Design proper monitoring and alerting systems

## Practice Cases

Your distributed system should handle:
- Service discovery and registration
- Load balancing across multiple instances
- Network failures and service outages
- Cache coherency across distributed nodes
- Monitoring and observability requirements

## Bonus Challenge

Create a complete distributed module platform that can automatically scale, handle service mesh integration, and provide real-time monitoring dashboards!

Remember: Distributed systems require careful consideration of consistency, availability, and partition tolerance!