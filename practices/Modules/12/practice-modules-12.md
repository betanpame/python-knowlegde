# Package Development and Distribution - Practice 12

**Difficulty:** ⭐⭐ (Easy-Medium)

## Description

Learn how to create, structure, and distribute Python packages professionally.

## Objectives

- Create proper package structures
- Write setup.py and pyproject.toml files
- Understand package versioning
- Learn distribution best practices

## Your Tasks

1. **create_package_structure()** - Build a complete package layout
2. **write_setup_configuration()** - Create setup.py and pyproject.toml
3. **package_versioning_system()** - Implement version management
4. **dependency_specification()** - Define package dependencies
5. **entry_points_creation()** - Create command-line interfaces
6. **package_metadata_management()** - Handle package information
7. **build_distribution_files()** - Create wheel and source distributions
8. **local_package_installation()** - Install packages in development mode

## Example

```python
# setup.py example
from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "click>=7.0",
    ],
    entry_points={
        "console_scripts": [
            "mycommand=mypackage.cli:main",
        ],
    },
)
```

## Hints

- Use setuptools for package configuration
- Follow semantic versioning (major.minor.patch)
- Include proper metadata (author, description, license)
- Consider using pyproject.toml for modern packaging

## Practice Cases

Your package should include:
- Proper directory structure with __init__.py files
- Complete metadata and dependencies
- Working entry points
- Version information

## Bonus Challenge

Create a package that can be installed via pip and includes both a library API and command-line interface!

Remember: Good packaging makes your code easy to share and install!