# JSON and XML Data Processing - Practice 3

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to work with JSON and XML data formats in Python. Master reading, writing, parsing, and manipulating structured data commonly used in web APIs and data exchange.

## Objectives

- Parse and generate JSON data
- Work with nested JSON structures
- Handle XML parsing and creation
- Convert between different data formats
- Validate and sanitize data

## Your Tasks

1. **parse_json_data()** - Parse JSON from strings and files
2. **create_json_response()** - Generate JSON responses for APIs
3. **handle_nested_json()** - Work with complex nested structures
4. **parse_xml_data()** - Parse XML documents
5. **convert_data_formats()** - Convert between JSON and XML

## Example

```python
import json
import xml.etree.ElementTree as ET
from xml.dom import minidom
import csv
from typing import Dict, List, Any, Union
import requests
from datetime import datetime
import xmltodict

def parse_json_data():
    """Parse JSON data from various sources."""
    print("=== JSON Data Parsing ===")
    
    # 1. Parse JSON from string
    json_string = '''
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York",
        "hobbies": ["reading", "swimming", "coding"],
        "address": {
            "street": "123 Main St",
            "zipcode": "10001"
        }
    }
    '''
    
    try:
        data = json.loads(json_string)
        print("Parsed JSON data:")
        print(f"Name: {data['name']}")
        print(f"Age: {data['age']}")
        print(f"Hobbies: {', '.join(data['hobbies'])}")
        print(f"Address: {data['address']['street']}, {data['address']['zipcode']}")
    except json.JSONDecodeError as e:
        print(f"JSON parsing error: {e}")
    
    # 2. Parse JSON from file
    sample_data = {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"},
            {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
        ],
        "metadata": {
            "total": 3,
            "created": datetime.now().isoformat()
        }
    }
    
    # Write to file
    with open('users.json', 'w') as f:
        json.dump(sample_data, f, indent=2)
    
    # Read from file
    with open('users.json', 'r') as f:
        loaded_data = json.load(f)
    
    print("\\nLoaded from file:")
    for user in loaded_data['users']:
        print(f"User {user['id']}: {user['name']} - {user['email']}")
    
    # 3. Parse JSON with error handling
    invalid_json = '{"name": "John", "age": 30,}'  # Trailing comma
    
    try:
        json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"\\nInvalid JSON error: {e}")
        print(f"Error at line {e.lineno}, column {e.colno}")
    
    return data, loaded_data

def create_json_response():
    """Create JSON responses for APIs."""
    print("\\n=== Creating JSON Responses ===")
    
    # 1. Simple API response
    def create_user_response(user_id: int, name: str, email: str):
        response = {
            "status": "success",
            "data": {
                "user": {
                    "id": user_id,
                    "name": name,
                    "email": email,
                    "created_at": datetime.now().isoformat()
                }
            },
            "metadata": {
                "timestamp": datetime.now().isoformat(),
                "version": "1.0"
            }
        }
        return json.dumps(response, indent=2)
    
    user_response = create_user_response(1, "John Doe", "john@example.com")
    print("User creation response:")
    print(user_response)
    
    # 2. Error response
    def create_error_response(error_code: int, message: str, details: str = None):
        response = {
            "status": "error",
            "error": {
                "code": error_code,
                "message": message,
                "timestamp": datetime.now().isoformat()
            }
        }
        
        if details:
            response["error"]["details"] = details
        
        return json.dumps(response, indent=2)
    
    error_response = create_error_response(404, "User not found", "User with ID 999 does not exist")
    print("\\nError response:")
    print(error_response)
    
    # 3. Paginated response
    def create_paginated_response(data: List[Dict], page: int, per_page: int, total: int):
        response = {
            "status": "success",
            "data": data,
            "pagination": {
                "page": page,
                "per_page": per_page,
                "total": total,
                "pages": (total + per_page - 1) // per_page,
                "has_next": page * per_page < total,
                "has_prev": page > 1
            }
        }
        return json.dumps(response, indent=2)
    
    sample_posts = [
        {"id": i, "title": f"Post {i}", "content": f"Content for post {i}"} 
        for i in range(1, 6)
    ]
    
    paginated_response = create_paginated_response(sample_posts, 1, 5, 25)
    print("\\nPaginated response:")
    print(paginated_response)
    
    return user_response, error_response, paginated_response

def handle_nested_json():
    """Work with complex nested JSON structures."""
    print("\\n=== Handling Nested JSON ===")
    
    # Complex nested structure
    complex_data = {
        "company": {
            "name": "Tech Corp",
            "founded": 2020,
            "employees": [
                {
                    "id": 1,
                    "name": "Alice Johnson",
                    "department": {
                        "name": "Engineering",
                        "budget": 1000000,
                        "projects": [
                            {
                                "name": "Project Alpha",
                                "status": "active",
                                "team": ["Alice", "Bob", "Charlie"],
                                "milestones": [
                                    {"name": "Phase 1", "completed": True, "date": "2024-01-15"},
                                    {"name": "Phase 2", "completed": False, "date": "2024-03-15"}
                                ]
                            }
                        ]
                    }
                },
                {
                    "id": 2,
                    "name": "Bob Smith",
                    "department": {
                        "name": "Marketing",
                        "budget": 500000,
                        "projects": [
                            {
                                "name": "Campaign X",
                                "status": "planning",
                                "team": ["Bob", "Diana"],
                                "milestones": []
                            }
                        ]
                    }
                }
            ]
        }
    }
    
    # Navigate nested structure
    print("Company Information:")
    print(f"Name: {complex_data['company']['name']}")
    print(f"Founded: {complex_data['company']['founded']}")
    print(f"Number of employees: {len(complex_data['company']['employees'])}")
    
    # Extract specific data
    print("\\nEmployee Projects:")
    for employee in complex_data['company']['employees']:
        name = employee['name']
        dept = employee['department']['name']
        projects = employee['department']['projects']
        
        print(f"{name} ({dept}):")
        for project in projects:
            print(f"  - {project['name']}: {project['status']}")
            print(f"    Team: {', '.join(project['team'])}")
            
            if project['milestones']:
                print("    Milestones:")
                for milestone in project['milestones']:
                    status = "✓" if milestone['completed'] else "○"
                    print(f"      {status} {milestone['name']} ({milestone['date']})")
    
    # Modify nested data
    def add_milestone(data: Dict, employee_name: str, project_name: str, milestone: Dict):
        for employee in data['company']['employees']:
            if employee['name'] == employee_name:
                for project in employee['department']['projects']:
                    if project['name'] == project_name:
                        project['milestones'].append(milestone)
                        return True
        return False
    
    new_milestone = {
        "name": "Phase 3",
        "completed": False,
        "date": "2024-05-15"
    }
    
    if add_milestone(complex_data, "Alice Johnson", "Project Alpha", new_milestone):
        print("\\nAdded new milestone to Project Alpha")
    
    # Flatten nested structure
    def flatten_employees(data: Dict) -> List[Dict]:
        flattened = []
        for employee in data['company']['employees']:
            flat_employee = {
                "id": employee['id'],
                "name": employee['name'],
                "department_name": employee['department']['name'],
                "department_budget": employee['department']['budget'],
                "project_count": len(employee['department']['projects'])
            }
            flattened.append(flat_employee)
        return flattened
    
    flat_employees = flatten_employees(complex_data)
    print("\\nFlattened employee data:")
    for emp in flat_employees:
        print(f"ID: {emp['id']}, Name: {emp['name']}, Dept: {emp['department_name']}")
    
    return complex_data, flat_employees

def parse_xml_data():
    """Parse XML documents."""
    print("\\n=== XML Data Parsing ===")
    
    # Create sample XML
    xml_string = '''<?xml version="1.0" encoding="UTF-8"?>
    <library>
        <book id="1" genre="fiction">
            <title>The Great Gatsby</title>
            <author>F. Scott Fitzgerald</author>
            <year>1925</year>
            <price currency="USD">12.99</price>
            <availability>
                <in_stock>true</in_stock>
                <quantity>15</quantity>
            </availability>
        </book>
        <book id="2" genre="science">
            <title>A Brief History of Time</title>
            <author>Stephen Hawking</author>
            <year>1988</year>
            <price currency="USD">15.99</price>
            <availability>
                <in_stock>false</in_stock>
                <quantity>0</quantity>
            </availability>
        </book>
        <book id="3" genre="fiction">
            <title>1984</title>
            <author>George Orwell</author>
            <year>1949</year>
            <price currency="USD">13.99</price>
            <availability>
                <in_stock>true</in_stock>
                <quantity>8</quantity>
            </availability>
        </book>
    </library>'''
    
    # Parse XML with ElementTree
    root = ET.fromstring(xml_string)
    
    print("Library Books:")
    for book in root.findall('book'):
        book_id = book.get('id')
        genre = book.get('genre')
        title = book.find('title').text
        author = book.find('author').text
        year = book.find('year').text
        
        price_elem = book.find('price')
        price = price_elem.text
        currency = price_elem.get('currency')
        
        availability = book.find('availability')
        in_stock = availability.find('in_stock').text == 'true'
        quantity = int(availability.find('quantity').text)
        
        print(f"Book {book_id}: {title}")
        print(f"  Author: {author} ({year})")
        print(f"  Genre: {genre}")
        print(f"  Price: {price} {currency}")
        print(f"  In Stock: {in_stock} (Quantity: {quantity})")
        print()
    
    # Create XML programmatically
    def create_xml_catalog(books: List[Dict]) -> str:
        catalog = ET.Element("catalog")
        
        for book_data in books:
            book = ET.SubElement(catalog, "book")
            book.set("id", str(book_data["id"]))
            book.set("isbn", book_data.get("isbn", ""))
            
            # Add child elements
            for field in ["title", "author", "category", "description"]:
                if field in book_data:
                    elem = ET.SubElement(book, field)
                    elem.text = book_data[field]
            
            # Add price with attributes
            if "price" in book_data:
                price_elem = ET.SubElement(book, "price")
                price_elem.text = str(book_data["price"])
                price_elem.set("currency", book_data.get("currency", "USD"))
        
        # Convert to string with pretty formatting
        xml_str = ET.tostring(catalog, encoding='unicode')
        
        # Pretty print
        dom = minidom.parseString(xml_str)
        return dom.toprettyxml(indent="  ")
    
    new_books = [
        {
            "id": 1,
            "isbn": "978-0-123456-78-9",
            "title": "Python Programming",
            "author": "John Smith",
            "category": "Programming",
            "description": "A comprehensive guide to Python programming",
            "price": 29.99,
            "currency": "USD"
        },
        {
            "id": 2,
            "isbn": "978-0-987654-32-1",
            "title": "Web Development",
            "author": "Jane Doe",
            "category": "Web",
            "description": "Modern web development techniques",
            "price": 34.99,
            "currency": "USD"
        }
    ]
    
    xml_catalog = create_xml_catalog(new_books)
    print("Generated XML catalog:")
    print(xml_catalog)
    
    return root, xml_catalog

def convert_data_formats():
    """Convert between different data formats."""
    print("\\n=== Data Format Conversion ===")
    
    # Sample data
    data = {
        "products": [
            {
                "id": 1,
                "name": "Laptop",
                "category": "Electronics",
                "price": 999.99,
                "specs": {
                    "cpu": "Intel i7",
                    "ram": "16GB",
                    "storage": "512GB SSD"
                }
            },
            {
                "id": 2,
                "name": "Mouse",
                "category": "Accessories",
                "price": 29.99,
                "specs": {
                    "type": "Wireless",
                    "dpi": "1600",
                    "battery": "AAA x2"
                }
            }
        ]
    }
    
    # 1. JSON to XML
    def json_to_xml(json_data: Dict, root_name: str = "root") -> str:
        def dict_to_xml(data: Any, parent: ET.Element, name: str = "item"):
            if isinstance(data, dict):
                element = ET.SubElement(parent, name)
                for key, value in data.items():
                    dict_to_xml(value, element, key)
            elif isinstance(data, list):
                for item in data:
                    dict_to_xml(item, parent, name[:-1] if name.endswith('s') else name)
            else:
                element = ET.SubElement(parent, name)
                element.text = str(data)
        
        root = ET.Element(root_name)
        for key, value in json_data.items():
            dict_to_xml(value, root, key)
        
        xml_str = ET.tostring(root, encoding='unicode')
        dom = minidom.parseString(xml_str)
        return dom.toprettyxml(indent="  ")
    
    xml_data = json_to_xml(data, "catalog")
    print("JSON to XML conversion:")
    print(xml_data)
    
    # 2. JSON to CSV (for flat data)
    def json_to_csv(json_data: List[Dict], filename: str):
        if not json_data:
            return
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = json_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for row in json_data:
                writer.writerow(row)
    
    # Flatten products for CSV
    flat_products = []
    for product in data['products']:
        flat_product = {
            "id": product["id"],
            "name": product["name"],
            "category": product["category"],
            "price": product["price"]
        }
        # Flatten specs
        for spec_key, spec_value in product["specs"].items():
            flat_product[f"spec_{spec_key}"] = spec_value
        
        flat_products.append(flat_product)
    
    json_to_csv(flat_products, "products.csv")
    print("\\nJSON to CSV conversion completed")
    
    # Read CSV back
    with open("products.csv", 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        print("CSV data:")
        for row in csv_reader:
            print(f"  {row['name']}: ${row['price']}")
    
    # 3. XML to JSON
    def xml_to_json(xml_string: str) -> Dict:
        root = ET.fromstring(xml_string)
        
        def element_to_dict(element):
            result = {}
            
            # Add attributes
            if element.attrib:
                result.update(element.attrib)
            
            # Add text content
            if element.text and element.text.strip():
                if len(element) == 0:  # No children
                    return element.text.strip()
                else:
                    result['text'] = element.text.strip()
            
            # Add children
            for child in element:
                child_data = element_to_dict(child)
                
                if child.tag in result:
                    # Multiple children with same tag - convert to list
                    if not isinstance(result[child.tag], list):
                        result[child.tag] = [result[child.tag]]
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = child_data
            
            return result
        
        return {root.tag: element_to_dict(root)}
    
    sample_xml = '''<?xml version="1.0"?>
    <store name="TechStore" location="Downtown">
        <item id="1" category="laptop">
            <name>Gaming Laptop</name>
            <price currency="USD">1299.99</price>
        </item>
        <item id="2" category="mouse">
            <name>Gaming Mouse</name>
            <price currency="USD">79.99</price>
        </item>
    </store>'''
    
    json_from_xml = xml_to_json(sample_xml)
    print("\\nXML to JSON conversion:")
    print(json.dumps(json_from_xml, indent=2))
    
    return xml_data, flat_products, json_from_xml

# Main execution
if __name__ == "__main__":
    print("=== JSON and XML Data Processing ===")
    
    print("\\n1. Parsing JSON Data:")
    json_data, file_data = parse_json_data()
    
    print("\\n2. Creating JSON Responses:")
    user_resp, error_resp, paginated_resp = create_json_response()
    
    print("\\n3. Handling Nested JSON:")
    nested_data, flat_data = handle_nested_json()
    
    print("\\n4. Parsing XML Data:")
    xml_root, xml_catalog = parse_xml_data()
    
    print("\\n5. Converting Data Formats:")
    converted_xml, csv_data, converted_json = convert_data_formats()
    
    print("\\n" + "="*50)
    print("=== DATA PROCESSING COMPLETE ===")
    print("✓ JSON parsing and generation")
    print("✓ Nested data structure handling")
    print("✓ XML parsing and creation")
    print("✓ Data format conversions")
    print("✓ Error handling and validation")
```

## Hints

- Always handle JSON parsing errors with try-except blocks
- Use `json.dumps(indent=2)` for readable JSON output
- ElementTree is great for XML parsing, minidom for pretty printing
- When converting between formats, consider data structure differences
- Validate data before parsing to avoid errors

## Practice Cases

Your data processing functions should:

- Parse valid JSON without errors
- Handle malformed JSON gracefully
- Navigate complex nested structures
- Parse XML with attributes and text content
- Convert between JSON, XML, and CSV formats

## Bonus Challenge

Add data validation schemas, handle different character encodings, and implement streaming parsers for large files!