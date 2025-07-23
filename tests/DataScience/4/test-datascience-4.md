# Basic Data Visualization with Matplotlib - Test 4

**Difficulty:** ⭐ (Very Easy)

## Description

Learn to create basic visualizations using Matplotlib, the fundamental plotting library in Python. Create line plots, bar charts, histograms, and scatter plots to explore data visually.

## Objectives

- Create line plots for time series data
- Build bar charts for categorical data
- Generate histograms for data distributions
- Create scatter plots for relationships
- Customize plot appearance and labels

## Your Tasks

1. **create_line_plots()** - Plot trends over time
2. **create_bar_charts()** - Visualize categorical data
3. **create_histograms()** - Show data distributions
4. **create_scatter_plots()** - Explore relationships
5. **customize_plots()** - Add labels, colors, and styling

## Example

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def create_line_plots():
    """Create line plots for time series data."""
    
    # Create sample time series data
    dates = pd.date_range('2023-01-01', periods=30, freq='D')
    temperature = 20 + 10 * np.sin(np.arange(30) * 2 * np.pi / 7) + np.random.normal(0, 2, 30)
    humidity = 60 + 15 * np.cos(np.arange(30) * 2 * np.pi / 7) + np.random.normal(0, 5, 30)
    
    # Create line plot
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.plot(dates, temperature, marker='o', linestyle='-', color='red', label='Temperature')
    plt.title('Daily Temperature')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.plot(dates, humidity, marker='s', linestyle='--', color='blue', label='Humidity')
    plt.title('Daily Humidity')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Multiple lines on same plot
    plt.figure(figsize=(10, 6))
    plt.plot(dates, temperature, label='Temperature (°C)', color='red', linewidth=2)
    plt.plot(dates, humidity, label='Humidity (%)', color='blue', linewidth=2)
    plt.title('Weather Data Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return dates, temperature, humidity

def create_bar_charts():
    """Create bar charts for categorical data."""
    
    # Sample categorical data
    categories = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
    sales_q1 = [120, 95, 180, 150, 110]
    sales_q2 = [140, 88, 175, 160, 125]
    
    # Simple bar chart
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.bar(categories, sales_q1, color='skyblue', edgecolor='navy', alpha=0.7)
    plt.title('Q1 Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Sales (thousands)')
    plt.xticks(rotation=45)
    
    # Add value labels on bars
    for i, v in enumerate(sales_q1):
        plt.text(i, v + 5, str(v), ha='center', va='bottom')
    
    # Grouped bar chart
    x = np.arange(len(categories))
    width = 0.35
    
    plt.subplot(1, 2, 2)
    plt.bar(x - width/2, sales_q1, width, label='Q1', color='lightblue', alpha=0.8)
    plt.bar(x + width/2, sales_q2, width, label='Q2', color='lightcoral', alpha=0.8)
    
    plt.title('Quarterly Sales Comparison')
    plt.xlabel('Product')
    plt.ylabel('Sales (thousands)')
    plt.xticks(x, categories, rotation=45)
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Horizontal bar chart
    plt.figure(figsize=(8, 6))
    plt.barh(categories, sales_q1, color='lightgreen', alpha=0.7)
    plt.title('Q1 Sales (Horizontal)')
    plt.xlabel('Sales (thousands)')
    plt.ylabel('Product')
    plt.grid(axis='x', alpha=0.3)
    plt.show()
    
    return categories, sales_q1, sales_q2

def create_histograms():
    """Create histograms to show data distributions."""
    
    # Generate sample data
    np.random.seed(42)
    normal_data = np.random.normal(100, 15, 1000)
    uniform_data = np.random.uniform(50, 150, 1000)
    
    # Single histogram
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.hist(normal_data, bins=30, color='purple', alpha=0.7, edgecolor='black')
    plt.title('Normal Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    # Add statistics
    mean_val = np.mean(normal_data)
    std_val = np.std(normal_data)
    plt.axvline(mean_val, color='red', linestyle='--', linewidth=2, label=f'Mean: {mean_val:.1f}')
    plt.axvline(mean_val + std_val, color='orange', linestyle='--', alpha=0.7, label=f'+1 STD: {mean_val + std_val:.1f}')
    plt.axvline(mean_val - std_val, color='orange', linestyle='--', alpha=0.7, label=f'-1 STD: {mean_val - std_val:.1f}')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.hist(uniform_data, bins=30, color='green', alpha=0.7, edgecolor='black')
    plt.title('Uniform Distribution')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Overlapping histograms
    plt.figure(figsize=(10, 6))
    plt.hist(normal_data, bins=30, alpha=0.5, color='blue', label='Normal', density=True)
    plt.hist(uniform_data, bins=30, alpha=0.5, color='red', label='Uniform', density=True)
    plt.title('Distribution Comparison')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return normal_data, uniform_data

def create_scatter_plots():
    """Create scatter plots to explore relationships."""
    
    # Generate sample data with relationships
    np.random.seed(42)
    x = np.random.normal(50, 15, 100)
    y = 2 * x + np.random.normal(0, 10, 100)  # Positive correlation
    z = -1.5 * x + 200 + np.random.normal(0, 15, 100)  # Negative correlation
    
    sizes = np.random.randint(20, 200, 100)
    colors = np.random.choice(['red', 'blue', 'green', 'purple', 'orange'], 100)
    
    # Basic scatter plot
    plt.figure(figsize=(12, 6))
    
    plt.subplot(1, 2, 1)
    plt.scatter(x, y, alpha=0.6, color='blue')
    plt.title('Positive Correlation')
    plt.xlabel('X Variable')
    plt.ylabel('Y Variable')
    plt.grid(True, alpha=0.3)
    
    # Add trend line
    z_poly = np.polyfit(x, y, 1)
    p_poly = np.poly1d(z_poly)
    plt.plot(x, p_poly(x), "r--", alpha=0.8, linewidth=2, label=f'Trend: y = {z_poly[0]:.2f}x + {z_poly[1]:.2f}')
    plt.legend()
    
    plt.subplot(1, 2, 2)
    plt.scatter(x, z, alpha=0.6, color='red')
    plt.title('Negative Correlation')
    plt.xlabel('X Variable')
    plt.ylabel('Z Variable')
    plt.grid(True, alpha=0.3)
    
    # Add trend line
    z_poly2 = np.polyfit(x, z, 1)
    p_poly2 = np.poly1d(z_poly2)
    plt.plot(x, p_poly2(x), "b--", alpha=0.8, linewidth=2, label=f'Trend: z = {z_poly2[0]:.2f}x + {z_poly2[1]:.2f}')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    # Fancy scatter plot with size and color variations
    plt.figure(figsize=(10, 8))
    scatter = plt.scatter(x, y, s=sizes, c=x, cmap='viridis', alpha=0.6, edgecolors='black', linewidth=0.5)
    plt.colorbar(scatter, label='X Value')
    plt.title('Scatter Plot with Size and Color Mapping')
    plt.xlabel('X Variable')
    plt.ylabel('Y Variable')
    plt.grid(True, alpha=0.3)
    plt.show()
    
    return x, y, z

def customize_plots():
    """Learn to customize plot appearance."""
    
    # Sample data
    x = np.linspace(0, 10, 100)
    y1 = np.sin(x)
    y2 = np.cos(x)
    y3 = np.sin(x) * np.cos(x)
    
    # Customized plot
    plt.figure(figsize=(12, 8))
    
    # Set style
    plt.style.use('seaborn-v0_8')
    
    plt.plot(x, y1, label='sin(x)', linewidth=3, color='#FF6B6B', linestyle='-')
    plt.plot(x, y2, label='cos(x)', linewidth=3, color='#4ECDC4', linestyle='--')
    plt.plot(x, y3, label='sin(x)cos(x)', linewidth=3, color='#45B7D1', linestyle=':')
    
    # Customize title and labels
    plt.title('Trigonometric Functions', fontsize=18, fontweight='bold', pad=20)
    plt.xlabel('X Values', fontsize=14, fontweight='bold')
    plt.ylabel('Y Values', fontsize=14, fontweight='bold')
    
    # Customize legend
    plt.legend(fontsize=12, frameon=True, fancybox=True, shadow=True, framealpha=0.9)
    
    # Customize grid
    plt.grid(True, linestyle=':', alpha=0.6, color='gray')
    
    # Customize axes
    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
    
    # Add annotations
    plt.annotate('Maximum of sin(x)', xy=(np.pi/2, 1), xytext=(2, 1.3),
                arrowprops=dict(arrowstyle='->', color='red', lw=2),
                fontsize=12, ha='center')
    
    # Customize tick labels
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    
    plt.tight_layout()
    plt.show()
    
    # Subplots with different styles
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Different Plot Styles', fontsize=16, fontweight='bold')
    
    # Plot 1: Default style
    axes[0, 0].plot(x, y1, 'b-', linewidth=2)
    axes[0, 0].set_title('Default Style')
    axes[0, 0].grid(True)
    
    # Plot 2: Dots and markers
    axes[0, 1].plot(x[::5], y2[::5], 'ro-', markersize=8, linewidth=2)
    axes[0, 1].set_title('Markers Style')
    axes[0, 1].grid(True)
    
    # Plot 3: Filled area
    axes[1, 0].fill_between(x, y3, alpha=0.5, color='green')
    axes[1, 0].plot(x, y3, 'g-', linewidth=2)
    axes[1, 0].set_title('Filled Area')
    axes[1, 0].grid(True)
    
    # Plot 4: Step plot
    axes[1, 1].step(x[::10], y1[::10], 'purple', linewidth=3, where='mid')
    axes[1, 1].set_title('Step Plot')
    axes[1, 1].grid(True)
    
    plt.tight_layout()
    plt.show()
    
    return x, y1, y2, y3

# Test all functions
if __name__ == "__main__":
    print("=== Basic Data Visualization with Matplotlib ===")
    
    print("\\n1. Creating Line Plots:")
    line_results = create_line_plots()
    
    print("\\n2. Creating Bar Charts:")
    bar_results = create_bar_charts()
    
    print("\\n3. Creating Histograms:")
    hist_results = create_histograms()
    
    print("\\n4. Creating Scatter Plots:")
    scatter_results = create_scatter_plots()
    
    print("\\n5. Customizing Plots:")
    custom_results = customize_plots()
    
    print("\\n=== Matplotlib Visualization Complete! ===")
```

## Hints

- Use `plt.figure(figsize=(width, height))` to set plot size
- Use `plt.subplot()` to create multiple plots in one figure
- Add `plt.grid(True)` for better readability
- Use `plt.legend()` to show plot labels
- Use `plt.tight_layout()` to prevent overlapping elements

## Test Cases

Your functions should:

- Create line plots with proper labels and markers
- Generate bar charts (vertical and horizontal) with multiple series
- Build histograms showing data distributions
- Create scatter plots with trend lines and correlations
- Customize plots with colors, styles, annotations, and formatting

## Bonus Challenge

Create a dashboard-style visualization combining multiple chart types to tell a data story!
