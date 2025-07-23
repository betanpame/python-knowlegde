# Django Framework Introduction - Test 6

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Introduction to Django web framework. Learn Django's MVT (Model-View-Template) architecture, URL routing, models with ORM, views, templates, and admin interface.

## Objectives

- Understand Django project structure and MVT pattern
- Create models with Django ORM
- Implement views and URL patterns
- Use Django templates and template inheritance
- Work with Django admin interface

## Your Tasks

1. **create_django_project()** - Set up Django project structure
2. **implement_models()** - Create Django models with relationships
3. **create_views_and_urls()** - Implement views and URL routing
4. **setup_templates()** - Create Django templates with inheritance
5. **configure_admin()** - Set up Django admin interface

## Example

```python
# Django Project Setup and Implementation
import os
import sys
from pathlib import Path
import subprocess

def create_django_project():
    """Set up Django project structure."""
    print("=== Creating Django Project ===")
    
    # Django project structure
    project_structure = {
        'myproject/': {
            'manage.py': '''#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
''',
            'myproject/': {
                '__init__.py': '',
                'settings.py': '''
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-demo-key-change-in-production'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',  # Our custom app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'myproject.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
''',
                'urls.py': '''
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
''',
                'wsgi.py': '''
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
application = get_wsgi_application()
''',
            }
        }
    }
    
    def create_files(structure, base_path=""):
        """Recursively create files and directories."""
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            
            if isinstance(content, dict):
                # It's a directory
                os.makedirs(path, exist_ok=True)
                create_files(content, path)
            else:
                # It's a file
                os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content.strip())
    
    # Create project structure
    create_files(project_structure)
    
    print("Django project structure created:")
    print("✓ myproject/ (main project directory)")
    print("✓ manage.py (Django management script)")
    print("✓ myproject/settings.py (project settings)")
    print("✓ myproject/urls.py (URL configuration)")
    print("✓ myproject/wsgi.py (WSGI configuration)")
    
    return project_structure

def implement_models():
    """Create Django models with relationships."""
    print("\\n=== Implementing Django Models ===")
    
    # Blog app structure
    blog_app = {
        'blog/': {
            '__init__.py': '',
            'apps.py': '''
from django.apps import AppConfig

class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
''',
            'models.py': '''
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify

class Category(models.Model):
    """Blog category model."""
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'slug': self.slug})

class Tag(models.Model):
    """Blog tag model."""
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    """Blog post model."""
    
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    
    content = models.TextField()
    excerpt = models.TextField(max_length=300, blank=True)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)
    
    views = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['-created_at']),
            models.Index(fields=['status']),
            models.Index(fields=['featured']),
        ]
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        
        # Set published_at when status changes to published
        if self.status == 'published' and not self.published_at:
            self.published_at = timezone.now()
        
        # Generate excerpt if not provided
        if not self.excerpt and self.content:
            self.excerpt = self.content[:300] + '...' if len(self.content) > 300 else self.content
        
        super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})
    
    @property
    def is_published(self):
        return self.status == 'published'
    
    def increment_views(self):
        """Increment view count."""
        self.views += 1
        self.save(update_fields=['views'])

class Comment(models.Model):
    """Blog comment model."""
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_approved = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'
    
    @property
    def is_reply(self):
        return self.parent is not None

class UserProfile(models.Model):
    """Extended user profile."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    website = models.URLField(blank=True)
    
    # Social media links
    twitter = models.CharField(max_length=50, blank=True)
    github = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def get_absolute_url(self):
        return reverse('blog:profile_detail', kwargs={'username': self.user.username})

# Signal to create user profile automatically
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
''',
            'admin.py': '''
from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Tag, Post, Comment, UserProfile

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'post_count', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']
    
    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = 'Posts'

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'post_count']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    
    def post_count(self, obj):
        return obj.post_set.count()
    post_count.short_description = 'Posts'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'featured', 'views', 'created_at']
    list_filter = ['status', 'featured', 'category', 'created_at', 'author']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content', 'excerpt')
        }),
        ('Metadata', {
            'fields': ('tags', 'status', 'featured')
        }),
        ('Statistics', {
            'fields': ('views',),
            'classes': ('collapse',)
        })
    )
    
    filter_horizontal = ['tags']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author', 'category')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'content_preview', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at', 'post']
    search_fields = ['content', 'author__username', 'post__title']
    
    def content_preview(self, obj):
        return obj.content[:50] + '...' if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'website', 'created_at']
    search_fields = ['user__username', 'user__email', 'bio']
    list_filter = ['created_at']
''',
            'migrations/': {
                '__init__.py': ''
            }
        }
    }
    
    def create_files(structure, base_path=""):
        """Recursively create files and directories."""
        for name, content in structure.items():
            path = os.path.join(base_path, name)
            
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_files(content, path)
            else:
                os.makedirs(os.path.dirname(path) if os.path.dirname(path) else ".", exist_ok=True)
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content.strip())
    
    create_files(blog_app)
    
    print("Django models implemented:")
    print("✓ Category model with slug generation")
    print("✓ Tag model for post tagging")
    print("✓ Post model with status, views, and relationships")
    print("✓ Comment model with reply functionality")
    print("✓ UserProfile model extending User")
    print("✓ Model relationships (ForeignKey, ManyToMany, OneToOne)")
    print("✓ Django admin configuration")
    
    return blog_app

def create_views_and_urls():
    """Implement views and URL routing."""
    print("\\n=== Creating Views and URLs ===")
    
    views_content = '''
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Category, Tag, Comment, UserProfile
from .forms import PostForm, CommentForm, UserProfileForm
from django.contrib.auth.models import User

# Function-based views
def home(request):
    """Home page with featured and recent posts."""
    featured_posts = Post.objects.filter(status='published', featured=True)[:3]
    recent_posts = Post.objects.filter(status='published').exclude(featured=True)[:6]
    categories = Category.objects.annotate(post_count=Count('post')).filter(post_count__gt=0)[:5]
    
    context = {
        'featured_posts': featured_posts,
        'recent_posts': recent_posts,
        'categories': categories,
    }
    return render(request, 'blog/home.html', context)

def post_list(request):
    """List all published posts with pagination."""
    posts = Post.objects.filter(status='published').select_related('author', 'category')
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        posts = posts.filter(
            Q(title__icontains=search_query) |
            Q(content__icontains=search_query) |
            Q(author__username__icontains=search_query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        posts = posts.filter(category__slug=category_slug)
    
    # Tag filter
    tag_slug = request.GET.get('tag')
    if tag_slug:
        posts = posts.filter(tags__slug=tag_slug)
    
    # Pagination
    paginator = Paginator(posts, 6)  # 6 posts per page
    page = request.GET.get('page')
    
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    context = {
        'posts': posts,
        'search_query': search_query,
        'category_slug': category_slug,
        'tag_slug': tag_slug,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    """Post detail view with comments."""
    post = get_object_or_404(Post, slug=slug, status='published')
    
    # Increment view count
    post.increment_views()
    
    # Get comments
    comments = post.comments.filter(is_approved=True, parent=None).select_related('author')
    
    # Comment form
    comment_form = CommentForm()
    
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            
            # Handle reply
            parent_id = request.POST.get('parent_id')
            if parent_id:
                comment.parent = get_object_or_404(Comment, id=parent_id)
            
            comment.save()
            messages.success(request, 'Your comment has been added!')
            return redirect('blog:post_detail', slug=post.slug)
    
    # Related posts
    related_posts = Post.objects.filter(
        status='published',
        category=post.category
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'related_posts': related_posts,
    }
    return render(request, 'blog/post_detail.html', context)

def category_detail(request, slug):
    """Category detail view."""
    category = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=category, status='published')
    
    # Pagination
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    
    context = {
        'category': category,
        'posts': posts,
    }
    return render(request, 'blog/category_detail.html', context)

@login_required
def create_post(request):
    """Create new post (login required)."""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()  # Save many-to-many relationships
            
            messages.success(request, 'Post created successfully!')
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {'form': form})

# Class-based views
class PostListView(ListView):
    """Class-based view for post listing."""
    model = Post
    template_name = 'blog/post_list_cbv.html'
    context_object_name = 'posts'
    paginate_by = 6
    
    def get_queryset(self):
        return Post.objects.filter(status='published').select_related('author', 'category')

class PostDetailView(DetailView):
    """Class-based view for post detail."""
    model = Post
    template_name = 'blog/post_detail_cbv.html'
    context_object_name = 'post'
    slug_field = 'slug'
    
    def get_queryset(self):
        return Post.objects.filter(status='published')
    
    def get_object(self):
        obj = super().get_object()
        obj.increment_views()
        return obj

class PostCreateView(LoginRequiredMixin, CreateView):
    """Class-based view for creating posts."""
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post_cbv.html'
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post created successfully!')
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UpdateView):
    """Class-based view for updating posts."""
    model = Post
    form_class = PostForm
    template_name = 'blog/update_post.html'
    
    def get_queryset(self):
        # Users can only edit their own posts
        return Post.objects.filter(author=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, 'Post updated successfully!')
        return super().form_valid(form)

# API views
def api_posts(request):
    """API endpoint for posts."""
    posts = Post.objects.filter(status='published').values(
        'id', 'title', 'slug', 'author__username', 'created_at', 'views'
    )[:10]
    
    return JsonResponse({
        'posts': list(posts),
        'count': len(posts)
    })

def search_api(request):
    """Search API endpoint."""
    query = request.GET.get('q', '')
    
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query),
            status='published'
        ).values('title', 'slug')[:5]
        
        return JsonResponse({
            'results': list(posts),
            'query': query
        })
    
    return JsonResponse({'results': [], 'query': ''})
'''
    
    urls_content = '''
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Function-based views
    path('', views.home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('create/', views.create_post, name='create_post'),
    
    # Class-based views
    path('posts/cbv/', views.PostListView.as_view(), name='post_list_cbv'),
    path('post/cbv/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail_cbv'),
    path('create/cbv/', views.PostCreateView.as_view(), name='create_post_cbv'),
    path('edit/<slug:slug>/', views.PostUpdateView.as_view(), name='update_post'),
    
    # API endpoints
    path('api/posts/', views.api_posts, name='api_posts'),
    path('api/search/', views.search_api, name='search_api'),
]
'''
    
    forms_content = '''
from django import forms
from .models import Post, Comment, UserProfile, Category, Tag

class PostForm(forms.ModelForm):
    """Form for creating and editing posts."""
    
    class Meta:
        model = Post
        fields = ['title', 'category', 'tags', 'content', 'excerpt', 'status', 'featured']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter post title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 10,
                'placeholder': 'Write your post content here...'
            }),
            'excerpt': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Brief excerpt of your post'
            }),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'tags': forms.CheckboxSelectMultiple(),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all()
        self.fields['tags'].queryset = Tag.objects.all()

class CommentForm(forms.ModelForm):
    """Form for adding comments."""
    
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Write your comment here...'
            })
        }

class UserProfileForm(forms.ModelForm):
    """Form for editing user profile."""
    
    class Meta:
        model = UserProfile
        fields = ['bio', 'location', 'birth_date', 'avatar', 'website', 'twitter', 'github', 'linkedin']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tell us about yourself...'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your location'
            }),
            'birth_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://yourwebsite.com'
            }),
            'twitter': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '@username'
            }),
            'github': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'github_username'
            }),
            'linkedin': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'linkedin_username'
            })
        }

class SearchForm(forms.Form):
    """Search form."""
    query = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Search posts...',
            'type': 'search'
        })
    )
'''
    
    # Create files
    files = {
        'blog/views.py': views_content,
        'blog/urls.py': urls_content,
        'blog/forms.py': forms_content,
    }
    
    for filepath, content in files.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip())
    
    print("Views and URLs implemented:")
    print("✓ Function-based views (home, post_list, post_detail)")
    print("✓ Class-based views (ListView, DetailView, CreateView)")
    print("✓ URL patterns with named URLs")
    print("✓ Form handling and validation")
    print("✓ Pagination and search functionality")
    print("✓ API endpoints for JSON responses")
    
    return files

def setup_templates():
    """Create Django templates with inheritance."""
    print("\\n=== Setting up Django Templates ===")
    
    # Base template
    base_template = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Django Blog{% endblock %}</title>
    
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
    
    {% block extra_css %}{% endblock %}
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container">
            <a class="navbar-brand" href="{% url 'blog:home' %}">Django Blog</a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:home' %}">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="{% url 'blog:post_list' %}">Posts</a>
                    </li>
                </ul>
                
                <ul class="navbar-nav">
                    {% if user.is_authenticated %}
                        <li class="nav-item">
                            <a class="nav-link" href="{% url 'blog:create_post' %}">Write Post</a>
                        </li>
                        <li class="nav-item dropdown">
                            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown">
                                {{ user.username }}
                            </a>
                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="#">Profile</a></li>
                                <li><a class="dropdown-item" href="{% url 'admin:index' %}">Admin</a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><a class="dropdown-item" href="#">Logout</a></li>
                            </ul>
                        </li>
                    {% else %}
                        <li class="nav-item">
                            <a class="nav-link" href="#">Login</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Register</a>
                        </li>
                    {% endif %}
                </ul>
            </div>
        </div>
    </nav>
    
    <!-- Main content -->
    <main class="container my-4">
        <!-- Messages -->
        {% if messages %}
            {% for message in messages %}
                <div class="alert alert-{{ message.tags }} alert-dismissible fade show" role="alert">
                    {{ message }}
                    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
                </div>
            {% endfor %}
        {% endif %}
        
        {% block content %}{% endblock %}
    </main>
    
    <!-- Footer -->
    <footer class="bg-dark text-light py-4 mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-6">
                    <h5>Django Blog</h5>
                    <p>A modern blog built with Django.</p>
                </div>
                <div class="col-md-6 text-md-end">
                    <p>&copy; 2024 Django Blog. All rights reserved.</p>
                </div>
            </div>
        </div>
    </footer>
    
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    
    {% block extra_js %}{% endblock %}
</body>
</html>'''
    
    # Home template
    home_template = '''{% extends 'base.html' %}

{% block title %}Home - Django Blog{% endblock %}

{% block content %}
<!-- Hero section -->
<div class="row mb-5">
    <div class="col-12">
        <div class="bg-primary text-white p-5 rounded">
            <h1 class="display-4">Welcome to Django Blog</h1>
            <p class="lead">Discover amazing articles and share your thoughts with the community.</p>
            <a href="{% url 'blog:post_list' %}" class="btn btn-light btn-lg">Explore Posts</a>
        </div>
    </div>
</div>

<!-- Featured posts -->
{% if featured_posts %}
<div class="row mb-5">
    <div class="col-12">
        <h2 class="mb-4">Featured Posts</h2>
        <div class="row">
            {% for post in featured_posts %}
            <div class="col-md-4 mb-4">
                <div class="card h-100">
                    <div class="card-body">
                        <h5 class="card-title">
                            <a href="{{ post.get_absolute_url }}" class="text-decoration-none">
                                {{ post.title }}
                            </a>
                        </h5>
                        <p class="card-text">{{ post.excerpt }}</p>
                        <small class="text-muted">
                            By {{ post.author.username }} • {{ post.created_at|date:"M d, Y" }}
                        </small>
                    </div>
                    <div class="card-footer">
                        <a href="{{ post.get_absolute_url }}" class="btn btn-primary btn-sm">Read More</a>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>
{% endif %}

<!-- Recent posts -->
<div class="row">
    <div class="col-md-8">
        <h2 class="mb-4">Recent Posts</h2>
        {% for post in recent_posts %}
        <div class="card mb-3">
            <div class="card-body">
                <h5 class="card-title">
                    <a href="{{ post.get_absolute_url }}" class="text-decoration-none">
                        {{ post.title }}
                    </a>
                </h5>
                <p class="card-text">{{ post.excerpt }}</p>
                <small class="text-muted">
                    By {{ post.author.username }} in 
                    {% if post.category %}
                        <a href="{{ post.category.get_absolute_url }}">{{ post.category.name }}</a>
                    {% else %}
                        Uncategorized
                    {% endif %}
                    • {{ post.created_at|date:"M d, Y" }} • {{ post.views }} views
                </small>
            </div>
        </div>
        {% empty %}
        <p>No posts available yet.</p>
        {% endfor %}
    </div>
    
    <!-- Sidebar -->
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5>Categories</h5>
            </div>
            <div class="card-body">
                {% for category in categories %}
                <a href="{{ category.get_absolute_url }}" class="btn btn-outline-secondary btn-sm me-2 mb-2">
                    {{ category.name }} ({{ category.post_count }})
                </a>
                {% empty %}
                <p>No categories available.</p>
                {% endfor %}
            </div>
        </div>
    </div>
</div>
{% endblock %}'''
    
    # Post list template
    post_list_template = '''{% extends 'base.html' %}

{% block title %}Posts - Django Blog{% endblock %}

{% block content %}
<div class="row">
    <div class="col-md-8">
        <h1>All Posts</h1>
        
        <!-- Search form -->
        <form method="GET" class="mb-4">
            <div class="input-group">
                <input type="text" name="search" class="form-control" placeholder="Search posts..." value="{{ search_query }}">
                <button class="btn btn-outline-secondary" type="submit">Search</button>
            </div>
        </form>
        
        <!-- Posts -->
        {% for post in posts %}
        <article class="card mb-4">
            <div class="card-body">
                <h2 class="card-title h4">
                    <a href="{{ post.get_absolute_url }}" class="text-decoration-none">
                        {{ post.title }}
                    </a>
                </h2>
                
                <p class="card-text">{{ post.excerpt }}</p>
                
                <div class="d-flex justify-content-between align-items-center">
                    <small class="text-muted">
                        By {{ post.author.username }}
                        {% if post.category %}
                            in <a href="{{ post.category.get_absolute_url }}">{{ post.category.name }}</a>
                        {% endif %}
                        • {{ post.created_at|date:"M d, Y" }}
                        • {{ post.views }} views
                    </small>
                    
                    <a href="{{ post.get_absolute_url }}" class="btn btn-primary btn-sm">Read More</a>
                </div>
                
                <!-- Tags -->
                {% if post.tags.all %}
                <div class="mt-2">
                    {% for tag in post.tags.all %}
                    <span class="badge bg-secondary me-1">{{ tag.name }}</span>
                    {% endfor %}
                </div>
                {% endif %}
            </div>
        </article>
        {% empty %}
        <div class="alert alert-info">
            No posts found.
        </div>
        {% endfor %}
        
        <!-- Pagination -->
        {% if posts.has_other_pages %}
        <nav aria-label="Posts pagination">
            <ul class="pagination justify-content-center">
                {% if posts.has_previous %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ posts.previous_page_number }}{% if search_query %}&search={{ search_query }}{% endif %}">Previous</a>
                </li>
                {% endif %}
                
                {% for num in posts.paginator.page_range %}
                <li class="page-item {% if posts.number == num %}active{% endif %}">
                    <a class="page-link" href="?page={{ num }}{% if search_query %}&search={{ search_query }}{% endif %}">{{ num }}</a>
                </li>
                {% endfor %}
                
                {% if posts.has_next %}
                <li class="page-item">
                    <a class="page-link" href="?page={{ posts.next_page_number }}{% if search_query %}&search={{ search_query }}{% endif %}">Next</a>
                </li>
                {% endif %}
            </ul>
        </nav>
        {% endif %}
    </div>
    
    <!-- Sidebar -->
    <div class="col-md-4">
        <div class="card mb-4">
            <div class="card-header">
                <h5>Quick Stats</h5>
            </div>
            <div class="card-body">
                <p>Total Posts: <strong>{{ posts.paginator.count }}</strong></p>
                <p>Current Page: <strong>{{ posts.number }}</strong> of <strong>{{ posts.paginator.num_pages }}</strong></p>
            </div>
        </div>
    </div>
</div>
{% endblock %}'''
    
    # Create templates
    templates = {
        'templates/base.html': base_template,
        'templates/blog/home.html': home_template,
        'templates/blog/post_list.html': post_list_template,
    }
    
    for filepath, content in templates.items():
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content.strip())
    
    print("Django templates created:")
    print("✓ base.html (layout template)")
    print("✓ home.html (homepage)")
    print("✓ post_list.html (post listing)")
    print("✓ Template inheritance implemented")
    print("✓ Bootstrap styling included")
    print("✓ Navigation and footer")
    
    return templates

def configure_admin():
    """Configure Django admin interface."""
    print("\\n=== Configuring Django Admin ===")
    
    # Admin configuration is already in models.py, but let's show additional features
    admin_customization = '''
# Additional admin customization for blog/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from .models import Category, Tag, Post, Comment, UserProfile

# Customize admin site
admin.site.site_header = "Django Blog Administration"
admin.site.site_title = "Django Blog Admin"
admin.site.index_title = "Welcome to Django Blog Administration"

# Inline admin for UserProfile
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

# Extend User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'post_count')
    
    def post_count(self, obj):
        return obj.blog_posts.count()
    post_count.short_description = 'Posts'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Custom actions
@admin.action(description='Mark selected posts as published')
def make_published(modeladmin, request, queryset):
    queryset.update(status='published')

@admin.action(description='Mark selected posts as draft')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='draft')

# Enhanced Post admin
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ('author', 'created_at')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'status', 'featured', 'view_count', 'created_at']
    list_filter = ['status', 'featured', 'category', 'created_at', 'author']
    search_fields = ['title', 'content', 'author__username']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'
    actions = [make_published, make_draft]
    inlines = [CommentInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'category')
        }),
        ('Content', {
            'fields': ('content', 'excerpt')
        }),
        ('Metadata', {
            'fields': ('tags', 'status', 'featured')
        }),
        ('Statistics', {
            'fields': ('views',),
            'classes': ('collapse',)
        })
    )
    
    filter_horizontal = ['tags']
    
    def view_count(self, obj):
        return obj.views
    view_count.short_description = 'Views'
    view_count.admin_order_field = 'views'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('author', 'category').prefetch_related('tags')

# Management commands for the admin
# Save this as blog/management/commands/create_sample_data.py
sample_data_command = """
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Category, Tag, Post
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Create sample blog data'
    
    def handle(self, *args, **options):
        # Create categories
        categories = ['Technology', 'Programming', 'Web Development', 'Python', 'Django']
        for cat_name in categories:
            category, created = Category.objects.get_or_create(
                name=cat_name,
                defaults={'slug': slugify(cat_name), 'description': f'Posts about {cat_name}'}
            )
            if created:
                self.stdout.write(f'Created category: {cat_name}')
        
        # Create tags
        tags = ['python', 'django', 'web', 'tutorial', 'beginner', 'advanced', 'tips', 'guide']
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(
                name=tag_name,
                defaults={'slug': slugify(tag_name)}
            )
            if created:
                self.stdout.write(f'Created tag: {tag_name}')
        
        # Create sample posts
        if not User.objects.filter(username='admin').exists():
            admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Created admin user')
        else:
            admin_user = User.objects.get(username='admin')
        
        sample_posts = [
            {
                'title': 'Getting Started with Django',
                'content': 'Django is a high-level Python web framework...',
                'category': 'Django',
                'tags': ['python', 'django', 'tutorial'],
                'status': 'published'
            },
            {
                'title': 'Python Best Practices',
                'content': 'Here are some Python best practices...',
                'category': 'Python', 
                'tags': ['python', 'tips'],
                'status': 'published'
            }
        ]
        
        for post_data in sample_posts:
            category = Category.objects.get(name=post_data['category'])
            post, created = Post.objects.get_or_create(
                title=post_data['title'],
                defaults={
                    'content': post_data['content'],
                    'author': admin_user,
                    'category': category,
                    'status': post_data['status'],
                    'slug': slugify(post_data['title'])
                }
            )
            
            if created:
                # Add tags
                for tag_name in post_data['tags']:
                    tag = Tag.objects.get(name=tag_name)
                    post.tags.add(tag)
                
                self.stdout.write(f'Created post: {post_data["title"]}')
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
"""
    
    # Create management command directory
    os.makedirs('blog/management/commands', exist_ok=True)
    
    # Create __init__.py files
    with open('blog/management/__init__.py', 'w') as f:
        f.write('')
    
    with open('blog/management/commands/__init__.py', 'w') as f:
        f.write('')
    
    # Create sample data command
    with open('blog/management/commands/create_sample_data.py', 'w') as f:
        f.write(sample_data_command.strip())
    
    print("Django admin configured:")
    print("✓ Custom admin site header and title")
    print("✓ Enhanced User admin with profile inline")
    print("✓ Post admin with actions and inlines")
    print("✓ List displays, filters, and search")
    print("✓ Fieldsets and filter_horizontal")
    print("✓ Management command for sample data")
    
    print("\\nTo use the admin:")
    print("1. Run: python manage.py makemigrations")
    print("2. Run: python manage.py migrate")
    print("3. Run: python manage.py createsuperuser")
    print("4. Run: python manage.py create_sample_data")
    print("5. Run: python manage.py runserver")
    print("6. Visit: http://127.0.0.1:8000/admin/")
    
    return admin_customization

# Main execution
if __name__ == "__main__":
    print("=== Django Framework Development ===")
    
    print("\\n1. Creating Django Project:")
    project = create_django_project()
    
    print("\\n2. Implementing Models:")
    models = implement_models()
    
    print("\\n3. Creating Views and URLs:")
    views = create_views_and_urls()
    
    print("\\n4. Setting up Templates:")
    templates = setup_templates()
    
    print("\\n5. Configuring Admin:")
    admin_config = configure_admin()
    
    print("\\n" + "="*60)
    print("=== DJANGO DEVELOPMENT COMPLETE ===")
    print("✓ Django project structure")
    print("✓ Models with relationships and ORM")
    print("✓ Views (function-based and class-based)")
    print("✓ URL routing and named URLs")
    print("✓ Template inheritance and Bootstrap styling")
    print("✓ Django admin interface customization")
    print("✓ Forms and validation")
    print("✓ Management commands")
    print("\\nNext steps:")
    print("1. Install Django: pip install django")
    print("2. Navigate to project directory")
    print("3. Run migrations and create superuser")
    print("4. Start development server")
```

## Hints

- Use `python manage.py startproject` and `startapp` commands in real development
- Always run `makemigrations` and `migrate` after model changes
- Use Django's built-in User model or extend it with profiles
- Leverage Django admin for quick content management
- Follow Django's MVT pattern for organized code

## Test Cases

Your Django application should:

- Create models with proper relationships
- Handle URL routing correctly
- Render templates with template inheritance
- Process forms with validation
- Provide working admin interface

## Bonus Challenge

Add user authentication, implement REST API with Django REST framework, and deploy to production with proper settings!
