# RESTful APIs with FastAPI - Practice 7

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Build RESTful APIs using FastAPI framework. Learn automatic API documentation, request/response models with Pydantic, authentication, validation, and async operations.

## Objectives

- Create FastAPI applications with automatic documentation
- Use Pydantic models for request/response validation
- Implement CRUD operations with proper HTTP methods
- Add authentication and authorization
- Handle async operations and database integration

## Your Tasks

1. **create_fastapi_app()** - Set up FastAPI with automatic docs
2. **implement_pydantic_models()** - Create data models with validation
3. **build_crud_endpoints()** - Implement full CRUD operations
4. **add_authentication()** - Add JWT authentication
5. **create_async_operations()** - Implement async database operations

## Example

```python
from fastapi import FastAPI, HTTPException, Depends, status, Query, Path, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, validator, Field
from typing import List, Optional, Dict, Any
from datetime import datetime, timedelta
import jwt
import bcrypt
import uuid
from enum import Enum
import asyncio
import aiofiles
import json

def create_fastapi_app():
    """Set up FastAPI application with automatic documentation."""
    print("=== Creating FastAPI Application ===")
    
    # Create FastAPI app with metadata
    app = FastAPI(
        title="Blog API",
        description="A complete RESTful API for a blog application",
        version="1.0.0",
        docs_url="/docs",  # Swagger UI
        redoc_url="/redoc",  # ReDoc
        openapi_url="/openapi.json"
    )
    
    # Configure CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:3000", "http://localhost:8080"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Global exception handler
    @app.exception_handler(HTTPException)
    async def http_exception_handler(request, exc):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "error": {
                    "message": exc.detail,
                    "status_code": exc.status_code,
                    "timestamp": datetime.utcnow().isoformat()
                }
            }
        )
    
    # Health check endpoint
    @app.get("/health", tags=["Health"])
    async def health_check():
        """Health check endpoint."""
        return {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "version": "1.0.0"
        }
    
    # Root endpoint
    @app.get("/", tags=["Root"])
    async def root():
        """Root endpoint with API information."""
        return {
            "message": "Welcome to Blog API",
            "version": "1.0.0",
            "docs_url": "/docs",
            "redoc_url": "/redoc",
            "endpoints": {
                "health": "/health",
                "posts": "/posts",
                "users": "/users",
                "auth": "/auth"
            }
        }
    
    print("FastAPI app created with:")
    print("✓ Automatic API documentation at /docs")
    print("✓ Alternative docs at /redoc")
    print("✓ CORS middleware configured")
    print("✓ Global exception handling")
    print("✓ Health check endpoint")
    
    return app

def implement_pydantic_models():
    """Create Pydantic models for request/response validation."""
    print("\\n=== Implementing Pydantic Models ===")
    
    # Enums for choices
    class PostStatus(str, Enum):
        draft = "draft"
        published = "published"
        archived = "archived"
    
    class UserRole(str, Enum):
        user = "user"
        admin = "admin"
        moderator = "moderator"
    
    # Base models
    class TimestampMixin(BaseModel):
        """Mixin for timestamp fields."""
        created_at: datetime = Field(default_factory=datetime.utcnow)
        updated_at: datetime = Field(default_factory=datetime.utcnow)
    
    # User models
    class UserBase(BaseModel):
        """Base user model."""
        username: str = Field(..., min_length=3, max_length=50, regex="^[a-zA-Z0-9_]+$")
        email: EmailStr
        full_name: Optional[str] = Field(None, max_length=100)
        bio: Optional[str] = Field(None, max_length=500)
        is_active: bool = True
        role: UserRole = UserRole.user
        
        @validator('username')
        def username_must_not_be_reserved(cls, v):
            reserved = ['admin', 'root', 'api', 'www']
            if v.lower() in reserved:
                raise ValueError('Username is reserved')
            return v
    
    class UserCreate(UserBase):
        """User creation model."""
        password: str = Field(..., min_length=8, max_length=100)
        
        @validator('password')
        def validate_password(cls, v):
            if not any(c.isupper() for c in v):
                raise ValueError('Password must contain at least one uppercase letter')
            if not any(c.islower() for c in v):
                raise ValueError('Password must contain at least one lowercase letter')
            if not any(c.isdigit() for c in v):
                raise ValueError('Password must contain at least one digit')
            return v
    
    class UserUpdate(BaseModel):
        """User update model."""
        full_name: Optional[str] = Field(None, max_length=100)
        bio: Optional[str] = Field(None, max_length=500)
        is_active: Optional[bool] = None
    
    class UserResponse(UserBase, TimestampMixin):
        """User response model."""
        id: str
        post_count: int = 0
        
        class Config:
            schema_extra = {
                "example": {
                    "id": "550e8400-e29b-41d4-a716-446655440000",
                    "username": "johndoe",
                    "email": "john@example.com",
                    "full_name": "John Doe",
                    "bio": "Software developer and blogger",
                    "is_active": True,
                    "role": "user",
                    "post_count": 5,
                    "created_at": "2024-01-15T10:30:00Z",
                    "updated_at": "2024-01-20T14:45:00Z"
                }
            }
    
    # Post models
    class PostBase(BaseModel):
        """Base post model."""
        title: str = Field(..., min_length=5, max_length=200)
        content: str = Field(..., min_length=10)
        excerpt: Optional[str] = Field(None, max_length=300)
        status: PostStatus = PostStatus.draft
        tags: List[str] = Field(default_factory=list, max_items=10)
        featured: bool = False
        
        @validator('tags')
        def validate_tags(cls, v):
            if v:
                # Remove duplicates and empty strings
                v = list(set(tag.strip().lower() for tag in v if tag.strip()))
                # Validate tag format
                for tag in v:
                    if not tag.replace('-', '').replace('_', '').isalnum():
                        raise ValueError(f'Invalid tag format: {tag}')
            return v
    
    class PostCreate(PostBase):
        """Post creation model."""
        pass
    
    class PostUpdate(BaseModel):
        """Post update model."""
        title: Optional[str] = Field(None, min_length=5, max_length=200)
        content: Optional[str] = Field(None, min_length=10)
        excerpt: Optional[str] = Field(None, max_length=300)
        status: Optional[PostStatus] = None
        tags: Optional[List[str]] = Field(None, max_items=10)
        featured: Optional[bool] = None
    
    class PostResponse(PostBase, TimestampMixin):
        """Post response model."""
        id: str
        author_id: str
        author: UserResponse
        slug: str
        views: int = 0
        likes: int = 0
        comment_count: int = 0
        
        class Config:
            schema_extra = {
                "example": {
                    "id": "550e8400-e29b-41d4-a716-446655440001",
                    "title": "Getting Started with FastAPI",
                    "content": "FastAPI is a modern, fast web framework...",
                    "excerpt": "Learn the basics of FastAPI",
                    "status": "published",
                    "tags": ["fastapi", "python", "api"],
                    "featured": True,
                    "author_id": "550e8400-e29b-41d4-a716-446655440000",
                    "slug": "getting-started-with-fastapi",
                    "views": 150,
                    "likes": 25,
                    "comment_count": 8,
                    "created_at": "2024-01-15T10:30:00Z",
                    "updated_at": "2024-01-20T14:45:00Z"
                }
            }
    
    # Comment models
    class CommentBase(BaseModel):
        """Base comment model."""
        content: str = Field(..., min_length=5, max_length=1000)
    
    class CommentCreate(CommentBase):
        """Comment creation model."""
        post_id: str
        parent_id: Optional[str] = None
    
    class CommentResponse(CommentBase, TimestampMixin):
        """Comment response model."""
        id: str
        post_id: str
        author_id: str
        author: UserResponse
        parent_id: Optional[str] = None
        replies: List['CommentResponse'] = []
        likes: int = 0
    
    # Update forward references
    CommentResponse.update_forward_refs()
    
    # Authentication models
    class Token(BaseModel):
        """Token response model."""
        access_token: str
        token_type: str = "bearer"
        expires_in: int
        refresh_token: str
    
    class TokenData(BaseModel):
        """Token data model."""
        user_id: Optional[str] = None
        username: Optional[str] = None
        role: Optional[str] = None
    
    class LoginRequest(BaseModel):
        """Login request model."""
        username: str
        password: str
    
    # Pagination models
    class PaginationParams(BaseModel):
        """Pagination parameters."""
        page: int = Field(1, ge=1, description="Page number")
        size: int = Field(10, ge=1, le=100, description="Page size")
        
        @property
        def offset(self) -> int:
            return (self.page - 1) * self.size
    
    class PaginatedResponse(BaseModel):
        """Paginated response model."""
        items: List[Any]
        total: int
        page: int
        size: int
        pages: int
        has_next: bool
        has_prev: bool
        
        @classmethod
        def create(cls, items: List[Any], total: int, page: int, size: int):
            pages = (total + size - 1) // size
            return cls(
                items=items,
                total=total,
                page=page,
                size=size,
                pages=pages,
                has_next=page < pages,
                has_prev=page > 1
            )
    
    # Error models
    class ErrorResponse(BaseModel):
        """Error response model."""
        error: Dict[str, Any]
        
        class Config:
            schema_extra = {
                "example": {
                    "error": {
                        "message": "Post not found",
                        "status_code": 404,
                        "timestamp": "2024-01-15T10:30:00Z"
                    }
                }
            }
    
    print("Pydantic models created:")
    print("✓ User models (Create, Update, Response)")
    print("✓ Post models with validation")
    print("✓ Comment models with nesting")
    print("✓ Authentication models")
    print("✓ Pagination models")
    print("✓ Error response models")
    print("✓ Enum types for choices")
    print("✓ Custom validators")
    
    return {
        'UserCreate': UserCreate,
        'UserResponse': UserResponse,
        'PostCreate': PostCreate,
        'PostResponse': PostResponse,
        'CommentCreate': CommentCreate,
        'CommentResponse': CommentResponse,
        'Token': Token,
        'PaginatedResponse': PaginatedResponse,
        'ErrorResponse': ErrorResponse
    }

def build_crud_endpoints():
    """Implement full CRUD operations with FastAPI."""
    print("\\n=== Building CRUD Endpoints ===")
    
    app = FastAPI(title="CRUD API Demo")
    
    # Mock database
    users_db = {}
    posts_db = {}
    comments_db = {}
    
    # Import models (in real app, these would be imported)
    from pydantic import BaseModel, Field
    from typing import List, Optional, Dict
    from datetime import datetime
    import uuid
    
    # Simplified models for demo
    class User(BaseModel):
        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        username: str
        email: str
        full_name: Optional[str] = None
        created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class UserCreate(BaseModel):
        username: str
        email: str
        full_name: Optional[str] = None
    
    class Post(BaseModel):
        id: str = Field(default_factory=lambda: str(uuid.uuid4()))
        title: str
        content: str
        author_id: str
        created_at: datetime = Field(default_factory=datetime.utcnow)
    
    class PostCreate(BaseModel):
        title: str
        content: str
    
    # User CRUD endpoints
    @app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED, tags=["Users"])
    async def create_user(user_data: UserCreate):
        """Create a new user."""
        user = User(**user_data.dict())
        users_db[user.id] = user
        return user
    
    @app.get("/users", response_model=List[User], tags=["Users"])
    async def get_users(
        skip: int = Query(0, ge=0, description="Number of users to skip"),
        limit: int = Query(10, ge=1, le=100, description="Number of users to return")
    ):
        """Get list of users with pagination."""
        users_list = list(users_db.values())
        return users_list[skip:skip + limit]
    
    @app.get("/users/{user_id}", response_model=User, tags=["Users"])
    async def get_user(user_id: str = Path(..., description="User ID")):
        """Get user by ID."""
        if user_id not in users_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return users_db[user_id]
    
    @app.put("/users/{user_id}", response_model=User, tags=["Users"])
    async def update_user(
        user_id: str = Path(..., description="User ID"),
        user_data: UserCreate = Body(..., description="Updated user data")
    ):
        """Update user by ID."""
        if user_id not in users_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        user = users_db[user_id]
        user_dict = user_data.dict(exclude_unset=True)
        for field, value in user_dict.items():
            setattr(user, field, value)
        
        return user
    
    @app.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Users"])
    async def delete_user(user_id: str = Path(..., description="User ID")):
        """Delete user by ID."""
        if user_id not in users_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        del users_db[user_id]
        # Also delete user's posts
        user_posts = [post_id for post_id, post in posts_db.items() if post.author_id == user_id]
        for post_id in user_posts:
            del posts_db[post_id]
    
    # Post CRUD endpoints
    @app.post("/posts", response_model=Post, status_code=status.HTTP_201_CREATED, tags=["Posts"])
    async def create_post(
        post_data: PostCreate,
        author_id: str = Query(..., description="Author user ID")
    ):
        """Create a new post."""
        if author_id not in users_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Author not found"
            )
        
        post = Post(**post_data.dict(), author_id=author_id)
        posts_db[post.id] = post
        return post
    
    @app.get("/posts", response_model=List[Post], tags=["Posts"])
    async def get_posts(
        skip: int = Query(0, ge=0),
        limit: int = Query(10, ge=1, le=100),
        author_id: Optional[str] = Query(None, description="Filter by author ID")
    ):
        """Get list of posts with optional filtering."""
        posts_list = list(posts_db.values())
        
        if author_id:
            posts_list = [post for post in posts_list if post.author_id == author_id]
        
        return posts_list[skip:skip + limit]
    
    @app.get("/posts/{post_id}", response_model=Post, tags=["Posts"])
    async def get_post(post_id: str = Path(..., description="Post ID")):
        """Get post by ID."""
        if post_id not in posts_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        return posts_db[post_id]
    
    @app.put("/posts/{post_id}", response_model=Post, tags=["Posts"])
    async def update_post(
        post_id: str = Path(..., description="Post ID"),
        post_data: PostCreate = Body(..., description="Updated post data")
    ):
        """Update post by ID."""
        if post_id not in posts_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        
        post = posts_db[post_id]
        post_dict = post_data.dict(exclude_unset=True)
        for field, value in post_dict.items():
            setattr(post, field, value)
        
        return post
    
    @app.delete("/posts/{post_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Posts"])
    async def delete_post(post_id: str = Path(..., description="Post ID")):
        """Delete post by ID."""
        if post_id not in posts_db:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Post not found"
            )
        del posts_db[post_id]
    
    # Bulk operations
    @app.post("/posts/bulk", response_model=List[Post], tags=["Posts"])
    async def create_bulk_posts(
        posts_data: List[PostCreate],
        author_id: str = Query(..., description="Author user ID")
    ):
        """Create multiple posts at once."""
        if author_id not in users_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Author not found"
            )
        
        created_posts = []
        for post_data in posts_data:
            post = Post(**post_data.dict(), author_id=author_id)
            posts_db[post.id] = post
            created_posts.append(post)
        
        return created_posts
    
    @app.delete("/posts/bulk", status_code=status.HTTP_204_NO_CONTENT, tags=["Posts"])
    async def delete_bulk_posts(post_ids: List[str] = Body(..., description="List of post IDs to delete")):
        """Delete multiple posts at once."""
        not_found = []
        for post_id in post_ids:
            if post_id not in posts_db:
                not_found.append(post_id)
            else:
                del posts_db[post_id]
        
        if not_found:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Posts not found: {not_found}"
            )
    
    # Search endpoint
    @app.get("/posts/search", response_model=List[Post], tags=["Posts"])
    async def search_posts(
        q: str = Query(..., min_length=3, description="Search query"),
        limit: int = Query(10, ge=1, le=100)
    ):
        """Search posts by title or content."""
        results = []
        for post in posts_db.values():
            if q.lower() in post.title.lower() or q.lower() in post.content.lower():
                results.append(post)
            
            if len(results) >= limit:
                break
        
        return results
    
    # Statistics endpoint
    @app.get("/stats", tags=["Statistics"])
    async def get_statistics():
        """Get API statistics."""
        return {
            "users_count": len(users_db),
            "posts_count": len(posts_db),
            "comments_count": len(comments_db),
            "endpoints": {
                "users": "/users",
                "posts": "/posts",
                "search": "/posts/search",
                "bulk_operations": "/posts/bulk"
            }
        }
    
    print("CRUD endpoints implemented:")
    print("✓ User CRUD (Create, Read, Update, Delete)")
    print("✓ Post CRUD with filtering")
    print("✓ Bulk operations")
    print("✓ Search functionality")
    print("✓ Path and query parameters")
    print("✓ Proper HTTP status codes")
    print("✓ Request/response models")
    print("✓ API documentation tags")
    
    return app

def add_authentication():
    """Add JWT authentication and authorization."""
    print("\\n=== Adding Authentication ===")
    
    app = FastAPI(title="Authenticated API")
    
    # Configuration
    SECRET_KEY = "your-secret-key-here"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_DAYS = 7
    
    # Security
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")
    security = HTTPBearer()
    
    # Mock user database
    users_db = {
        "admin": {
            "id": "1",
            "username": "admin",
            "email": "admin@example.com",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
            "role": "admin",
            "is_active": True
        },
        "user": {
            "id": "2",
            "username": "user",
            "email": "user@example.com",
            "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",  # secret
            "role": "user",
            "is_active": True
        }
    }
    
    # Models
    class User(BaseModel):
        id: str
        username: str
        email: str
        role: str
        is_active: bool
    
    class Token(BaseModel):
        access_token: str
        refresh_token: str
        token_type: str = "bearer"
        expires_in: int
    
    class TokenData(BaseModel):
        user_id: Optional[str] = None
        username: Optional[str] = None
        role: Optional[str] = None
    
    # Password utilities
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        """Verify password against hash."""
        return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    def get_password_hash(password: str) -> str:
        """Hash password."""
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    # JWT utilities
    def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
        """Create access token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        
        to_encode.update({"exp": expire, "type": "access"})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def create_refresh_token(data: dict, expires_delta: Optional[timedelta] = None):
        """Create refresh token."""
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(days=7)
        
        to_encode.update({"exp": expire, "type": "refresh"})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
    
    def verify_token(token: str) -> TokenData:
        """Verify and decode token."""
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            user_id: str = payload.get("sub")
            username: str = payload.get("username")
            role: str = payload.get("role")
            
            if user_id is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            
            return TokenData(user_id=user_id, username=username, role=role)
            
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    # Authentication functions
    def authenticate_user(username: str, password: str):
        """Authenticate user credentials."""
        user = users_db.get(username)
        if not user:
            return False
        if not verify_password(password, user["hashed_password"]):
            return False
        return user
    
    async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
        """Get current authenticated user."""
        token_data = verify_token(token)
        user = users_db.get(token_data.username)
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        if not user["is_active"]:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
        
        return User(**user)
    
    async def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
        """Get current active user."""
        if not current_user.is_active:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Inactive user"
            )
        return current_user
    
    async def get_admin_user(current_user: User = Depends(get_current_user)) -> User:
        """Get current admin user."""
        if current_user.role != "admin":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return current_user
    
    # Authentication endpoints
    @app.post("/auth/login", response_model=Token, tags=["Authentication"])
    async def login(form_data: OAuth2PasswordRequestForm = Depends()):
        """Login endpoint."""
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
        
        access_token = create_access_token(
            data={"sub": user["id"], "username": user["username"], "role": user["role"]},
            expires_delta=access_token_expires
        )
        
        refresh_token = create_refresh_token(
            data={"sub": user["id"], "username": user["username"]},
            expires_delta=refresh_token_expires
        )
        
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
        }
    
    @app.post("/auth/refresh", response_model=Token, tags=["Authentication"])
    async def refresh_token(refresh_token: str = Body(..., embed=True)):
        """Refresh access token."""
        try:
            payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
            
            if payload.get("type") != "refresh":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid token type"
                )
            
            username = payload.get("username")
            user = users_db.get(username)
            
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="User not found"
                )
            
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user["id"], "username": user["username"], "role": user["role"]},
                expires_delta=access_token_expires
            )
            
            return {
                "access_token": access_token,
                "refresh_token": refresh_token,  # Keep the same refresh token
                "token_type": "bearer",
                "expires_in": ACCESS_TOKEN_EXPIRE_MINUTES * 60
            }
            
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token has expired"
            )
        except jwt.JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
    
    @app.get("/auth/me", response_model=User, tags=["Authentication"])
    async def get_current_user_info(current_user: User = Depends(get_current_active_user)):
        """Get current user information."""
        return current_user
    
    # Protected endpoints
    @app.get("/protected", tags=["Protected"])
    async def protected_route(current_user: User = Depends(get_current_active_user)):
        """Protected endpoint requiring authentication."""
        return {"message": f"Hello {current_user.username}! This is a protected route."}
    
    @app.get("/admin-only", tags=["Protected"])
    async def admin_only_route(admin_user: User = Depends(get_admin_user)):
        """Admin-only endpoint."""
        return {"message": f"Hello admin {admin_user.username}! This is an admin-only route."}
    
    @app.get("/users/profile", response_model=User, tags=["Users"])
    async def get_user_profile(current_user: User = Depends(get_current_active_user)):
        """Get user profile."""
        return current_user
    
    @app.put("/users/profile", response_model=User, tags=["Users"])
    async def update_user_profile(
        email: str = Body(...),
        current_user: User = Depends(get_current_active_user)
    ):
        """Update user profile."""
        # Update user in database
        users_db[current_user.username]["email"] = email
        updated_user = users_db[current_user.username]
        
        return User(**updated_user)
    
    print("Authentication implemented:")
    print("✓ JWT access and refresh tokens")
    print("✓ Password hashing with bcrypt")
    print("✓ Login and refresh endpoints")
    print("✓ Protected routes with dependencies")
    print("✓ Role-based access control")
    print("✓ Current user information")
    print("✓ OAuth2 password flow")
    print("✓ Token expiration handling")
    
    return app

def create_async_operations():
    """Implement async database operations."""
    print("\\n=== Creating Async Operations ===")
    
    import asyncio
    import aiofiles
    import httpx
    from typing import AsyncGenerator
    
    app = FastAPI(title="Async API")
    
    # Mock async database
    class AsyncDatabase:
        def __init__(self):
            self.users = {}
            self.posts = {}
            self._connection_pool_size = 10
            self._current_connections = 0
        
        async def connect(self):
            """Simulate database connection."""
            await asyncio.sleep(0.1)  # Simulate connection time
            self._current_connections += 1
            print(f"Connected to database (connections: {self._current_connections})")
        
        async def disconnect(self):
            """Simulate database disconnection."""
            await asyncio.sleep(0.05)
            self._current_connections -= 1
            print(f"Disconnected from database (connections: {self._current_connections})")
        
        async def find_user(self, user_id: str):
            """Find user by ID."""
            await asyncio.sleep(0.1)  # Simulate database query
            return self.users.get(user_id)
        
        async def find_users(self, limit: int = 10, offset: int = 0):
            """Find multiple users."""
            await asyncio.sleep(0.2)  # Simulate database query
            users_list = list(self.users.values())
            return users_list[offset:offset + limit]
        
        async def create_user(self, user_data: dict):
            """Create new user."""
            await asyncio.sleep(0.15)  # Simulate database write
            user_id = str(uuid.uuid4())
            user = {"id": user_id, "created_at": datetime.utcnow(), **user_data}
            self.users[user_id] = user
            return user
        
        async def update_user(self, user_id: str, user_data: dict):
            """Update user."""
            await asyncio.sleep(0.15)
            if user_id in self.users:
                self.users[user_id].update(user_data)
                self.users[user_id]["updated_at"] = datetime.utcnow()
                return self.users[user_id]
            return None
        
        async def delete_user(self, user_id: str):
            """Delete user."""
            await asyncio.sleep(0.1)
            return self.users.pop(user_id, None)
    
    # Database instance
    db = AsyncDatabase()
    
    # Database dependency
    async def get_database():
        """Get database connection."""
        await db.connect()
        try:
            yield db
        finally:
            await db.disconnect()
    
    # Models
    class User(BaseModel):
        id: Optional[str] = None
        username: str
        email: str
        created_at: Optional[datetime] = None
        updated_at: Optional[datetime] = None
    
    class UserCreate(BaseModel):
        username: str
        email: str
    
    # Async endpoints
    @app.get("/async/users", response_model=List[User], tags=["Async Operations"])
    async def get_users_async(
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        database: AsyncDatabase = Depends(get_database)
    ):
        """Get users asynchronously."""
        users = await database.find_users(limit=limit, offset=offset)
        return users
    
    @app.get("/async/users/{user_id}", response_model=User, tags=["Async Operations"])
    async def get_user_async(
        user_id: str,
        database: AsyncDatabase = Depends(get_database)
    ):
        """Get user by ID asynchronously."""
        user = await database.find_user(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return user
    
    @app.post("/async/users", response_model=User, status_code=status.HTTP_201_CREATED, tags=["Async Operations"])
    async def create_user_async(
        user_data: UserCreate,
        database: AsyncDatabase = Depends(get_database)
    ):
        """Create user asynchronously."""
        user = await database.create_user(user_data.dict())
        return user
    
    # Async file operations
    @app.post("/async/upload", tags=["Async File Operations"])
    async def upload_file_async(content: str = Body(..., description="File content")):
        """Upload file asynchronously."""
        filename = f"upload_{uuid.uuid4()}.txt"
        
        async with aiofiles.open(filename, 'w') as f:
            await f.write(content)
        
        return {
            "message": "File uploaded successfully",
            "filename": filename,
            "size": len(content)
        }
    
    @app.get("/async/download/{filename}", tags=["Async File Operations"])
    async def download_file_async(filename: str):
        """Download file asynchronously."""
        try:
            async with aiofiles.open(filename, 'r') as f:
                content = await f.read()
            
            return {
                "filename": filename,
                "content": content,
                "size": len(content)
            }
        except FileNotFoundError:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="File not found"
            )
    
    # Async HTTP requests
    @app.get("/async/external/{url:path}", tags=["Async HTTP"])
    async def fetch_external_async(url: str):
        """Fetch data from external API asynchronously."""
        full_url = f"https://{url}"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(full_url, timeout=10.0)
                return {
                    "url": full_url,
                    "status_code": response.status_code,
                    "headers": dict(response.headers),
                    "content_length": len(response.content)
                }
            except httpx.RequestError as e:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Request failed: {str(e)}"
                )
    
    # Concurrent operations
    @app.get("/async/concurrent", tags=["Async Operations"])
    async def concurrent_operations():
        """Perform multiple async operations concurrently."""
        
        async def task_1():
            await asyncio.sleep(1)
            return {"task": "1", "result": "completed"}
        
        async def task_2():
            await asyncio.sleep(0.5)
            return {"task": "2", "result": "completed"}
        
        async def task_3():
            await asyncio.sleep(0.8)
            return {"task": "3", "result": "completed"}
        
        start_time = datetime.utcnow()
        
        # Run tasks concurrently
        results = await asyncio.gather(task_1(), task_2(), task_3())
        
        end_time = datetime.utcnow()
        duration = (end_time - start_time).total_seconds()
        
        return {
            "results": results,
            "duration_seconds": duration,
            "message": "All tasks completed concurrently"
        }
    
    # Streaming response
    @app.get("/async/stream", tags=["Async Streaming"])
    async def stream_data():
        """Stream data asynchronously."""
        
        async def generate_data() -> AsyncGenerator[str, None]:
            for i in range(10):
                await asyncio.sleep(0.1)  # Simulate processing time
                yield f"data: chunk {i + 1}\\n\\n"
        
        return generate_data()
    
    # Background tasks
    @app.post("/async/background-task", tags=["Background Tasks"])
    async def create_background_task():
        """Create a background task."""
        
        async def background_job():
            # Simulate long-running task
            await asyncio.sleep(5)
            print("Background task completed!")
        
        # Start background task
        asyncio.create_task(background_job())
        
        return {
            "message": "Background task started",
            "task_id": str(uuid.uuid4())
        }
    
    # Async context manager
    @app.get("/async/context", tags=["Async Operations"])
    async def async_context_example():
        """Example using async context manager."""
        
        class AsyncResource:
            async def __aenter__(self):
                await asyncio.sleep(0.1)  # Simulate resource acquisition
                print("Resource acquired")
                return self
            
            async def __aexit__(self, exc_type, exc_val, exc_tb):
                await asyncio.sleep(0.1)  # Simulate resource cleanup
                print("Resource released")
            
            async def process(self):
                await asyncio.sleep(0.2)
                return "Processing completed"
        
        async with AsyncResource() as resource:
            result = await resource.process()
        
        return {"result": result}
    
    print("Async operations implemented:")
    print("✓ Async database operations")
    print("✓ Async file I/O")
    print("✓ Async HTTP requests")
    print("✓ Concurrent task execution")
    print("✓ Streaming responses")
    print("✓ Background tasks")
    print("✓ Async context managers")
    print("✓ Database connection pooling")
    
    return app

# Main execution
if __name__ == "__main__":
    print("=== FastAPI RESTful API Development ===")
    
    print("\\n1. Creating FastAPI App:")
    basic_app = create_fastapi_app()
    
    print("\\n2. Implementing Pydantic Models:")
    models = implement_pydantic_models()
    
    print("\\n3. Building CRUD Endpoints:")
    crud_app = build_crud_endpoints()
    
    print("\\n4. Adding Authentication:")
    auth_app = add_authentication()
    
    print("\\n5. Creating Async Operations:")
    async_app = create_async_operations()
    
    print("\\n" + "="*60)
    print("=== FASTAPI DEVELOPMENT COMPLETE ===")
    print("✓ FastAPI app with automatic documentation")
    print("✓ Pydantic models with validation")
    print("✓ Complete CRUD operations")
    print("✓ JWT authentication and authorization")
    print("✓ Async database operations")
    print("✓ File handling and HTTP requests")
    print("✓ Background tasks and streaming")
    print("✓ Error handling and middleware")
    print("\\nTo run: uvicorn main:app --reload")
    print("Visit: http://localhost:8000/docs for API documentation")
```

## Hints

- Use `uvicorn main:app --reload` for development with auto-reload
- FastAPI automatically generates OpenAPI/Swagger documentation
- Use type hints everywhere for better validation and docs
- Implement proper error handling with HTTPException
- Use dependency injection for database connections and auth

## Practice Cases

Your FastAPI application should:

- Generate automatic API documentation at `/docs`
- Validate request/response data with Pydantic models
- Handle CRUD operations with proper HTTP status codes
- Implement JWT authentication correctly
- Support async operations efficiently

## Bonus Challenge

Add database integration with SQLAlchemy, implement WebSocket endpoints, add rate limiting, and deploy with Docker!