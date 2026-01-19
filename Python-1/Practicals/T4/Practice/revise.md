# Streamlit & Matplotlib Comprehensive Reference Guide

## Table of Contents
- [Streamlit Reference](#streamlit-reference)
  - [1. Core Configuration & Structure](#1-core-configuration--structure)
  - [2. Text & Content Display](#2-text--content-display)
  - [3. Input Widgets (User Interaction)](#3-input-widgets-user-interaction)
  - [4. Media & File Handling](#4-media--file-handling)
  - [5. Data Visualization](#5-data-visualization)
  - [6. Status & Feedback](#6-status--feedback)
- [Matplotlib Reference](#matplotlib-reference)
  - [Line Plot Parameters](#line-plot-parameters)
  - [Plot Types with Examples](#plot-types-with-examples)
  - [Plot Configuration](#plot-configuration)
- [Examples](#examples)
  - [Streamlit Examples](#streamlit-examples)
  - [Matplotlib Examples](#matplotlib-examples)

---

## Streamlit Reference

### 1. Core Configuration & Structure

**`st.set_page_config(page_title, page_icon, layout)`**
- **Description**: Configures page settings - must be the first Streamlit command in your script.
- **Parameters**:
  - `page_title`: Title displayed in browser tab
  - `page_icon`: Favicon (emoji or file path)
  - `layout`: "centered" (default) or "wide"
- **Example**: `st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")`

**`st.sidebar`**
- **Description**: Context manager for creating sidebar widgets.
- **Parameters**: Widgets placed inside the context manager
- **Example**:
```python
with st.sidebar:
    option = st.selectbox("Choose option", ["A", "B", "C"])
```

**`st.columns(n)`**
- **Description**: Creates horizontal columns for side-by-side layouts.
- **Parameters**:
  - `n`: Number of columns (integer)
- **Returns**: List of column objects
- **Example**:
```python
col1, col2 = st.columns(2)
with col1:
    st.write("Left content")
```

**`st.expander("Title")`**
- **Description**: Creates a collapsible/expandable container.
- **Parameters**:
  - `title`: String displayed as expander header
- **Example**:
```python
with st.expander("See details"):
    st.write("Hidden content here")
```

### 2. Text & Content Display

**`st.title(text)`**
- **Description**: Displays main page title (largest heading).
- **Parameters**: `text`: Title string
- **Example**: `st.title("Sales Dashboard")`
- **Output**: Large heading at top of page

**`st.header(text)`**
- **Description**: Displays section header.
- **Parameters**: `text`: Header string
- **Example**: `st.header("Monthly Report")`
- **Output**: Medium-sized heading

**`st.subheader(text)`**
- **Description**: Displays subsection header.
- **Parameters**: `text`: Subheader string
- **Example**: `st.subheader("Q1 Performance")`
- **Output**: Smaller heading

**`st.write(*args)`**
- **Description**: Universal display function for text, variables, charts.
- **Parameters**: Any Python object (string, number, DataFrame, chart)
- **Example**: `st.write("Result:", df)`
- **Output**: Renders appropriate display format

**`st.markdown(text)`**
- **Description**: Renders Markdown-formatted text.
- **Parameters**: `text`: Markdown string
- **Example**: `st.markdown("**Bold text** and *italic*")`
- **Output**: Formatted text with Markdown styling

**`st.code(code, language)`**
- **Description**: Displays code blocks with syntax highlighting.
- **Parameters**:
  - `code`: Code string
  - `language`: Programming language (python, javascript, etc.)
- **Example**: `st.code("import streamlit as st", language="python")`
- **Output**: Syntax-highlighted code block

### 3. Input Widgets (User Interaction)

**`st.text_input(label, value, key)`**
- **Description**: Single-line text input field.
- **Parameters**:
  - `label`: Field label
  - `value`: Default value
  - `key`: Unique identifier
- **Example**: `name = st.text_input("Enter name", "John")`
- **Returns**: String value

**`st.text_area(label, value, height)`**
- **Description**: Multi-line text input for longer content.
- **Parameters**:
  - `label`: Field label
  - `value`: Default text
  - `height`: Height in pixels
- **Example**: `notes = st.text_area("Comments", "", height=100)`
- **Returns**: String value

**`st.number_input(label, min_value, max_value, value, step)`**
- **Description**: Input field for numeric values.
- **Parameters**:
  - `label`: Field label
  - `min_value`: Minimum allowed value
  - `max_value`: Maximum allowed value
  - `value`: Default value
  - `step`: Increment/decrement step
- **Example**: `age = st.number_input("Age", 0, 120, 25, 1)`
- **Returns**: Integer or float

**`st.slider(label, min_value, max_value, value)`**
- **Description**: Slider for selecting value from range.
- **Parameters**:
  - `label`: Slider label
  - `min_value`: Minimum value
  - `max_value`: Maximum value
  - `value`: Default value or (start, end) for range
- **Example**: `price = st.slider("Price range", 0.0, 100.0, (25.0, 75.0))`
- **Returns**: Single value or tuple for range

**`st.selectbox(label, options, index)`**
- **Description**: Dropdown menu for single selection.
- **Parameters**:
  - `label`: Dropdown label
  - `options`: List of options
  - `index`: Default selected index
- **Example**: `color = st.selectbox("Color", ["Red", "Blue", "Green"], 0)`
- **Returns**: Selected option

**`st.multiselect(label, options, default)`**
- **Description**: Multi-select dropdown.
- **Parameters**:
  - `label`: Field label
  - `options`: List of options
  - `default`: List of default selections
- **Example**: `skills = st.multiselect("Skills", ["Python", "SQL", "R"], ["Python"])`
- **Returns**: List of selected options

**`st.radio(label, options, index)`**
- **Description**: Radio buttons for single selection.
- **Parameters**:
  - `label`: Group label
  - `options`: List of options
  - `index`: Default selected index
- **Example**: `gender = st.radio("Gender", ["Male", "Female", "Other"], 0)`
- **Returns**: Selected option

**`st.checkbox(label, value)`**
- **Description**: Checkbox for boolean input.
- **Parameters**:
  - `label`: Checkbox label
  - `value`: Default state
- **Example**: `agree = st.checkbox("I agree to terms", False)`
- **Returns**: Boolean (True/False)

**`st.button(label, key)`**
- **Description**: Clickable button.
- **Parameters**:
  - `label`: Button text
  - `key`: Unique identifier
- **Example**: 
```python
if st.button("Process Data"):
    st.write("Processing...")
```
- **Returns**: Boolean (True when clicked)

### 4. Media & File Handling

**`st.file_uploader(label, type, accept_multiple_files)`**
- **Description**: File upload interface.
- **Parameters**:
  - `label`: Uploader label
  - `type`: Allowed file types (e.g., ["csv", "txt"])
  - `accept_multiple_files`: Allow multiple uploads
- **Example**: `uploaded = st.file_uploader("Upload CSV", ["csv"])`
- **Returns**: UploadedFile object or list

**`st.image(image, caption, use_column_width)`**
- **Description**: Displays images.
- **Parameters**:
  - `image`: Path, URL, or bytes
  - `caption`: Image caption
  - `use_column_width`: Fit to column width
- **Example**: `st.image("chart.png", "Sales Chart", use_column_width=True)`
- **Output**: Displayed image

**`st.download_button(label, data, file_name, mime)`**
- **Description**: Download button for files.
- **Parameters**:
  - `label`: Button text
  - `data`: File data
  - `file_name`: Download filename
  - `mime`: MIME type
- **Example**:
```python
st.download_button("Download CSV", csv_data, "data.csv", "text/csv")
```
- **Output**: Download dialog

### 5. Data Visualization

**`st.line_chart(data)`**
- **Description**: Creates interactive line chart.
- **Parameters**: `data`: DataFrame or array
- **Example**: `st.line_chart(df[["Sales", "Profit"]])`
- **Output**: Interactive line chart

**`st.pyplot(fig)`**
- **Description**: Displays Matplotlib figure.
- **Parameters**: `fig`: Matplotlib figure object
- **Example**:
```python
fig, ax = plt.subplots()
ax.plot(x, y)
st.pyplot(fig)
```
- **Output**: Static Matplotlib chart

### 6. Status & Feedback

**`st.success(message)`**
- **Description**: Green success message box.
- **Parameters**: `message`: Success text
- **Example**: `st.success("Data saved successfully!")`
- **Output**: Green notification box

**`st.info(message)`**
- **Description**: Blue information message box.
- **Parameters**: `message`: Information text
- **Example**: `st.info("Please check the new updates.")`
- **Output**: Blue notification box

**`st.warning(message)`**
- **Description**: Yellow warning message box.
- **Parameters**: `message`: Warning text
- **Example**: `st.warning("Data may be incomplete.")`
- **Output**: Yellow notification box

**`st.error(message)`**
- **Description**: Red error message box.
- **Parameters**: `message`: Error text
- **Example**: `st.error("Failed to load data.")`
- **Output**: Red notification box

---

## Matplotlib Reference

### Line Plot Parameters

**Marker Parameters:**
- **`marker`**: Marker style ('.', 'o', 's', '^', 'D', '*', '+', 'x')
- **`ms`** or **`markersize`**: Marker size in points
- **`mfc`** or **`markerfacecolor`**: Marker interior color
- **`mec`** or **`markeredgecolor`**: Marker border color

**Line Parameters:**
- **`c`** or **`color`**: Line color (name, hex, or RGB tuple)
- **`ls`** or **`linestyle`**: Line style ('-', '--', '-.', ':')
- **`lw`** or **`linewidth`**: Line width in points

**Axis Labels:**
- **`xlabel`**: X-axis label text
- **`ylabel`**: Y-axis label text
- **`title`**: Plot title

**Font Configuration:**
- **`fontdict`**: Dictionary controlling text properties
  - `family`: Font family ('serif', 'sans-serif', 'monospace')
  - `color`: Text color
  - `size`: Font size

**Grid Configuration:**
- **`plt.grid()`**: Shows grid lines
  - `axis`: 'x', 'y', or 'both' (default)
  - `lw` or `linewidth`: Grid line width
  - `ls` or `linestyle`: Grid line style
  - `color`: Grid line color

**Colorbar:**
- **`plt.colorbar()`**: Adds colorbar to plot
  - `label`: Colorbar label
  - `orientation`: 'vertical' or 'horizontal'

**Legend:**
- **`plt.legend()`**: Shows legend
  - `title`: Legend title
  - `loc`: Location ('best', 'upper right', 'lower left', etc.)

**Fill Between:**
- **`plt.fill_between(x, y1, y2)`**: Fills area between curves
  - `color`: Fill color
  - `alpha`: Transparency (0-1)
  - `where`: Condition for filling
  - `label`: Legend label
  - `interpolate`: Smooth interpolation

**Axis Control:**
- **`plt.axis()`**: Controls axis display
  - `'off'` or `False`: Hide all axes
  - `'equal'`: Equal scaling
  - `[xmin, xmax, ymin, ymax]`: Set limits

### Plot Types with Examples

**Line Plot:**
```python
import matplotlib.pyplot as plt

# Basic line plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 5, 3]
plt.plot(x, y, marker='o', c='blue', ls='--', lw=2, 
         ms=8, mfc='red', mec='black')
plt.title("Line Plot Example")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(axis='y', lw=0.5, ls=':', color='gray')
plt.show()
```

**Scatter Plot:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Scatter plot with color mapping
x = np.random.randn(50)
y = np.random.randn(50)
colors = np.random.rand(50)
sizes = 100 * np.random.rand(50)

plt.scatter(x, y, c=colors, s=sizes, alpha=0.6, 
           cmap='viridis', ec='black', linewidth=0.5)
plt.colorbar(label='Color value')
plt.title("Scatter Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
```

**Bar Chart:**
```python
import matplotlib.pyplot as plt

# Vertical bar chart
categories = ['A', 'B', 'C', 'D']
values = [23, 45, 56, 78]

plt.bar(categories, values, color=['red', 'blue', 'green', 'orange'], 
        width=0.6, edgecolor='black', linewidth=2)
plt.title("Vertical Bar Chart")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.show()

# Horizontal bar chart
plt.barh(categories, values, height=0.6, color='skyblue')
plt.title("Horizontal Bar Chart")
plt.xlabel("Values")
plt.ylabel("Categories")
plt.show()
```

**Histogram:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Histogram with normal distribution
data = np.random.randn(1000)
plt.hist(data, bins=30, color='lightblue', edgecolor='black', 
         alpha=0.7, orientation='vertical')
plt.title("Histogram Example")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(axis='y', alpha=0.3)
plt.show()
```

**Pie Chart:**
```python
import matplotlib.pyplot as plt

# Pie chart with percentages
labels = ['Python', 'Java', 'C++', 'JavaScript', 'Other']
sizes = [40, 25, 15, 15, 5]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'lightgray']
explode = (0.1, 0, 0, 0, 0)  # explode 1st slice

plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=90,
        counterclock=False)
plt.title("Programming Language Popularity")
plt.show()
```

**Stack Plot:**
```python
import matplotlib.pyplot as plt

# Stack plot (area chart)
x = [1, 2, 3, 4, 5]
y1 = [1, 3, 4, 2, 5]
y2 = [2, 4, 1, 3, 2]
y3 = [1, 2, 3, 1, 4]

plt.stackplot(x, y1, y2, y3, labels=['Series 1', 'Series 2', 'Series 3'],
              colors=['lightblue', 'lightgreen', 'lightcoral'], alpha=0.8)
plt.title("Stack Plot Example")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.show()
```

### Plot Configuration

**Multiple Subplots:**
```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1
axes[0, 0].plot([1, 2, 3], [1, 4, 9], 'r-')
axes[0, 0].set_title('Plot 1')

# Plot 2
axes[0, 1].scatter([1, 2, 3], [2, 5, 10])
axes[0, 1].set_title('Plot 2')

# Plot 3
axes[1, 0].bar(['A', 'B', 'C'], [10, 20, 15])
axes[1, 0].set_title('Plot 3')

# Plot 4
axes[1, 1].hist(np.random.randn(100), bins=20)
axes[1, 1].set_title('Plot 4')

plt.tight_layout()
plt.show()
```

**Custom Styling:**
```python
import matplotlib.pyplot as plt

# Custom font dictionary
title_font = {'family': 'serif',
              'color': 'darkred',
              'size': 16,
              'weight': 'bold'}

label_font = {'family': 'sans-serif',
              'color': 'darkblue',
              'size': 12}

x = [1, 2, 3, 4, 5]
y = [x**2 for x in x]

plt.plot(x, y, 'b-s', linewidth=2, markersize=8)
plt.title("Custom Styled Plot", fontdict=title_font)
plt.xlabel("X Axis", fontdict=label_font)
plt.ylabel("Y Axis", fontdict=label_font)

# Custom grid
plt.grid(True, which='both', axis='both', 
         linestyle='--', linewidth=0.5, alpha=0.7)

# Custom legend
plt.legend(['y = x²'], loc='upper left', 
           frameon=True, fancybox=True, shadow=True)

plt.show()
```

---

## Examples

### Streamlit Examples

**Basic Data App:**
```python
import streamlit as st
import pandas as pd
import numpy as np

# Page config
st.set_page_config(
    page_title="Data Analysis App",
    page_icon="📈",
    layout="wide"
)

# Sidebar
with st.sidebar:
    st.header("Filters")
    dataset = st.selectbox(
        "Choose dataset",
        ["Sales", "Users", "Products"]
    )
    show_raw = st.checkbox("Show raw data")

# Main content
st.title(f"{dataset} Analysis")

# Create sample data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Sales': np.random.randint(100, 500, 5),
    'Profit': np.random.randint(50, 200, 5)
})

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Summary")
    st.write(f"Total Sales: ${data['Sales'].sum():,}")
    st.write(f"Average Profit: ${data['Profit'].mean():,.2f}")

with col2:
    st.subheader("Visualization")
    st.line_chart(data.set_index('Month'))

# Expander for raw data
if show_raw:
    with st.expander("Raw Data"):
        st.dataframe(data)

# Download option
csv = data.to_csv(index=False)
st.download_button(
    label="Download CSV",
    data=csv,
    file_name="data.csv",
    mime="text/csv"
)
```

**Interactive Form:**
```python
import streamlit as st

st.title("User Registration Form")

# Create form
with st.form("registration_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("First Name")
        email = st.text_input("Email")
        age = st.number_input("Age", 18, 100, 25)
        
    with col2:
        last_name = st.text_input("Last Name")
        phone = st.text_input("Phone")
        country = st.selectbox("Country", ["USA", "UK", "Canada", "Australia"])
    
    # Multi-select
    interests = st.multiselect(
        "Interests",
        ["Technology", "Sports", "Music", "Travel", "Food"]
    )
    
    # Text area
    bio = st.text_area("Bio", height=100)
    
    # Checkbox
    terms = st.checkbox("I agree to the terms and conditions")
    
    # Submit button
    submit = st.form_submit_button("Register")
    
    if submit:
        if not terms:
            st.error("You must agree to the terms")
        elif not first_name or not last_name:
            st.warning("Please fill all required fields")
        else:
            st.success(f"Registration complete for {first_name} {last_name}")
            st.info("Check your email for verification")
```

### Matplotlib Examples

**Complete Visualization:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Generate data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.exp(-x/5) * np.sin(x)

# Create figure with subplots
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))

# Plot 1: Multiple lines with legend
ax1.plot(x, y1, label='sin(x)', marker='o', markersize=3, markevery=10)
ax1.plot(x, y2, label='cos(x)', linestyle='--', linewidth=2)
ax1.set_title('Trigonometric Functions')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend(loc='upper right')
ax1.grid(True, alpha=0.3)

# Plot 2: Scatter with colormap
np.random.seed(42)
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 10
colors_scatter = np.random.rand(50)
sizes_scatter = 20 + 100 * np.random.rand(50)

scatter = ax2.scatter(x_scatter, y_scatter, c=colors_scatter, 
                      s=sizes_scatter, alpha=0.6, cmap='viridis')
ax2.set_title('Scatter Plot with Colormap')
ax2.set_xlabel('X')
ax2.set_ylabel('Y')
plt.colorbar(scatter, ax=ax2, label='Color intensity')

# Plot 3: Bar chart with error bars
categories = ['A', 'B', 'C', 'D', 'E']
values = [23, 45, 56, 78, 33]
errors = [3, 5, 2, 7, 4]

bars = ax3.bar(categories, values, yerr=errors, capsize=5,
               color=['skyblue', 'lightgreen', 'lightcoral', 
                      'gold', 'plum'],
               edgecolor='black', linewidth=1)
ax3.set_title('Bar Chart with Error Bars')
ax3.set_xlabel('Category')
ax3.set_ylabel('Value')

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax3.text(bar.get_x() + bar.get_width()/2., height + 2,
             f'{height}', ha='center', va='bottom')

# Plot 4: Histogram with density
data_hist = np.random.normal(0, 1, 1000)
ax4.hist(data_hist, bins=30, density=True, alpha=0.7, 
         color='lightseagreen', edgecolor='black')
ax4.set_title('Histogram with Density')
ax4.set_xlabel('Value')
ax4.set_ylabel('Density')
ax4.grid(True, alpha=0.3)

# Add KDE curve
from scipy.stats import gaussian_kde
kde = gaussian_kde(data_hist)
x_kde = np.linspace(-4, 4, 100)
ax4.plot(x_kde, kde(x_kde), 'r-', linewidth=2)

plt.tight_layout()
plt.savefig('complete_visualization.png', dpi=300, bbox_inches='tight')
plt.show()
```

**Interactive Dashboard-like Plot:**
```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from matplotlib.colors import LinearSegmentedColormap

# Create custom colormap
colors = [(0, 'green'), (0.5, 'yellow'), (1, 'red')]
cmap = LinearSegmentedColormap.from_list('custom', colors)

# Generate data
np.random.seed(42)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
categories = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']

data = np.random.randint(50, 200, size=(len(months), len(categories)))
cumulative = np.cumsum(data, axis=0)

# Create figure
fig = plt.figure(figsize=(14, 10))

# Plot 1: Heatmap-like bar chart
ax1 = plt.subplot(2, 2, 1)
x_pos = np.arange(len(months))
width = 0.15
for i, category in enumerate(categories):
    values = data[:, i]
    # Normalize for colormap
    normalized = (values - values.min()) / (values.max() - values.min())
    colors_bars = [cmap(val) for val in normalized]
    
    ax1.bar(x_pos + i*width, values, width, label=category, 
            color=colors_bars, edgecolor='black')

ax1.set_xlabel('Month')
ax1.set_ylabel('Sales')
ax1.set_title('Monthly Sales by Category')
ax1.set_xticks(x_pos + width*2)
ax1.set_xticklabels(months, rotation=45)
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax1.grid(True, alpha=0.3, axis='y')

# Plot 2: Stacked area chart
ax2 = plt.subplot(2, 2, 2)
ax2.stackplot(months, data.T, labels=categories, alpha=0.8)
ax2.set_title('Cumulative Sales (Stacked)')
ax2.set_xlabel('Month')
ax2.set_ylabel('Sales')
ax2.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
ax2.grid(True, alpha=0.3)

# Plot 3: Pie chart for annual total
ax3 = plt.subplot(2, 2, 3)
annual_totals = np.sum(data, axis=0)
explode = [0.1 if max(annual_totals) == val else 0 for val in annual_totals]
wedges, texts, autotexts = ax3.pie(annual_totals, explode=explode, 
                                    labels=categories, autopct='%1.1f%%',
                                    shadow=True, startangle=90)
ax3.set_title('Annual Sales Distribution')

# Plot 4: Line chart with fill between
ax4 = plt.subplot(2, 2, 4)
for i, category in enumerate(categories):
    ax4.plot(months, data[:, i], marker='o', label=category, linewidth=2)
    
    # Fill between current line and zero
    ax4.fill_between(months, 0, data[:, i], alpha=0.2)

ax4.set_title('Trend Analysis')
ax4.set_xlabel('Month')
ax4.set_ylabel('Sales')
ax4.legend()
ax4.grid(True, alpha=0.3)

# Add overall title
plt.suptitle('Annual Sales Dashboard Analysis', fontsize=16, fontweight='bold')

# Adjust layout
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()
```

**Practical Data Analysis Example:**
```python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# Create time series data
np.random.seed(42)
dates = [datetime(2024, 1, 1) + timedelta(days=i) for i in range(90)]
base_temperature = 20 + 10 * np.sin(np.linspace(0, 2*np.pi, 90))
temperature = base_temperature + np.random.normal(0, 3, 90)
rainfall = np.random.exponential(5, 90)
humidity = 60 + 20 * np.sin(np.linspace(0, 4*np.pi, 90)) + np.random.normal(0, 5, 90)

# Create figure
fig, axes = plt.subplots(3, 1, figsize=(12, 10), sharex=True)

# Plot 1: Temperature with rolling average
ax1 = axes[0]
ax1.plot(dates, temperature, 'o-', color='red', alpha=0.5, 
         markersize=3, label='Daily')
rolling_avg = pd.Series(temperature).rolling(window=7).mean()
ax1.plot(dates, rolling_avg, 'r-', linewidth=3, label='7-day Avg')
ax1.fill_between(dates, temperature.min(), temperature, 
                 where=(temperature > 25), color='red', alpha=0.2,
                 label='Hot days (>25°C)')
ax1.axhline(y=25, color='darkred', linestyle='--', alpha=0.5)
ax1.set_ylabel('Temperature (°C)')
ax1.set_title('Weather Analysis - Temperature')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# Plot 2: Rainfall as bars
ax2 = axes[1]
bars = ax2.bar(dates, rainfall, color='blue', alpha=0.7, 
               width=0.8, edgecolor='darkblue', linewidth=0.5)
ax2.set_ylabel('Rainfall (mm)')
ax2.set_title('Rainfall')
ax2.grid(True, alpha=0.3, axis='y')

# Highlight heavy rainfall days
for i, (date, rain) in enumerate(zip(dates, rainfall)):
    if rain > 15:
        bars[i].set_color('darkblue')
        bars[i].set_alpha(1)

# Plot 3: Humidity with fill between
ax3 = axes[2]
ax3.plot(dates, humidity, 'g-', linewidth=2, label='Humidity')
ax3.fill_between(dates, humidity, 60, where=(humidity > 60), 
                 color='green', alpha=0.3, label='High humidity')
ax3.fill_between(dates, humidity, 60, where=(humidity <= 60), 
                 color='lightgreen', alpha=0.3, label='Normal humidity')
ax3.axhline(y=60, color='darkgreen', linestyle='--', alpha=0.5)
ax3.set_ylabel('Humidity (%)')
ax3.set_xlabel('Date')
ax3.set_title('Humidity')
ax3.legend(loc='upper left')
ax3.grid(True, alpha=0.3)

# Format x-axis
plt.xticks(rotation=45)
fig.autofmt_xdate()

# Add overall statistics
stats_text = f"""
Statistics (90 days):
• Avg Temperature: {np.mean(temperature):.1f}°C
• Max Temperature: {np.max(temperature):.1f}°C
• Total Rainfall: {np.sum(rainfall):.1f}mm
• Rainy days (>10mm): {np.sum(rainfall > 10)} days
• Avg Humidity: {np.mean(humidity):.1f}%
"""
fig.text(0.02, 0.02, stats_text, fontsize=10, 
         verticalalignment='bottom',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.suptitle('Weather Station Data Analysis (Jan-Mar 2024)', 
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0.05, 1, 0.97])
plt.show()
```

This comprehensive guide provides both a quick reference for common functions and detailed examples for practical implementation. The Table of Contents allows easy navigation between sections.