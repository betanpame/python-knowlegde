# HTTP Requests and API Integration - Test 2

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to work with HTTP requests and RESTful APIs using Python's requests library. Practice making GET, POST, PUT, and DELETE requests, handling responses, and working with JSON data.

## Objectives

- Make HTTP requests using the requests library
- Handle different HTTP methods (GET, POST, PUT, DELETE)
- Work with request headers and authentication
- Parse JSON responses and handle errors
- Implement basic API client functionality

## Your Tasks

1. **basic_http_requests()** - Make simple GET and POST requests
2. **handle_request_headers()** - Work with custom headers and authentication
3. **api_error_handling()** - Handle HTTP errors and exceptions
4. **json_data_processing()** - Parse and manipulate JSON responses
5. **build_api_client()** - Create a reusable API client class

## Example

```python
import requests
import json
from typing import Dict, Any, Optional
import time

def basic_http_requests():
    """Learn basic HTTP request methods."""
    
    print("=== Basic HTTP Requests ===")
    
    # Simple GET request
    print("\\n1. Simple GET Request:")
    try:
        response = requests.get('https://httpbin.org/get')
        print(f"Status Code: {response.status_code}")
        print(f"Response Headers: {dict(response.headers)}")
        print(f"Response Content: {response.json()}")
    except requests.RequestException as e:
        print(f"GET request failed: {e}")
    
    # GET request with parameters
    print("\\n2. GET Request with Parameters:")
    params = {
        'key1': 'value1',
        'key2': 'value2',
        'search': 'python programming'
    }
    
    try:
        response = requests.get('https://httpbin.org/get', params=params)
        print(f"Request URL: {response.url}")
        print(f"Parameters sent: {response.json()['args']}")
    except requests.RequestException as e:
        print(f"GET with params failed: {e}")
    
    # POST request with JSON data
    print("\\n3. POST Request with JSON:")
    data = {
        'name': 'John Doe',
        'email': 'john@example.com',
        'message': 'Hello from Python!'
    }
    
    try:
        response = requests.post('https://httpbin.org/post', json=data)
        print(f"Status Code: {response.status_code}")
        print(f"JSON data sent: {response.json()['json']}")
    except requests.RequestException as e:
        print(f"POST request failed: {e}")
    
    # POST request with form data
    print("\\n4. POST Request with Form Data:")
    form_data = {
        'username': 'testuser',
        'password': 'secretpassword'
    }
    
    try:
        response = requests.post('https://httpbin.org/post', data=form_data)
        print(f"Form data sent: {response.json()['form']}")
    except requests.RequestException as e:
        print(f"POST with form data failed: {e}")
    
    # PUT request
    print("\\n5. PUT Request:")
    update_data = {'status': 'updated', 'version': '2.0'}
    
    try:
        response = requests.put('https://httpbin.org/put', json=update_data)
        print(f"PUT Status: {response.status_code}")
        print(f"Updated data: {response.json()['json']}")
    except requests.RequestException as e:
        print(f"PUT request failed: {e}")
    
    # DELETE request
    print("\\n6. DELETE Request:")
    try:
        response = requests.delete('https://httpbin.org/delete')
        print(f"DELETE Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except requests.RequestException as e:
        print(f"DELETE request failed: {e}")
    
    return response.status_code if 'response' in locals() else None

def handle_request_headers():
    """Work with custom headers and authentication."""
    
    print("\\n=== Request Headers and Authentication ===")
    
    # Custom headers
    print("\\n1. Custom Headers:")
    headers = {
        'User-Agent': 'Python-Tutorial/1.0',
        'Accept': 'application/json',
        'X-Custom-Header': 'MyCustomValue'
    }
    
    try:
        response = requests.get('https://httpbin.org/headers', headers=headers)
        print(f"Headers sent: {response.json()['headers']}")
    except requests.RequestException as e:
        print(f"Headers request failed: {e}")
    
    # Basic authentication
    print("\\n2. Basic Authentication:")
    try:
        # httpbin provides a basic auth endpoint
        response = requests.get(
            'https://httpbin.org/basic-auth/user/pass',
            auth=('user', 'pass')
        )
        print(f"Auth Status: {response.status_code}")
        print(f"Auth Response: {response.json()}")
    except requests.RequestException as e:
        print(f"Basic auth failed: {e}")
    
    # Bearer token authentication
    print("\\n3. Bearer Token Authentication:")
    token_headers = {
        'Authorization': 'Bearer your-token-here',
        'Content-Type': 'application/json'
    }
    
    try:
        response = requests.get('https://httpbin.org/bearer', headers=token_headers)
        print(f"Bearer auth attempted")
        print(f"Status: {response.status_code}")
        if response.status_code == 401:
            print("Authentication failed (expected with dummy token)")
    except requests.RequestException as e:
        print(f"Bearer auth request failed: {e}")
    
    # Session with cookies
    print("\\n4. Session Management:")
    session = requests.Session()
    
    # Set cookies
    try:
        response = session.get('https://httpbin.org/cookies/set/session_id/abc123')
        print(f"Cookie set status: {response.status_code}")
        
        # Use cookies in subsequent request
        response = session.get('https://httpbin.org/cookies')
        print(f"Cookies received: {response.json()['cookies']}")
    except requests.RequestException as e:
        print(f"Session request failed: {e}")
    
    return headers, session

def api_error_handling():
    """Handle HTTP errors and exceptions properly."""
    
    print("\\n=== API Error Handling ===")
    
    # Handle different HTTP status codes
    test_urls = [
        ('https://httpbin.org/status/200', 'Success'),
        ('https://httpbin.org/status/404', 'Not Found'),
        ('https://httpbin.org/status/500', 'Server Error'),
        ('https://httpbin.org/delay/10', 'Timeout Test')  # Will timeout
    ]
    
    for url, description in test_urls:
        print(f"\\nTesting: {description}")
        try:
            response = requests.get(url, timeout=3)  # 3 second timeout
            
            # Check status code
            if response.status_code == 200:
                print(f"✓ Success: {response.status_code}")
            elif response.status_code == 404:
                print(f"⚠ Not Found: {response.status_code}")
            elif response.status_code >= 500:
                print(f"✗ Server Error: {response.status_code}")
            else:
                print(f"? Unexpected status: {response.status_code}")
            
            # Raise exception for bad status codes
            response.raise_for_status()
            
        except requests.exceptions.Timeout:
            print("✗ Request timed out")
        except requests.exceptions.HTTPError as e:
            print(f"✗ HTTP Error: {e}")
        except requests.exceptions.ConnectionError:
            print("✗ Connection error")
        except requests.exceptions.RequestException as e:
            print(f"✗ Request failed: {e}")
    
    # Retry mechanism
    print("\\n=== Retry Mechanism ===")
    
    def make_request_with_retry(url, max_retries=3, delay=1):
        """Make request with retry logic."""
        for attempt in range(max_retries):
            try:
                response = requests.get(url, timeout=5)
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                if attempt < max_retries - 1:
                    print(f"Retrying in {delay} seconds...")
                    time.sleep(delay)
                    delay *= 2  # Exponential backoff
                else:
                    print("All retry attempts failed")
                    raise
    
    # Test retry mechanism
    try:
        response = make_request_with_retry('https://httpbin.org/status/500')
    except requests.RequestException:
        print("Request failed after all retries")
    
    return True

def json_data_processing():
    """Parse and manipulate JSON responses."""
    
    print("\\n=== JSON Data Processing ===")
    
    # Get JSON data from API
    print("\\n1. Fetching JSON Data:")
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        posts = response.json()
        
        print(f"Total posts: {len(posts)}")
        print(f"First post: {posts[0]}")
        
        # Process JSON data
        print("\\n2. Processing JSON Data:")
        
        # Filter posts by user
        user_1_posts = [post for post in posts if post['userId'] == 1]
        print(f"Posts by user 1: {len(user_1_posts)}")
        
        # Extract titles
        titles = [post['title'] for post in posts[:5]]
        print(f"First 5 titles: {titles}")
        
        # Count posts per user
        user_post_counts = {}
        for post in posts:
            user_id = post['userId']
            user_post_counts[user_id] = user_post_counts.get(user_id, 0) + 1
        
        print(f"Posts per user: {user_post_counts}")
        
    except requests.RequestException as e:
        print(f"Failed to fetch posts: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON: {e}")
        return None
    
    # Send JSON data
    print("\\n3. Sending JSON Data:")
    new_post = {
        'title': 'My New Post',
        'body': 'This is the content of my new post.',
        'userId': 1
    }
    
    try:
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=new_post
        )
        
        print(f"POST Status: {response.status_code}")
        created_post = response.json()
        print(f"Created post ID: {created_post.get('id')}")
        print(f"Created post: {created_post}")
        
    except requests.RequestException as e:
        print(f"Failed to create post: {e}")
    
    # Work with nested JSON
    print("\\n4. Nested JSON Processing:")
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/users')
        users = response.json()
        
        # Extract nested data
        for user in users[:3]:
            print(f"\\nUser: {user['name']}")
            print(f"  Email: {user['email']}")
            print(f"  Address: {user['address']['city']}, {user['address']['zipcode']}")
            print(f"  Company: {user['company']['name']}")
            print(f"  Website: {user['website']}")
    
    except requests.RequestException as e:
        print(f"Failed to fetch users: {e}")
    
    return posts, users

def build_api_client():
    """Create a reusable API client class."""
    
    print("\\n=== Building API Client ===")
    
    class APIClient:
        """Generic API client with common functionality."""
        
        def __init__(self, base_url: str, timeout: int = 30):
            """Initialize API client."""
            self.base_url = base_url.rstrip('/')
            self.timeout = timeout
            self.session = requests.Session()
            self.default_headers = {
                'User-Agent': 'Python-API-Client/1.0',
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            }
            self.session.headers.update(self.default_headers)
        
        def set_auth_token(self, token: str):
            """Set bearer token for authentication."""
            self.session.headers['Authorization'] = f'Bearer {token}'
        
        def set_basic_auth(self, username: str, password: str):
            """Set basic authentication."""
            self.session.auth = (username, password)
        
        def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
            """Make HTTP request with error handling."""
            url = f"{self.base_url}/{endpoint.lstrip('/')}"
            
            try:
                response = self.session.request(
                    method=method,
                    url=url,
                    timeout=self.timeout,
                    **kwargs
                )
                response.raise_for_status()
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                raise
        
        def get(self, endpoint: str, params: Dict = None) -> Dict[str, Any]:
            """Make GET request."""
            response = self._make_request('GET', endpoint, params=params)
            return response.json()
        
        def post(self, endpoint: str, data: Dict = None) -> Dict[str, Any]:
            """Make POST request."""
            response = self._make_request('POST', endpoint, json=data)
            return response.json()
        
        def put(self, endpoint: str, data: Dict = None) -> Dict[str, Any]:
            """Make PUT request."""
            response = self._make_request('PUT', endpoint, json=data)
            return response.json()
        
        def delete(self, endpoint: str) -> bool:
            """Make DELETE request."""
            response = self._make_request('DELETE', endpoint)
            return response.status_code in [200, 204]
    
    class JSONPlaceholderClient(APIClient):
        """Specific client for JSONPlaceholder API."""
        
        def __init__(self):
            """Initialize JSONPlaceholder client."""
            super().__init__('https://jsonplaceholder.typicode.com')
        
        def get_posts(self, user_id: Optional[int] = None) -> List[Dict]:
            """Get all posts or posts by user."""
            params = {'userId': user_id} if user_id else None
            return self.get('/posts', params=params)
        
        def get_post(self, post_id: int) -> Dict[str, Any]:
            """Get specific post."""
            return self.get(f'/posts/{post_id}')
        
        def create_post(self, title: str, body: str, user_id: int) -> Dict[str, Any]:
            """Create new post."""
            data = {
                'title': title,
                'body': body,
                'userId': user_id
            }
            return self.post('/posts', data=data)
        
        def update_post(self, post_id: int, title: str, body: str, user_id: int) -> Dict[str, Any]:
            """Update existing post."""
            data = {
                'id': post_id,
                'title': title,
                'body': body,
                'userId': user_id
            }
            return self.put(f'/posts/{post_id}', data=data)
        
        def delete_post(self, post_id: int) -> bool:
            """Delete post."""
            return self.delete(f'/posts/{post_id}')
        
        def get_users(self) -> List[Dict]:
            """Get all users."""
            return self.get('/users')
        
        def get_user(self, user_id: int) -> Dict[str, Any]:
            """Get specific user."""
            return self.get(f'/users/{user_id}')
    
    # Test the API client
    print("\\n1. Testing Generic API Client:")
    try:
        client = JSONPlaceholderClient()
        
        # Get posts
        print("Fetching posts...")
        posts = client.get_posts()
        print(f"Total posts: {len(posts)}")
        
        # Get specific post
        print("\\nFetching specific post...")
        post = client.get_post(1)
        print(f"Post 1 title: {post['title']}")
        
        # Get posts by user
        print("\\nFetching posts by user 1...")
        user_posts = client.get_posts(user_id=1)
        print(f"User 1 posts: {len(user_posts)}")
        
        # Create new post
        print("\\nCreating new post...")
        new_post = client.create_post(
            title="Test Post from API Client",
            body="This post was created using our API client.",
            user_id=1
        )
        print(f"Created post ID: {new_post.get('id')}")
        
        # Update post
        print("\\nUpdating post...")
        updated_post = client.update_post(
            post_id=1,
            title="Updated Post Title",
            body="Updated post content.",
            user_id=1
        )
        print(f"Updated post title: {updated_post['title']}")
        
        # Delete post
        print("\\nDeleting post...")
        deleted = client.delete_post(1)
        print(f"Post deleted: {deleted}")
        
        # Get users
        print("\\nFetching users...")
        users = client.get_users()
        print(f"Total users: {len(users)}")
        
        user = client.get_user(1)
        print(f"User 1: {user['name']} ({user['email']})")
        
    except Exception as e:
        print(f"API client test failed: {e}")
    
    return APIClient, JSONPlaceholderClient

# Test all functions
if __name__ == "__main__":
    print("=== HTTP Requests and API Integration ===")
    
    print("\\n1. Basic HTTP Requests:")
    basic_results = basic_http_requests()
    
    print("\\n" + "="*50)
    print("2. Request Headers and Authentication:")
    header_results = handle_request_headers()
    
    print("\\n" + "="*50)
    print("3. API Error Handling:")
    error_results = api_error_handling()
    
    print("\\n" + "="*50)
    print("4. JSON Data Processing:")
    json_results = json_data_processing()
    
    print("\\n" + "="*50)
    print("5. Building API Client:")
    client_results = build_api_client()
    
    print("\\n=== HTTP Requests and APIs Complete! ===")
```

## Hints

- Always handle exceptions when making HTTP requests
- Use `response.raise_for_status()` to automatically raise exceptions for bad status codes
- Use sessions for multiple requests to the same API
- Set appropriate timeouts to avoid hanging requests
- Use JSON mode (`json=data`) for sending JSON data in POST requests

## Test Cases

Your functions should:

- Successfully make GET, POST, PUT, and DELETE requests
- Handle custom headers and authentication methods
- Properly catch and handle HTTP errors and timeouts
- Parse JSON responses and extract relevant data
- Create reusable API client classes with error handling

## Bonus Challenge

Add request caching, rate limiting, and automatic retry with exponential backoff to your API client!
