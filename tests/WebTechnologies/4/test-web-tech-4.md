# Web Scraping with BeautifulSoup - Test 4

**Difficulty:** ⭐ (Very Easy)

## Description

Learn web scraping fundamentals using BeautifulSoup and requests. Extract data from websites, handle different HTML structures, and manage common scraping challenges.

## Objectives

- Parse HTML with BeautifulSoup
- Extract text, links, and attributes from web pages
- Handle different selectors (CSS, XPath-like)
- Manage forms, tables, and dynamic content
- Implement ethical scraping practices

## Your Tasks

1. **basic_html_parsing()** - Parse HTML and extract basic elements
2. **extract_links_and_images()** - Extract all links and images from pages
3. **scrape_tables()** - Extract data from HTML tables
4. **handle_forms()** - Work with form data and submissions
5. **advanced_scraping()** - Handle pagination and complex structures

## Example

```python
import requests
from bs4 import BeautifulSoup, Comment
import re
import time
import csv
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Any, Optional
import json
from datetime import datetime

def basic_html_parsing():
    """Parse HTML and extract basic elements."""
    print("=== Basic HTML Parsing ===")
    
    # Sample HTML content
    html_content = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Sample Blog</title>
        <meta name="description" content="A sample blog for web scraping">
    </head>
    <body>
        <header>
            <h1 id="main-title">Tech Blog</h1>
            <nav>
                <ul class="nav-menu">
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>
        
        <main>
            <article class="post" data-id="1">
                <h2 class="post-title">Introduction to Python</h2>
                <p class="post-meta">
                    Published by <span class="author">John Doe</span> 
                    on <time datetime="2024-01-15">January 15, 2024</time>
                </p>
                <div class="post-content">
                    <p>Python is a versatile programming language.</p>
                    <p>It's great for web development, data analysis, and more.</p>
                </div>
                <div class="post-tags">
                    <span class="tag">python</span>
                    <span class="tag">programming</span>
                    <span class="tag">beginner</span>
                </div>
            </article>
            
            <article class="post" data-id="2">
                <h2 class="post-title">Web Scraping Guide</h2>
                <p class="post-meta">
                    Published by <span class="author">Jane Smith</span> 
                    on <time datetime="2024-01-20">January 20, 2024</time>
                </p>
                <div class="post-content">
                    <p>Learn how to scrape websites responsibly.</p>
                    <p>Always check robots.txt before scraping.</p>
                </div>
                <div class="post-tags">
                    <span class="tag">web-scraping</span>
                    <span class="tag">beautifulsoup</span>
                    <span class="tag">python</span>
                </div>
            </article>
        </main>
        
        <footer>
            <p>&copy; 2024 Tech Blog. All rights reserved.</p>
        </footer>
    </body>
    </html>
    '''
    
    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract basic information
    print("Page Title:", soup.title.string)
    print("Meta Description:", soup.find('meta', attrs={'name': 'description'})['content'])
    
    # Extract main heading
    main_title = soup.find('h1', id='main-title')
    print("Main Title:", main_title.text)
    
    # Extract all post titles
    print("\\nPost Titles:")
    post_titles = soup.find_all('h2', class_='post-title')
    for i, title in enumerate(post_titles, 1):
        print(f"{i}. {title.text}")
    
    # Extract post metadata
    print("\\nPost Details:")
    posts = soup.find_all('article', class_='post')
    for post in posts:
        title = post.find('h2', class_='post-title').text
        author = post.find('span', class_='author').text
        date = post.find('time')['datetime']
        post_id = post['data-id']
        
        print(f"Post ID: {post_id}")
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Date: {date}")
        
        # Extract tags
        tags = [tag.text for tag in post.find_all('span', class_='tag')]
        print(f"Tags: {', '.join(tags)}")
        print("-" * 40)
    
    # Extract navigation links
    print("\\nNavigation Links:")
    nav_links = soup.select('nav .nav-menu a')
    for link in nav_links:
        href = link.get('href')
        text = link.text
        print(f"{text}: {href}")
    
    return soup, posts

def extract_links_and_images():
    """Extract all links and images from pages."""
    print("\\n=== Extracting Links and Images ===")
    
    # Sample HTML with various links and images
    html_content = '''
    <html>
    <head><title>Media Gallery</title></head>
    <body>
        <div class="content">
            <h1>Welcome to our Gallery</h1>
            
            <!-- Internal links -->
            <nav>
                <a href="/gallery">Gallery</a>
                <a href="/about">About Us</a>
                <a href="contact.html">Contact</a>
            </nav>
            
            <!-- External links -->
            <p>Visit our partners:</p>
            <ul>
                <li><a href="https://python.org" target="_blank">Python.org</a></li>
                <li><a href="https://github.com" rel="nofollow">GitHub</a></li>
                <li><a href="mailto:contact@example.com">Email Us</a></li>
                <li><a href="tel:+1234567890">Call Us</a></li>
            </ul>
            
            <!-- Images -->
            <div class="gallery">
                <img src="/images/photo1.jpg" alt="Beautiful landscape" title="Landscape Photo">
                <img src="https://example.com/photo2.jpg" alt="City view" class="featured">
                <img src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="Placeholder">
            </div>
            
            <!-- Download links -->
            <div class="downloads">
                <a href="/downloads/document.pdf" download>Download PDF</a>
                <a href="/downloads/data.csv" download="report.csv">Download Report</a>
            </div>
        </div>
    </body>
    </html>
    '''
    
    soup = BeautifulSoup(html_content, 'html.parser')
    base_url = "https://example.com"
    
    # Extract all links
    def extract_links(soup_obj, base_url):
        links_data = []
        
        for link in soup_obj.find_all('a', href=True):
            href = link['href']
            text = link.get_text(strip=True)
            
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, href)
            
            # Categorize link types
            link_type = "unknown"
            if href.startswith('http'):
                link_type = "external"
            elif href.startswith('/') or href.endswith('.html'):
                link_type = "internal"
            elif href.startswith('mailto:'):
                link_type = "email"
            elif href.startswith('tel:'):
                link_type = "phone"
            elif href.startswith('#'):
                link_type = "anchor"
            
            # Check for special attributes
            attributes = {}
            if link.get('target'):
                attributes['target'] = link['target']
            if link.get('rel'):
                attributes['rel'] = link['rel']
            if link.get('download') is not None:
                attributes['download'] = link.get('download', True)
            
            links_data.append({
                'text': text,
                'href': href,
                'absolute_url': absolute_url,
                'type': link_type,
                'attributes': attributes
            })
        
        return links_data
    
    # Extract all images
    def extract_images(soup_obj, base_url):
        images_data = []
        
        for img in soup_obj.find_all('img'):
            src = img.get('src', '')
            alt = img.get('alt', '')
            title = img.get('title', '')
            
            # Convert relative URLs to absolute
            absolute_url = urljoin(base_url, src) if src else ''
            
            # Determine image type
            img_type = "unknown"
            if src.startswith('data:'):
                img_type = "data_uri"
            elif src.startswith('http'):
                img_type = "external"
            else:
                img_type = "local"
            
            # Get image dimensions if available
            dimensions = {}
            if img.get('width'):
                dimensions['width'] = img['width']
            if img.get('height'):
                dimensions['height'] = img['height']
            
            images_data.append({
                'src': src,
                'absolute_url': absolute_url,
                'alt': alt,
                'title': title,
                'type': img_type,
                'dimensions': dimensions,
                'classes': img.get('class', [])
            })
        
        return images_data
    
    # Extract data
    links = extract_links(soup, base_url)
    images = extract_images(soup, base_url)
    
    # Display results
    print("Found Links:")
    for link in links:
        print(f"Text: {link['text']}")
        print(f"URL: {link['absolute_url']}")
        print(f"Type: {link['type']}")
        if link['attributes']:
            print(f"Attributes: {link['attributes']}")
        print("-" * 30)
    
    print(f"\\nFound Images ({len(images)} total):")
    for img in images:
        print(f"Source: {img['absolute_url']}")
        print(f"Alt text: {img['alt']}")
        print(f"Type: {img['type']}")
        if img['title']:
            print(f"Title: {img['title']}")
        print("-" * 30)
    
    return links, images

def scrape_tables():
    """Extract data from HTML tables."""
    print("\\n=== Scraping Tables ===")
    
    # Sample HTML with different table structures
    html_content = '''
    <html>
    <body>
        <!-- Simple table -->
        <table id="products">
            <thead>
                <tr>
                    <th>Product</th>
                    <th>Price</th>
                    <th>Stock</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Laptop</td>
                    <td>$999.99</td>
                    <td>15</td>
                </tr>
                <tr>
                    <td>Mouse</td>
                    <td>$29.99</td>
                    <td>50</td>
                </tr>
                <tr>
                    <td>Keyboard</td>
                    <td>$79.99</td>
                    <td>25</td>
                </tr>
            </tbody>
        </table>
        
        <!-- Complex table with merged cells -->
        <table id="sales-report">
            <caption>Quarterly Sales Report</caption>
            <thead>
                <tr>
                    <th rowspan="2">Product</th>
                    <th colspan="4">Quarters</th>
                </tr>
                <tr>
                    <th>Q1</th>
                    <th>Q2</th>
                    <th>Q3</th>
                    <th>Q4</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Laptops</td>
                    <td>100</td>
                    <td>120</td>
                    <td>90</td>
                    <td>140</td>
                </tr>
                <tr>
                    <td>Phones</td>
                    <td>200</td>
                    <td>180</td>
                    <td>220</td>
                    <td>250</td>
                </tr>
            </tbody>
        </table>
        
        <!-- Table without headers -->
        <table class="info-table">
            <tr>
                <td><strong>Name:</strong></td>
                <td>John Doe</td>
            </tr>
            <tr>
                <td><strong>Email:</strong></td>
                <td>john@example.com</td>
            </tr>
            <tr>
                <td><strong>Phone:</strong></td>
                <td>+1 234 567 8900</td>
            </tr>
        </table>
    </body>
    </html>
    '''
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Function to extract table data
    def extract_table_data(table):
        data = []
        
        # Try to find headers
        headers = []
        header_row = table.find('thead')
        if header_row:
            # Handle complex headers with rowspan/colspan
            header_rows = header_row.find_all('tr')
            if len(header_rows) == 1:
                headers = [th.get_text(strip=True) for th in header_rows[0].find_all(['th', 'td'])]
            else:
                # For now, just use the last header row
                headers = [th.get_text(strip=True) for th in header_rows[-1].find_all(['th', 'td'])]
        else:
            # Try to use first row as headers
            first_row = table.find('tr')
            if first_row and first_row.find('th'):
                headers = [th.get_text(strip=True) for th in first_row.find_all('th')]
        
        # Extract body data
        tbody = table.find('tbody')
        rows = tbody.find_all('tr') if tbody else table.find_all('tr')
        
        # Skip header row if no thead
        if not table.find('thead') and headers:
            rows = rows[1:]
        
        for row in rows:
            cells = row.find_all(['td', 'th'])
            row_data = [cell.get_text(strip=True) for cell in cells]
            
            if headers and len(row_data) == len(headers):
                data.append(dict(zip(headers, row_data)))
            else:
                data.append(row_data)
        
        return data, headers
    
    # Extract data from all tables
    tables = soup.find_all('table')
    
    for i, table in enumerate(tables, 1):
        table_id = table.get('id', f'table-{i}')
        caption = table.find('caption')
        caption_text = caption.get_text(strip=True) if caption else "No caption"
        
        print(f"\\nTable {i} (ID: {table_id}):")
        print(f"Caption: {caption_text}")
        
        data, headers = extract_table_data(table)
        
        if headers:
            print(f"Headers: {headers}")
        
        print("Data:")
        for row in data:
            if isinstance(row, dict):
                for key, value in row.items():
                    print(f"  {key}: {value}")
                print()
            else:
                print(f"  {row}")
        print("-" * 40)
    
    # Convert table to CSV
    def table_to_csv(table, filename):
        data, headers = extract_table_data(table)
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            if headers and data and isinstance(data[0], dict):
                writer = csv.DictWriter(csvfile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(data)
            else:
                writer = csv.writer(csvfile)
                if headers:
                    writer.writerow(headers)
                for row in data:
                    if isinstance(row, dict):
                        writer.writerow(row.values())
                    else:
                        writer.writerow(row)
    
    # Save first table to CSV
    if tables:
        table_to_csv(tables[0], 'products.csv')
        print("\\nFirst table saved to products.csv")
    
    return tables, data

def handle_forms():
    """Work with form data and submissions."""
    print("\\n=== Handling Forms ===")
    
    # Sample HTML with forms
    html_content = '''
    <html>
    <body>
        <!-- Login form -->
        <form id="login-form" action="/login" method="post">
            <input type="hidden" name="csrf_token" value="abc123">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required>
            
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>
            
            <input type="checkbox" id="remember" name="remember" value="1">
            <label for="remember">Remember me</label>
            
            <button type="submit">Login</button>
        </form>
        
        <!-- Contact form -->
        <form id="contact-form" action="/contact" method="post" enctype="multipart/form-data">
            <input type="text" name="name" placeholder="Your Name" required>
            <input type="email" name="email" placeholder="Your Email" required>
            
            <select name="subject">
                <option value="">Select Subject</option>
                <option value="general">General Inquiry</option>
                <option value="support">Support</option>
                <option value="billing">Billing</option>
            </select>
            
            <textarea name="message" placeholder="Your Message" rows="5" required></textarea>
            
            <input type="file" name="attachment" accept=".pdf,.doc,.docx">
            
            <input type="submit" value="Send Message">
        </form>
        
        <!-- Search form -->
        <form id="search-form" action="/search" method="get">
            <input type="search" name="q" placeholder="Search...">
            <input type="hidden" name="category" value="all">
            <button type="submit">Search</button>
        </form>
    </body>
    </html>
    '''
    
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Function to extract form information
    def extract_form_data(form):
        form_data = {
            'id': form.get('id'),
            'action': form.get('action', ''),
            'method': form.get('method', 'get').upper(),
            'enctype': form.get('enctype', 'application/x-www-form-urlencoded'),
            'fields': []
        }
        
        # Extract all form fields
        for field in form.find_all(['input', 'select', 'textarea', 'button']):
            field_info = {
                'tag': field.name,
                'type': field.get('type', 'text' if field.name == 'input' else field.name),
                'name': field.get('name'),
                'id': field.get('id'),
                'required': field.has_attr('required'),
                'value': field.get('value', ''),
                'placeholder': field.get('placeholder', ''),
                'accept': field.get('accept', ''),
                'rows': field.get('rows', ''),
                'cols': field.get('cols', '')
            }
            
            # Handle select options
            if field.name == 'select':
                options = []
                for option in field.find_all('option'):
                    options.append({
                        'value': option.get('value', ''),
                        'text': option.get_text(strip=True),
                        'selected': option.has_attr('selected')
                    })
                field_info['options'] = options
            
            # Handle labels
            label = soup.find('label', {'for': field.get('id')})
            if label:
                field_info['label'] = label.get_text(strip=True)
            
            form_data['fields'].append(field_info)
        
        return form_data
    
    # Extract all forms
    forms = soup.find_all('form')
    form_data_list = []
    
    for form in forms:
        form_data = extract_form_data(form)
        form_data_list.append(form_data)
        
        print(f"\\nForm: {form_data['id'] or 'unnamed'}")
        print(f"Action: {form_data['action']}")
        print(f"Method: {form_data['method']}")
        print(f"Encoding: {form_data['enctype']}")
        print("Fields:")
        
        for field in form_data['fields']:
            if field['name']:  # Skip buttons without names
                print(f"  - {field['name']} ({field['type']})")
                if field['label']:
                    print(f"    Label: {field['label']}")
                if field['required']:
                    print(f"    Required: Yes")
                if field['placeholder']:
                    print(f"    Placeholder: {field['placeholder']}")
                if field.get('options'):
                    print(f"    Options: {[opt['text'] for opt in field['options']]}")
        print("-" * 40)
    
    # Simulate form submission preparation
    def prepare_form_data(form_data, user_input):
        """Prepare data for form submission."""
        submission_data = {}
        
        for field in form_data['fields']:
            field_name = field['name']
            if not field_name:
                continue
                
            field_type = field['type']
            
            if field_type == 'hidden':
                submission_data[field_name] = field['value']
            elif field_type in ['text', 'email', 'password', 'search']:
                submission_data[field_name] = user_input.get(field_name, '')
            elif field_type == 'checkbox':
                submission_data[field_name] = field['value'] if user_input.get(field_name) else ''
            elif field_type == 'select':
                submission_data[field_name] = user_input.get(field_name, '')
            elif field_type == 'textarea':
                submission_data[field_name] = user_input.get(field_name, '')
        
        return submission_data
    
    # Example: Prepare login form data
    login_form = form_data_list[0]  # First form (login)
    user_input = {
        'username': 'john_doe',
        'password': 'secret123',
        'remember': True
    }
    
    login_data = prepare_form_data(login_form, user_input)
    print("\\nPrepared login form data:")
    for key, value in login_data.items():
        print(f"  {key}: {value}")
    
    return form_data_list, login_data

def advanced_scraping():
    """Handle pagination and complex structures."""
    print("\\n=== Advanced Scraping Techniques ===")
    
    # Simulate a paginated content page
    def create_paginated_content(page=1):
        """Create sample paginated content."""
        items_per_page = 3
        total_items = 10
        total_pages = (total_items + items_per_page - 1) // items_per_page
        
        start_item = (page - 1) * items_per_page + 1
        end_item = min(page * items_per_page, total_items)
        
        html = f'''
        <html>
        <body>
            <div class="content">
                <h1>Product Catalog - Page {page}</h1>
                <div class="products">
        '''
        
        for i in range(start_item, end_item + 1):
            html += f'''
                    <div class="product" data-id="{i}">
                        <h3>Product {i}</h3>
                        <p class="price">${10 + i}.99</p>
                        <p class="description">Description for product {i}</p>
                    </div>
            '''
        
        html += '''
                </div>
                <div class="pagination">
        '''
        
        # Add pagination links
        if page > 1:
            html += f'<a href="?page={page-1}" class="prev">Previous</a>'
        
        for p in range(1, total_pages + 1):
            if p == page:
                html += f'<span class="current">{p}</span>'
            else:
                html += f'<a href="?page={p}">{p}</a>'
        
        if page < total_pages:
            html += f'<a href="?page={page+1}" class="next">Next</a>'
        
        html += '''
                </div>
            </div>
        </body>
        </html>
        '''
        
        return html
    
    # Scrape all pages
    def scrape_all_pages():
        """Scrape data from all pages."""
        all_products = []
        page = 1
        
        while True:
            print(f"Scraping page {page}...")
            
            # Get page content
            html_content = create_paginated_content(page)
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Extract products from current page
            products = soup.find_all('div', class_='product')
            if not products:
                break
            
            for product in products:
                product_data = {
                    'id': product.get('data-id'),
                    'name': product.find('h3').get_text(strip=True),
                    'price': product.find('p', class_='price').get_text(strip=True),
                    'description': product.find('p', class_='description').get_text(strip=True),
                    'page': page
                }
                all_products.append(product_data)
            
            # Check if there's a next page
            next_link = soup.find('a', class_='next')
            if not next_link:
                break
            
            page += 1
            time.sleep(0.1)  # Be respectful - add delay
        
        return all_products
    
    # Extract structured data
    def extract_structured_data(html_content):
        """Extract JSON-LD and microdata."""
        soup = BeautifulSoup(html_content, 'html.parser')
        structured_data = {}
        
        # Extract JSON-LD
        json_ld_scripts = soup.find_all('script', type='application/ld+json')
        if json_ld_scripts:
            structured_data['json_ld'] = []
            for script in json_ld_scripts:
                try:
                    data = json.loads(script.string)
                    structured_data['json_ld'].append(data)
                except json.JSONDecodeError:
                    pass
        
        # Extract microdata
        microdata_items = soup.find_all(attrs={'itemscope': True})
        if microdata_items:
            structured_data['microdata'] = []
            for item in microdata_items:
                item_data = {
                    'type': item.get('itemtype', ''),
                    'properties': {}
                }
                
                # Find properties
                for prop in item.find_all(attrs={'itemprop': True}):
                    prop_name = prop.get('itemprop')
                    prop_value = prop.get('content') or prop.get_text(strip=True)
                    item_data['properties'][prop_name] = prop_value
                
                structured_data['microdata'].append(item_data)
        
        return structured_data
    
    # Clean and normalize text
    def clean_text(text):
        """Clean and normalize extracted text."""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\\s+', ' ', text)
        text = text.strip()
        
        # Remove unwanted characters
        text = re.sub(r'[\\x00-\\x08\\x0B\\x0C\\x0E-\\x1F\\x7F]', '', text)
        
        return text
    
    # Advanced content extraction
    def extract_article_content(soup):
        """Extract main article content, removing navigation and ads."""
        
        # Remove unwanted elements
        for element in soup(['script', 'style', 'nav', 'header', 'footer', 'aside']):
            element.decompose()
        
        # Remove comments
        for comment in soup.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        
        # Find main content
        main_content = None
        
        # Try common content selectors
        content_selectors = [
            'article',
            '[role="main"]',
            'main',
            '.content',
            '.post-content',
            '.article-content',
            '#content'
        ]
        
        for selector in content_selectors:
            main_content = soup.select_one(selector)
            if main_content:
                break
        
        if not main_content:
            # Fallback: find the element with most text
            all_elements = soup.find_all(['div', 'section', 'article'])
            if all_elements:
                main_content = max(all_elements, key=lambda x: len(x.get_text()))
        
        if main_content:
            # Extract and clean text
            text = main_content.get_text()
            return clean_text(text)
        
        return ""
    
    # Run advanced scraping
    print("\\n1. Scraping paginated content:")
    all_products = scrape_all_pages()
    print(f"Total products scraped: {len(all_products)}")
    
    for product in all_products[:3]:  # Show first 3
        print(f"  {product['name']} - {product['price']} (Page {product['page']})")
    
    print("\\n2. Text cleaning example:")
    messy_text = "  This   is\\n\\n\\ta   messy\\ttext  with\\nextra   whitespace  "
    cleaned = clean_text(messy_text)
    print(f"Original: {repr(messy_text)}")
    print(f"Cleaned: {repr(cleaned)}")
    
    print("\\n3. Advanced content extraction:")
    sample_html = '''
    <html>
    <head><title>Article</title></head>
    <body>
        <nav>Navigation menu</nav>
        <header>Site header</header>
        <main>
            <article>
                <h1>Main Article Title</h1>
                <p>This is the main content of the article.</p>
                <p>It contains valuable information.</p>
            </article>
        </main>
        <aside>Sidebar content</aside>
        <footer>Site footer</footer>
    </body>
    </html>
    '''
    
    soup = BeautifulSoup(sample_html, 'html.parser')
    article_text = extract_article_content(soup)
    print(f"Extracted article text: {article_text}")
    
    return all_products, cleaned, article_text

# Main execution
if __name__ == "__main__":
    print("=== Web Scraping with BeautifulSoup ===")
    
    print("\\n1. Basic HTML Parsing:")
    soup, posts = basic_html_parsing()
    
    print("\\n2. Extracting Links and Images:")
    links, images = extract_links_and_images()
    
    print("\\n3. Scraping Tables:")
    tables, table_data = scrape_tables()
    
    print("\\n4. Handling Forms:")
    forms, login_data = handle_forms()
    
    print("\\n5. Advanced Scraping:")
    products, cleaned_text, article_text = advanced_scraping()
    
    print("\\n" + "="*50)
    print("=== WEB SCRAPING COMPLETE ===")
    print("✓ HTML parsing and element extraction")
    print("✓ Link and image extraction")
    print("✓ Table data extraction")
    print("✓ Form handling and data preparation")
    print("✓ Advanced scraping techniques")
    print("✓ Text cleaning and normalization")
```

## Hints

- Always check `robots.txt` and respect rate limits when scraping
- Use `time.sleep()` between requests to be respectful to servers
- Handle missing elements gracefully with `.get()` and try-except blocks
- Use CSS selectors or `find()` methods based on your needs
- Clean and validate extracted data before using it

## Test Cases

Your scraping functions should:

- Parse HTML and extract specific elements accurately
- Handle missing or malformed HTML gracefully
- Extract all links and categorize them properly
- Convert table data to structured formats
- Prepare form data for submission

## Bonus Challenge

Add support for JavaScript-rendered content with Selenium, implement caching for scraped data, and create a scraping pipeline with error recovery!
