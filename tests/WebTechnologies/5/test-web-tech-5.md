# Flask Web Framework Basics - Test 5

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn Flask web framework fundamentals. Build web applications with routes, templates, forms, and basic database integration using SQLAlchemy.

## Objectives

- Create Flask applications with multiple routes
- Use Jinja2 templates for dynamic content
- Handle forms and user input
- Implement basic authentication
- Integrate databases with SQLAlchemy

## Your Tasks

1. **create_basic_flask_app()** - Set up Flask app with routes
2. **implement_templates()** - Use Jinja2 templating
3. **handle_forms()** - Process form submissions
4. **add_database_integration()** - Connect SQLAlchemy database
5. **build_todo_app()** - Create complete todo application

## Example

```python
from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

def create_basic_flask_app():
    """Set up Flask application with basic routes."""
    print("=== Creating Basic Flask Application ===")
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your-secret-key-here'
    
    # Basic routes
    @app.route('/')
    def home():
        """Home page."""
        return '''
        <h1>Welcome to Flask!</h1>
        <p>This is a basic Flask application.</p>
        <ul>
            <li><a href="/about">About</a></li>
            <li><a href="/contact">Contact</a></li>
            <li><a href="/api/users">API Demo</a></li>
        </ul>
        '''
    
    @app.route('/about')
    def about():
        """About page."""
        return '''
        <h1>About Us</h1>
        <p>This is the about page.</p>
        <a href="/">Back to Home</a>
        '''
    
    @app.route('/contact')
    def contact():
        """Contact page."""
        return '''
        <h1>Contact Us</h1>
        <p>Email: contact@example.com</p>
        <p>Phone: (555) 123-4567</p>
        <a href="/">Back to Home</a>
        '''
    
    # Route with parameters
    @app.route('/user/<string:username>')
    def user_profile(username):
        """User profile page."""
        return f'''
        <h1>User Profile</h1>
        <p>Username: {username}</p>
        <p>Welcome, {username.title()}!</p>
        <a href="/">Back to Home</a>
        '''
    
    # Route with multiple parameters
    @app.route('/post/<int:post_id>/<string:title>')
    def view_post(post_id, title):
        """View specific post."""
        return f'''
        <h1>Post #{post_id}: {title.replace('-', ' ').title()}</h1>
        <p>This is the content for post {post_id}.</p>
        <a href="/">Back to Home</a>
        '''
    
    # HTTP methods
    @app.route('/api/users', methods=['GET', 'POST'])
    def api_users():
        """API endpoint for users."""
        if request.method == 'GET':
            # Return list of users
            users = [
                {'id': 1, 'name': 'John Doe', 'email': 'john@example.com'},
                {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com'}
            ]
            return jsonify(users)
        
        elif request.method == 'POST':
            # Create new user
            data = request.get_json()
            new_user = {
                'id': 3,
                'name': data.get('name'),
                'email': data.get('email'),
                'created_at': datetime.now().isoformat()
            }
            return jsonify(new_user), 201
    
    # Error handlers
    @app.errorhandler(404)
    def not_found(error):
        """404 error handler."""
        return '''
        <h1>Page Not Found</h1>
        <p>The page you are looking for does not exist.</p>
        <a href="/">Back to Home</a>
        ''', 404
    
    @app.errorhandler(500)
    def internal_error(error):
        """500 error handler."""
        return '''
        <h1>Internal Server Error</h1>
        <p>Something went wrong on our end.</p>
        <a href="/">Back to Home</a>
        ''', 500
    
    # Context processor (makes variables available in all templates)
    @app.context_processor
    def inject_globals():
        """Inject global variables into templates."""
        return {
            'current_year': datetime.now().year,
            'app_name': 'Flask Demo App'
        }
    
    print("Flask app created with routes:")
    print("✓ / (home)")
    print("✓ /about")
    print("✓ /contact")
    print("✓ /user/<username>")
    print("✓ /post/<id>/<title>")
    print("✓ /api/users (GET, POST)")
    print("✓ Error handlers (404, 500)")
    
    return app

def implement_templates():
    """Use Jinja2 templating system."""
    print("\\n=== Implementing Jinja2 Templates ===")
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'template-demo-key'
    
    # Create templates directory
    templates_dir = os.path.join(os.getcwd(), 'templates')
    os.makedirs(templates_dir, exist_ok=True)
    
    # Base template
    base_template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ app_name }}{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; }
        .nav { background: #333; padding: 10px; margin-bottom: 20px; }
        .nav a { color: white; text-decoration: none; margin-right: 15px; }
        .nav a:hover { text-decoration: underline; }
        .alert { padding: 10px; margin: 10px 0; border-radius: 4px; }
        .alert-success { background: #d4edda; color: #155724; border: 1px solid #c3e6cb; }
        .alert-error { background: #f8d7da; color: #721c24; border: 1px solid #f5c6cb; }
        .footer { margin-top: 40px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; }
    </style>
</head>
<body>
    <div class="container">
        <nav class="nav">
            <a href="{{ url_for('home') }}">Home</a>
            <a href="{{ url_for('about') }}">About</a>
            <a href="{{ url_for('blog') }}">Blog</a>
            <a href="{{ url_for('contact') }}">Contact</a>
        </nav>
        
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
        
        <main>
            {% block content %}{% endblock %}
        </main>
        
        <footer class="footer">
            <p>&copy; {{ current_year }} {{ app_name }}. All rights reserved.</p>
        </footer>
    </div>
</body>
</html>
'''
    
    # Home template
    home_template = '''
{% extends "base.html" %}

{% block title %}Home - {{ super() }}{% endblock %}

{% block content %}
<h1>Welcome to {{ app_name }}!</h1>
<p>Current time: {{ current_time.strftime('%Y-%m-%d %H:%M:%S') }}</p>

<h2>Features</h2>
<ul>
    {% for feature in features %}
        <li>{{ feature }}</li>
    {% endfor %}
</ul>

<h2>Quick Stats</h2>
<div style="display: flex; gap: 20px;">
    {% for stat in stats %}
        <div style="border: 1px solid #ddd; padding: 10px; border-radius: 4px;">
            <h3>{{ stat.value }}</h3>
            <p>{{ stat.label }}</p>
        </div>
    {% endfor %}
</div>
{% endblock %}
'''
    
    # Blog template
    blog_template = '''
{% extends "base.html" %}

{% block title %}Blog - {{ super() }}{% endblock %}

{% block content %}
<h1>Blog Posts</h1>

{% if posts %}
    {% for post in posts %}
        <article style="border-bottom: 1px solid #eee; margin-bottom: 20px; padding-bottom: 20px;">
            <h2><a href="{{ url_for('view_post', post_id=post.id) }}">{{ post.title }}</a></h2>
            <p><small>Published on {{ post.date.strftime('%B %d, %Y') }} by {{ post.author }}</small></p>
            <p>{{ post.excerpt }}</p>
            <a href="{{ url_for('view_post', post_id=post.id) }}">Read more &rarr;</a>
        </article>
    {% endfor %}
{% else %}
    <p>No blog posts available yet.</p>
{% endif %}
{% endblock %}
'''
    
    # Post detail template
    post_template = '''
{% extends "base.html" %}

{% block title %}{{ post.title }} - {{ super() }}{% endblock %}

{% block content %}
<article>
    <h1>{{ post.title }}</h1>
    <p><small>Published on {{ post.date.strftime('%B %d, %Y') }} by {{ post.author }}</small></p>
    
    {% if post.tags %}
        <div style="margin: 10px 0;">
            Tags: 
            {% for tag in post.tags %}
                <span style="background: #f0f0f0; padding: 2px 6px; border-radius: 3px; margin-right: 5px;">{{ tag }}</span>
            {% endfor %}
        </div>
    {% endif %}
    
    <div style="margin-top: 20px;">
        {{ post.content | safe }}
    </div>
</article>

<div style="margin-top: 30px;">
    <a href="{{ url_for('blog') }}">&larr; Back to Blog</a>
</div>
{% endblock %}
'''
    
    # Save templates
    with open(os.path.join(templates_dir, 'base.html'), 'w') as f:
        f.write(base_template)
    
    with open(os.path.join(templates_dir, 'home.html'), 'w') as f:
        f.write(home_template)
    
    with open(os.path.join(templates_dir, 'blog.html'), 'w') as f:
        f.write(blog_template)
    
    with open(os.path.join(templates_dir, 'post.html'), 'w') as f:
        f.write(post_template)
    
    # Template routes
    @app.route('/')
    def home():
        """Home page with template."""
        return render_template('home.html',
            current_time=datetime.now(),
            features=[
                'Responsive Design',
                'Template Inheritance',
                'Flash Messages',
                'URL Generation'
            ],
            stats=[
                {'value': '100+', 'label': 'Happy Users'},
                {'value': '50+', 'label': 'Features'},
                {'value': '24/7', 'label': 'Support'}
            ]
        )
    
    @app.route('/about')
    def about():
        """About page."""
        return render_template('base.html'), 200
    
    @app.route('/blog')
    def blog():
        """Blog listing page."""
        # Sample blog posts
        posts = [
            {
                'id': 1,
                'title': 'Getting Started with Flask',
                'author': 'John Doe',
                'date': datetime(2024, 1, 15),
                'excerpt': 'Learn the basics of Flask web framework...'
            },
            {
                'id': 2,
                'title': 'Template Inheritance in Jinja2',
                'author': 'Jane Smith',
                'date': datetime(2024, 1, 20),
                'excerpt': 'Master template inheritance for cleaner code...'
            },
            {
                'id': 3,
                'title': 'Database Integration with SQLAlchemy',
                'author': 'Bob Wilson',
                'date': datetime(2024, 1, 25),
                'excerpt': 'Connect your Flask app to databases...'
            }
        ]
        
        return render_template('blog.html', posts=posts)
    
    @app.route('/post/<int:post_id>')
    def view_post(post_id):
        """View individual blog post."""
        # Sample post data
        posts_data = {
            1: {
                'id': 1,
                'title': 'Getting Started with Flask',
                'author': 'John Doe',
                'date': datetime(2024, 1, 15),
                'content': '''
                <p>Flask is a lightweight and flexible web framework for Python...</p>
                <h3>Installation</h3>
                <pre>pip install flask</pre>
                <h3>Hello World Example</h3>
                <pre>from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'</pre>
                ''',
                'tags': ['flask', 'python', 'web-development']
            },
            2: {
                'id': 2,
                'title': 'Template Inheritance in Jinja2',
                'author': 'Jane Smith',
                'date': datetime(2024, 1, 20),
                'content': '''
                <p>Template inheritance is a powerful feature in Jinja2...</p>
                <h3>Base Template</h3>
                <p>Create a base.html template with common elements...</p>
                ''',
                'tags': ['jinja2', 'templates', 'flask']
            }
        }
        
        post = posts_data.get(post_id)
        if not post:
            flash('Post not found!', 'error')
            return redirect(url_for('blog'))
        
        return render_template('post.html', post=post)
    
    @app.route('/contact')
    def contact():
        """Contact page."""
        flash('Contact form coming soon!', 'success')
        return redirect(url_for('home'))
    
    print("Templates created:")
    print("✓ base.html (layout template)")
    print("✓ home.html (extends base)")
    print("✓ blog.html (post listing)")
    print("✓ post.html (post detail)")
    print("✓ Template inheritance implemented")
    print("✓ Flash messages support")
    
    return app

def handle_forms():
    """Process form submissions with WTForms."""
    print("\\n=== Handling Forms with WTForms ===")
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'form-demo-key'
    
    # Form classes
    class ContactForm(FlaskForm):
        """Contact form."""
        name = StringField('Name', validators=[DataRequired(), Length(min=2, max=80)])
        email = StringField('Email', validators=[DataRequired(), Email()])
        subject = StringField('Subject', validators=[DataRequired(), Length(min=5, max=100)])
        message = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=500)])
        submit = SubmitField('Send Message')
    
    class RegistrationForm(FlaskForm):
        """User registration form."""
        username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
        email = StringField('Email', validators=[DataRequired(), Email()])
        password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
        password2 = PasswordField('Confirm Password', 
                                 validators=[DataRequired(), EqualTo('password')])
        accept_terms = BooleanField('I accept the terms and conditions', 
                                   validators=[DataRequired()])
        submit = SubmitField('Register')
    
    class LoginForm(FlaskForm):
        """User login form."""
        username = StringField('Username', validators=[DataRequired()])
        password = PasswordField('Password', validators=[DataRequired()])
        remember_me = BooleanField('Remember Me')
        submit = SubmitField('Sign In')
    
    # Create form templates
    contact_form_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Contact Form</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea, select { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .error { color: red; font-size: 14px; }
        .flash-messages { margin-bottom: 20px; }
        .alert { padding: 10px; border-radius: 4px; margin-bottom: 10px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    
    <div class="flash-messages">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
    </div>
    
    <form method="POST">
        {{ form.hidden_tag() }}
        
        <div class="form-group">
            {{ form.name.label }}
            {{ form.name() }}
            {% if form.name.errors %}
                {% for error in form.name.errors %}
                    <div class="error">{{ error }}</div>
                {% endfor %}
            {% endif %}
        </div>
        
        <div class="form-group">
            {{ form.email.label }}
            {{ form.email() }}
            {% if form.email.errors %}
                {% for error in form.email.errors %}
                    <div class="error">{{ error }}</div>
                {% endfor %}
            {% endif %}
        </div>
        
        <div class="form-group">
            {{ form.subject.label }}
            {{ form.subject() }}
            {% if form.subject.errors %}
                {% for error in form.subject.errors %}
                    <div class="error">{{ error }}</div>
                {% endfor %}
            {% endif %}
        </div>
        
        <div class="form-group">
            {{ form.message.label }}
            {{ form.message(rows=5) }}
            {% if form.message.errors %}
                {% for error in form.message.errors %}
                    <div class="error">{{ error }}</div>
                {% endfor %}
            {% endif %}
        </div>
        
        <div class="form-group">
            {{ form.submit() }}
        </div>
    </form>
    
    <p><a href="{{ url_for('form_demo') }}">Back to Forms Demo</a></p>
</body>
</html>
'''
    
    # Save contact form template
    os.makedirs('templates', exist_ok=True)
    with open('templates/contact_form.html', 'w') as f:
        f.write(contact_form_template)
    
    # Form routes
    @app.route('/')
    def form_demo():
        """Form demonstration page."""
        return '''
        <h1>Flask Forms Demo</h1>
        <ul>
            <li><a href="/contact">Contact Form</a></li>
            <li><a href="/register">Registration Form</a></li>
            <li><a href="/login">Login Form</a></li>
        </ul>
        '''
    
    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        """Contact form handler."""
        form = ContactForm()
        
        if form.validate_on_submit():
            # Process form data
            contact_data = {
                'name': form.name.data,
                'email': form.email.data,
                'subject': form.subject.data,
                'message': form.message.data,
                'timestamp': datetime.now().isoformat()
            }
            
            # In a real app, you would save to database or send email
            print(f"Contact form submitted: {contact_data}")
            
            flash(f'Thank you {form.name.data}! Your message has been sent.', 'success')
            return redirect(url_for('contact'))
        
        return render_template('contact_form.html', form=form)
    
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        """Registration form handler."""
        form = RegistrationForm()
        
        if form.validate_on_submit():
            # Check if username exists (mock check)
            existing_users = ['admin', 'test', 'demo']
            
            if form.username.data.lower() in existing_users:
                flash('Username already exists!', 'error')
                return render_template('register.html', form=form)
            
            # Create user (mock)
            user_data = {
                'username': form.username.data,
                'email': form.email.data,
                'password_hash': generate_password_hash(form.password.data),
                'created_at': datetime.now().isoformat()
            }
            
            print(f"User registered: {user_data}")
            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))
        
        return f'''
        <h1>Register</h1>
        <form method="POST">
            {form.hidden_tag()}
            <p>{form.username.label}: {form.username()}</p>
            <p>{form.email.label}: {form.email()}</p>
            <p>{form.password.label}: {form.password()}</p>
            <p>{form.password2.label}: {form.password2()}</p>
            <p>{form.accept_terms()} {form.accept_terms.label}</p>
            <p>{form.submit()}</p>
        </form>
        <a href="/">Back to Demo</a>
        '''
    
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        """Login form handler."""
        form = LoginForm()
        
        if form.validate_on_submit():
            # Mock authentication
            valid_users = {
                'admin': 'password123',
                'user': 'secret456'
            }
            
            username = form.username.data
            password = form.password.data
            
            if username in valid_users and valid_users[username] == password:
                session['username'] = username
                session['logged_in'] = True
                
                flash(f'Welcome back, {username}!', 'success')
                return redirect(url_for('dashboard'))
            else:
                flash('Invalid username or password!', 'error')
        
        return f'''
        <h1>Login</h1>
        <form method="POST">
            {form.hidden_tag()}
            <p>{form.username.label}: {form.username()}</p>
            <p>{form.password.label}: {form.password()}</p>
            <p>{form.remember_me()} {form.remember_me.label}</p>
            <p>{form.submit()}</p>
        </form>
        <a href="/">Back to Demo</a>
        '''
    
    @app.route('/dashboard')
    def dashboard():
        """User dashboard."""
        if not session.get('logged_in'):
            flash('Please log in to access the dashboard.', 'error')
            return redirect(url_for('login'))
        
        username = session.get('username')
        return f'''
        <h1>Dashboard</h1>
        <p>Welcome, {username}!</p>
        <p><a href="/logout">Logout</a></p>
        <p><a href="/">Back to Demo</a></p>
        '''
    
    @app.route('/logout')
    def logout():
        """Logout user."""
        session.clear()
        flash('You have been logged out.', 'success')
        return redirect(url_for('form_demo'))
    
    print("Forms implemented:")
    print("✓ ContactForm with validation")
    print("✓ RegistrationForm with password confirmation")
    print("✓ LoginForm with session management")
    print("✓ Form validation and error handling")
    print("✓ Flash messages for feedback")
    
    return app

def add_database_integration():
    """Integrate SQLAlchemy database."""
    print("\\n=== Database Integration with SQLAlchemy ===")
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'database-demo-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///demo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db = SQLAlchemy(app)
    
    # Database models
    class User(db.Model):
        """User model."""
        id = db.Column(db.Integer, primary_key=True)
        username = db.Column(db.String(80), unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        password_hash = db.Column(db.String(120), nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        posts = db.relationship('Post', backref='author', lazy=True)
        
        def __repr__(self):
            return f'<User {self.username}>'
    
    class Post(db.Model):
        """Post model."""
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        content = db.Column(db.Text, nullable=False)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
        
        def __repr__(self):
            return f'<Post {self.title}>'
    
    # Database routes
    @app.route('/')
    def index():
        """Home page with database stats."""
        user_count = User.query.count()
        post_count = Post.query.count()
        recent_posts = Post.query.order_by(Post.created_at.desc()).limit(5).all()
        
        return f'''
        <h1>Database Demo</h1>
        <p>Users: {user_count}</p>
        <p>Posts: {post_count}</p>
        
        <h3>Recent Posts:</h3>
        <ul>
        ''' + '\\n'.join([f'<li><a href="/post/{post.id}">{post.title}</a> by {post.author.username}</li>' 
                         for post in recent_posts]) + '''
        </ul>
        
        <p><a href="/users">View All Users</a></p>
        <p><a href="/create-user">Create User</a></p>
        <p><a href="/create-post">Create Post</a></p>
        '''
    
    @app.route('/users')
    def list_users():
        """List all users."""
        users = User.query.all()
        
        user_list = '\\n'.join([
            f'<li><a href="/user/{user.id}">{user.username}</a> ({user.email}) - {len(user.posts)} posts</li>'
            for user in users
        ])
        
        return f'''
        <h1>All Users</h1>
        <ul>{user_list}</ul>
        <p><a href="/">Back to Home</a></p>
        '''
    
    @app.route('/user/<int:user_id>')
    def view_user(user_id):
        """View user profile."""
        user = User.query.get_or_404(user_id)
        
        posts_list = '\\n'.join([
            f'<li><a href="/post/{post.id}">{post.title}</a> ({post.created_at.strftime("%Y-%m-%d")})</li>'
            for post in user.posts
        ])
        
        return f'''
        <h1>{user.username}</h1>
        <p>Email: {user.email}</p>
        <p>Joined: {user.created_at.strftime("%Y-%m-%d")}</p>
        <p>Posts: {len(user.posts)}</p>
        
        <h3>Posts by {user.username}:</h3>
        <ul>{posts_list}</ul>
        
        <p><a href="/users">Back to Users</a></p>
        '''
    
    @app.route('/post/<int:post_id>')
    def view_post(post_id):
        """View post."""
        post = Post.query.get_or_404(post_id)
        
        return f'''
        <h1>{post.title}</h1>
        <p>By: <a href="/user/{post.author.id}">{post.author.username}</a></p>
        <p>Posted: {post.created_at.strftime("%Y-%m-%d %H:%M")}</p>
        <div style="margin: 20px 0; padding: 20px; background: #f9f9f9;">
            {post.content.replace('\\n', '<br>')}
        </div>
        <p><a href="/">Back to Home</a></p>
        '''
    
    @app.route('/create-user', methods=['GET', 'POST'])
    def create_user():
        """Create new user."""
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            
            # Check if user exists
            if User.query.filter_by(username=username).first():
                return f'<p>Username already exists! <a href="/create-user">Try again</a></p>'
            
            if User.query.filter_by(email=email).first():
                return f'<p>Email already exists! <a href="/create-user">Try again</a></p>'
            
            # Create user
            user = User(
                username=username,
                email=email,
                password_hash=generate_password_hash(password)
            )
            
            db.session.add(user)
            db.session.commit()
            
            return f'<p>User {username} created successfully! <a href="/users">View users</a></p>'
        
        return '''
        <h1>Create User</h1>
        <form method="POST">
            <p><label>Username: <input type="text" name="username" required></label></p>
            <p><label>Email: <input type="email" name="email" required></label></p>
            <p><label>Password: <input type="password" name="password" required></label></p>
            <p><input type="submit" value="Create User"></p>
        </form>
        <p><a href="/">Back to Home</a></p>
        '''
    
    @app.route('/create-post', methods=['GET', 'POST'])
    def create_post():
        """Create new post."""
        if request.method == 'POST':
            title = request.form['title']
            content = request.form['content']
            user_id = request.form['user_id']
            
            # Validate user exists
            user = User.query.get(user_id)
            if not user:
                return f'<p>User not found! <a href="/create-post">Try again</a></p>'
            
            # Create post
            post = Post(
                title=title,
                content=content,
                user_id=user_id
            )
            
            db.session.add(post)
            db.session.commit()
            
            return f'<p>Post "{title}" created successfully! <a href="/post/{post.id}">View post</a></p>'
        
        # Get users for dropdown
        users = User.query.all()
        user_options = '\\n'.join([
            f'<option value="{user.id}">{user.username}</option>'
            for user in users
        ])
        
        return f'''
        <h1>Create Post</h1>
        <form method="POST">
            <p><label>Title: <input type="text" name="title" required></label></p>
            <p><label>Author: 
                <select name="user_id" required>
                    <option value="">Select user...</option>
                    {user_options}
                </select>
            </label></p>
            <p><label>Content: <textarea name="content" rows="5" required></textarea></label></p>
            <p><input type="submit" value="Create Post"></p>
        </form>
        <p><a href="/">Back to Home</a></p>
        '''
    
    # Initialize database
    with app.app_context():
        db.create_all()
        
        # Create sample data if empty
        if User.query.count() == 0:
            # Create sample users
            users_data = [
                {'username': 'alice', 'email': 'alice@example.com', 'password': 'password123'},
                {'username': 'bob', 'email': 'bob@example.com', 'password': 'password123'},
                {'username': 'charlie', 'email': 'charlie@example.com', 'password': 'password123'}
            ]
            
            for user_data in users_data:
                user = User(
                    username=user_data['username'],
                    email=user_data['email'],
                    password_hash=generate_password_hash(user_data['password'])
                )
                db.session.add(user)
            
            db.session.commit()
            
            # Create sample posts
            posts_data = [
                {'title': 'Welcome to Flask', 'content': 'This is my first Flask post!', 'user_id': 1},
                {'title': 'Database Integration', 'content': 'Learning SQLAlchemy is fun!', 'user_id': 2},
                {'title': 'Building Web Apps', 'content': 'Flask makes web development easy.', 'user_id': 1},
                {'title': 'Python Tips', 'content': 'Here are some useful Python tips...', 'user_id': 3}
            ]
            
            for post_data in posts_data:
                post = Post(**post_data)
                db.session.add(post)
            
            db.session.commit()
            
            print("Sample data created:")
            print("✓ 3 users")
            print("✓ 4 posts")
    
    print("Database integration complete:")
    print("✓ SQLAlchemy models (User, Post)")
    print("✓ Database relationships")
    print("✓ CRUD operations")
    print("✓ Sample data")
    
    return app, db

def build_todo_app():
    """Create complete todo application."""
    print("\\n=== Building Complete Todo Application ===")
    
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'todo-app-secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db = SQLAlchemy(app)
    
    # Todo model
    class Todo(db.Model):
        """Todo item model."""
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(100), nullable=False)
        description = db.Column(db.Text)
        completed = db.Column(db.Boolean, default=False)
        priority = db.Column(db.String(10), default='medium')  # low, medium, high
        due_date = db.Column(db.Date)
        created_at = db.Column(db.DateTime, default=datetime.utcnow)
        updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
        
        def __repr__(self):
            return f'<Todo {self.title}>'
    
    # Todo form
    class TodoForm(FlaskForm):
        """Todo creation/edit form."""
        title = StringField('Title', validators=[DataRequired(), Length(min=1, max=100)])
        description = TextAreaField('Description')
        priority = StringField('Priority', default='medium')
        due_date = StringField('Due Date (YYYY-MM-DD)')
        submit = SubmitField('Save Todo')
    
    # Routes
    @app.route('/')
    def index():
        """Todo list page."""
        # Get filter parameters
        filter_status = request.args.get('status', 'all')
        filter_priority = request.args.get('priority', 'all')
        
        # Build query
        query = Todo.query
        
        if filter_status == 'completed':
            query = query.filter_by(completed=True)
        elif filter_status == 'pending':
            query = query.filter_by(completed=False)
        
        if filter_priority != 'all':
            query = query.filter_by(priority=filter_priority)
        
        todos = query.order_by(Todo.created_at.desc()).all()
        
        # Stats
        total_todos = Todo.query.count()
        completed_todos = Todo.query.filter_by(completed=True).count()
        pending_todos = total_todos - completed_todos
        
        return render_template('todo_index.html',
                             todos=todos,
                             total_todos=total_todos,
                             completed_todos=completed_todos,
                             pending_todos=pending_todos,
                             filter_status=filter_status,
                             filter_priority=filter_priority)
    
    @app.route('/create', methods=['GET', 'POST'])
    def create_todo():
        """Create new todo."""
        form = TodoForm()
        
        if form.validate_on_submit():
            # Parse due date
            due_date = None
            if form.due_date.data:
                try:
                    due_date = datetime.strptime(form.due_date.data, '%Y-%m-%d').date()
                except ValueError:
                    flash('Invalid date format. Use YYYY-MM-DD.', 'error')
                    return render_template('todo_form.html', form=form, action='Create')
            
            # Create todo
            todo = Todo(
                title=form.title.data,
                description=form.description.data,
                priority=form.priority.data,
                due_date=due_date
            )
            
            db.session.add(todo)
            db.session.commit()
            
            flash(f'Todo "{todo.title}" created successfully!', 'success')
            return redirect(url_for('index'))
        
        return render_template('todo_form.html', form=form, action='Create')
    
    @app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
    def edit_todo(todo_id):
        """Edit existing todo."""
        todo = Todo.query.get_or_404(todo_id)
        form = TodoForm(obj=todo)
        
        if form.validate_on_submit():
            # Parse due date
            due_date = None
            if form.due_date.data:
                try:
                    due_date = datetime.strptime(form.due_date.data, '%Y-%m-%d').date()
                except ValueError:
                    flash('Invalid date format. Use YYYY-MM-DD.', 'error')
                    return render_template('todo_form.html', form=form, action='Edit', todo=todo)
            
            # Update todo
            todo.title = form.title.data
            todo.description = form.description.data
            todo.priority = form.priority.data
            todo.due_date = due_date
            todo.updated_at = datetime.utcnow()
            
            db.session.commit()
            
            flash(f'Todo "{todo.title}" updated successfully!', 'success')
            return redirect(url_for('index'))
        
        # Pre-populate due date
        if todo.due_date:
            form.due_date.data = todo.due_date.strftime('%Y-%m-%d')
        
        return render_template('todo_form.html', form=form, action='Edit', todo=todo)
    
    @app.route('/toggle/<int:todo_id>')
    def toggle_todo(todo_id):
        """Toggle todo completion status."""
        todo = Todo.query.get_or_404(todo_id)
        todo.completed = not todo.completed
        todo.updated_at = datetime.utcnow()
        
        db.session.commit()
        
        status = 'completed' if todo.completed else 'pending'
        flash(f'Todo "{todo.title}" marked as {status}!', 'success')
        
        return redirect(url_for('index'))
    
    @app.route('/delete/<int:todo_id>')
    def delete_todo(todo_id):
        """Delete todo."""
        todo = Todo.query.get_or_404(todo_id)
        title = todo.title
        
        db.session.delete(todo)
        db.session.commit()
        
        flash(f'Todo "{title}" deleted successfully!', 'success')
        return redirect(url_for('index'))
    
    # Create todo templates
    todo_index_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Todo App</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        .header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; }
        .stats { display: flex; gap: 20px; margin-bottom: 20px; }
        .stat { background: #f0f0f0; padding: 10px; border-radius: 4px; text-align: center; }
        .filters { margin-bottom: 20px; }
        .todo-item { border: 1px solid #ddd; margin-bottom: 10px; padding: 15px; border-radius: 4px; }
        .todo-item.completed { background: #f9f9f9; opacity: 0.7; }
        .todo-header { display: flex; justify-content: space-between; align-items: center; }
        .todo-title { margin: 0; }
        .todo-title.completed { text-decoration: line-through; }
        .priority { padding: 2px 6px; border-radius: 3px; font-size: 12px; }
        .priority.high { background: #ffebee; color: #c62828; }
        .priority.medium { background: #fff3e0; color: #ef6c00; }
        .priority.low { background: #e8f5e8; color: #2e7d32; }
        .actions a { margin-left: 10px; text-decoration: none; }
        .btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer; text-decoration: none; display: inline-block; }
        .btn-primary { background: #007bff; color: white; }
        .btn-success { background: #28a745; color: white; }
        .btn-warning { background: #ffc107; color: black; }
        .btn-danger { background: #dc3545; color: white; }
        .alert { padding: 10px; margin-bottom: 10px; border-radius: 4px; }
        .alert-success { background: #d4edda; color: #155724; }
        .alert-error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <div class="header">
        <h1>Todo App</h1>
        <a href="{{ url_for('create_todo') }}" class="btn btn-primary">Add Todo</a>
    </div>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <div class="stats">
        <div class="stat">
            <strong>{{ total_todos }}</strong><br>Total
        </div>
        <div class="stat">
            <strong>{{ pending_todos }}</strong><br>Pending
        </div>
        <div class="stat">
            <strong>{{ completed_todos }}</strong><br>Completed
        </div>
    </div>
    
    <div class="filters">
        <strong>Filter:</strong>
        <a href="?status=all&priority={{ filter_priority }}">All</a> |
        <a href="?status=pending&priority={{ filter_priority }}">Pending</a> |
        <a href="?status=completed&priority={{ filter_priority }}">Completed</a>
        
        &nbsp;&nbsp;
        
        <strong>Priority:</strong>
        <a href="?status={{ filter_status }}&priority=all">All</a> |
        <a href="?status={{ filter_status }}&priority=high">High</a> |
        <a href="?status={{ filter_status }}&priority=medium">Medium</a> |
        <a href="?status={{ filter_status }}&priority=low">Low</a>
    </div>
    
    {% if todos %}
        {% for todo in todos %}
            <div class="todo-item {% if todo.completed %}completed{% endif %}">
                <div class="todo-header">
                    <h3 class="todo-title {% if todo.completed %}completed{% endif %}">
                        {{ todo.title }}
                        <span class="priority {{ todo.priority }}">{{ todo.priority }}</span>
                    </h3>
                    <div class="actions">
                        <a href="{{ url_for('toggle_todo', todo_id=todo.id) }}" 
                           class="btn {% if todo.completed %}btn-warning{% else %}btn-success{% endif %}">
                            {% if todo.completed %}Undo{% else %}Complete{% endif %}
                        </a>
                        <a href="{{ url_for('edit_todo', todo_id=todo.id) }}" class="btn btn-primary">Edit</a>
                        <a href="{{ url_for('delete_todo', todo_id=todo.id) }}" 
                           class="btn btn-danger" 
                           onclick="return confirm('Are you sure?')">Delete</a>
                    </div>
                </div>
                
                {% if todo.description %}
                    <p>{{ todo.description }}</p>
                {% endif %}
                
                <small>
                    Created: {{ todo.created_at.strftime('%Y-%m-%d %H:%M') }}
                    {% if todo.due_date %}
                        | Due: {{ todo.due_date.strftime('%Y-%m-%d') }}
                    {% endif %}
                </small>
            </div>
        {% endfor %}
    {% else %}
        <p>No todos found. <a href="{{ url_for('create_todo') }}">Create your first todo!</a></p>
    {% endif %}
</body>
</html>
'''
    
    todo_form_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ action }} Todo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 50px auto; padding: 20px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, textarea, select { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #0056b3; }
        .error { color: red; font-size: 14px; }
        .alert { padding: 10px; margin-bottom: 10px; border-radius: 4px; }
        .alert-error { background: #f8d7da; color: #721c24; }
    </style>
</head>
<body>
    <h1>{{ action }} Todo</h1>
    
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            {% for category, message in messages %}
                <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        {% endif %}
    {% endwith %}
    
    <form method="POST">
        {{ form.hidden_tag() }}
        
        <div class="form-group">
            {{ form.title.label }}
            {{ form.title() }}
            {% if form.title.errors %}
                {% for error in form.title.errors %}
                    <div class="error">{{ error }}</div>
                {% endfor %}
            {% endif %}
        </div>
        
        <div class="form-group">
            {{ form.description.label }}
            {{ form.description(rows=4) }}
        </div>
        
        <div class="form-group">
            <label for="priority">Priority</label>
            <select name="priority" id="priority">
                <option value="low" {% if form.priority.data == 'low' %}selected{% endif %}>Low</option>
                <option value="medium" {% if form.priority.data == 'medium' %}selected{% endif %}>Medium</option>
                <option value="high" {% if form.priority.data == 'high' %}selected{% endif %}>High</option>
            </select>
        </div>
        
        <div class="form-group">
            {{ form.due_date.label }}
            {{ form.due_date(type="date") }}
        </div>
        
        <div class="form-group">
            {{ form.submit() }}
            <a href="{{ url_for('index') }}" style="margin-left: 10px;">Cancel</a>
        </div>
    </form>
</body>
</html>
'''
    
    # Save templates
    os.makedirs('templates', exist_ok=True)
    with open('templates/todo_index.html', 'w') as f:
        f.write(todo_index_template)
    
    with open('templates/todo_form.html', 'w') as f:
        f.write(todo_form_template)
    
    # Initialize database
    with app.app_context():
        db.create_all()
        
        # Create sample todos if empty
        if Todo.query.count() == 0:
            sample_todos = [
                {
                    'title': 'Learn Flask',
                    'description': 'Complete the Flask tutorial and build a web application',
                    'priority': 'high',
                    'due_date': datetime(2024, 2, 15).date()
                },
                {
                    'title': 'Buy groceries',
                    'description': 'Milk, bread, eggs, fruits',
                    'priority': 'medium',
                    'completed': True
                },
                {
                    'title': 'Read Python book',
                    'description': 'Read chapters 5-7',
                    'priority': 'low'
                }
            ]
            
            for todo_data in sample_todos:
                todo = Todo(**todo_data)
                db.session.add(todo)
            
            db.session.commit()
            print("Sample todos created")
    
    print("Todo application complete:")
    print("✓ Todo model with SQLAlchemy")
    print("✓ CRUD operations (Create, Read, Update, Delete)")
    print("✓ Todo completion toggle")
    print("✓ Priority levels and due dates")
    print("✓ Filtering and statistics")
    print("✓ Responsive web interface")
    
    return app

# Main execution
if __name__ == "__main__":
    print("=== Flask Web Framework Development ===")
    
    print("\\n1. Creating Basic Flask App:")
    basic_app = create_basic_flask_app()
    
    print("\\n2. Implementing Templates:")
    template_app = implement_templates()
    
    print("\\n3. Handling Forms:")
    form_app = handle_forms()
    
    print("\\n4. Database Integration:")
    db_app, db = add_database_integration()
    
    print("\\n5. Building Todo Application:")
    todo_app = build_todo_app()
    
    print("\\n" + "="*60)
    print("=== FLASK DEVELOPMENT COMPLETE ===")
    print("✓ Flask application structure")
    print("✓ Route handling and URL parameters")
    print("✓ Jinja2 template system")
    print("✓ Form processing with WTForms")
    print("✓ SQLAlchemy database integration")
    print("✓ Complete todo web application")
    print("\\nTo run any app: app.run(debug=True)")
```

## Hints

- Use `app.run(debug=True)` for development with auto-reload
- Create separate modules for models, forms, and routes in larger apps
- Use `url_for()` for generating URLs instead of hardcoding them
- Handle database operations in try-except blocks
- Use flash messages to provide user feedback

## Test Cases

Your Flask application should:

- Handle multiple routes with different HTTP methods
- Render templates with dynamic content
- Process forms with proper validation
- Perform database CRUD operations
- Display appropriate error messages

## Bonus Challenge

Add user authentication with Flask-Login, implement API endpoints with JSON responses, and deploy to a cloud platform!
