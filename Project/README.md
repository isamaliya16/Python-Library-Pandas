# 🧠 Pandas Analyzer & Data Visualization Tool

## 📋 Project Overview
This project — **Sales Data Analyzer & Visualization Tool** — is a Python-based data analysis program built using **Pandas**, **NumPy**, **Matplotlib**, and **Seaborn**.  
It helps users **analyze, clean, summarize, and visualize** sales data efficiently through a **menu-driven console interface**.

Users can:
- Load and explore sales datasets  
- Handle missing values  
- Perform mathematical and statistical operations  
- Generate pivot tables  
- Perform advanced Pandas operations (GroupBy, Transform, Reindexing, etc.)  
- Create beautiful visualizations including bar, line, pie, and heatmap charts  

---

## 🧰 Technologies Used
- **Python 3.x**
- **Pandas** – for data manipulation  
- **NumPy** – for numerical operations  
- **Matplotlib** – for static plotting  
- **Seaborn** – for advanced statistical visualizations  

---

## ⚙️ Features

### 🗂️ Data Handling
- Load CSV datasets easily  
- Explore data (head, tail, info, column types)  
- Handle missing values (view, fill, drop, replace)

### 🧮 Mathematical Operations
- Perform sum, mean, min, and max on numeric columns  

### 🔍 Search, Sort, and Filter
- Search products by name  
- Sort sales data  
- Filter by region  

### 📊 Aggregation & Statistics
- Display total sales and average profit  
- Generate descriptive statistics summary  

### 🔁 Pivot Tables
- Create pivot tables for `Sales` grouped by `Region` and `Product`

### 🚀 Advanced Operations
- Create pivot tables dynamically  
- Reindex and rename columns  
- Perform GroupBy and Transform to add new analytical columns  

### 🎨 Data Visualization
Generate 6 types of charts:
1. Bar Plot (Sales by Product)  
2. Line Plot (Sales over Years)  
3. Scatter Plot (Custom columns)  
4. Pie Chart (Sales by Region)  
5. Histogram (Sales distribution)  
6. Heatmap (Correlation between numeric fields)

### 💾 Save Visualization
Save the generated charts as image files (`.png`, `.jpg`, etc.)

---

## 📁 Project Structure

```
SalesDataAnalyzer/
│
├── sales_data.csv               # Sample dataset (user-provided)
├── main.py                      # Main Python script (this code)
├── README.md                    # Project documentation
└── output_charts/               # Folder for saved visualizations (optional)
```

---

## ▶️ How to Run

### Step 1: Install Required Libraries
Open your terminal or command prompt and run:
```bash
pip install pandas numpy matplotlib seaborn
```

### Step 2: Prepare Your Dataset
Ensure you have a `sales_data.csv` file containing fields like:
```
Product, Region, Sales, Profit, Year
```

### Step 3: Run the Program
Execute the script:
```bash
python main.py
```

### Step 4: Follow the Menu
You’ll see a menu like:
```
========== Data Analysis & Visualization Program ==========
1. Load Dataset
2. Explore Data
3. Handle Missing Data
4. Perform Mathematical Operations
5. Search/Sort/Filter
6. Aggregation & Statistics
7. Create Pivot Table
8. Data Visualization
9. Advanced Operations
10. Save Visualization
11. Exit
```

Enter the number of the operation you want to perform.

---

## 🧠 Example Use Case

1. Load the dataset (`sales_data.csv`)  
2. Explore first few rows  
3. Clean missing data  
4. View total sales and average profit  
5. Generate a bar chart of **Sales by Product**  
6. Save chart as `sales_chart.png`

---

## 📈 Sample Output

**Bar Chart Example:**
```
| Product | Sales |
|----------|-------|
| A        | 35000 |
| B        | 29000 |
| C        | 41000 |
```
*(Displays as a bar graph using Matplotlib/Seaborn)*

**Heatmap Example:**
Displays correlations between `Sales`, `Profit`, and `Quantity` columns.

---

## 🚧 Future Enhancements
- Add GUI using **Tkinter** or **Streamlit**  
- Export summarized reports to Excel or PDF  
- Add machine learning prediction for future sales  

---

## 🧑‍💻 Author
**Developed by:** *Ayush Isamaliya*  
**Language:** Python  
**Version:** 1.0  

---

## 📜 License
This project is open-source and free to use for educational purposes.
