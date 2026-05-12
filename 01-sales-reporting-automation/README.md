# Sales Reporting Automation

## 📊 Project Overview

This project automates the consolidation of monthly sales data from multiple CSV files and generates key performance indicators (KPIs) for business analysis.

**Problem Solved:**
- Manual consolidation of 3 months' sales data took **2-3 hours**
- Error-prone when done manually in Excel
- No consistent KPI calculations

**Solution:**
- Automated Python script that reads multiple CSV files
- Calculates KPIs automatically (Revenue, MoM Growth, Category Analysis)
- Generates both CSV and Excel reports in seconds

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **Libraries:** Pandas, NumPy, OpenPyXL
- **Data Format:** CSV input → CSV/Excel output

---

## 📂 Project Structure
01-sales-reporting-automation/
├── sales_automation.py          # Main script
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── sample_data/                 # Input folder
│   ├── january_sales.csv
│   ├── february_sales.csv
│   └── march_sales.csv
└── sales_report.csv            # Output (generated)


---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Prepare Input Data
Place monthly CSV files in `sample_data/` folder with columns:
- `product_name`
- `category`
- `quantity_sold`
- `unit_price`
- `date`

### 3. Run the Script
```bash
python sales_automation.py
```

### 4. Output Files
- `sales_report.csv` - Summary by month
- `sales_report.xlsx` - Multi-sheet analysis

---

## 📈 KPIs Calculated

1. **Monthly Revenue** - Total sales per month
2. **Month-over-Month Growth** - % change between months
3. **Revenue by Category** - Sales breakdown by product category
4. **Top 5 Products** - Best-performing products
5. **Overall Statistics** - Total revenue, units, average order value

---

## 📊 Sample Output
MONTHLY REVENUE:
2025-01    $23,620.00
2025-02    $28,320.00
2025-03    $33,780.00
MONTH-OVER-MONTH GROWTH:
2025-02:  +19.94%
2025-03:  +19.21%
REVENUE BY CATEGORY:
Electronics: $51,380.00
Furniture:   $32,340.00

---

## 💡 Key Learnings

- **Data Consolidation:** Pandas `concat()` for combining multiple files
- **Time Series Analysis:** Grouping by time periods (month) for trend analysis
- **Reporting:** Automated Excel/CSV generation saves manual work
- **Error Reduction:** Eliminates human error in manual data entry

## 📧 Author

**Idris Fatih Acar**  
[LinkedIn](https://linkedin.com/in/idrisfatihacar/) | [GitHub](https://github.com/ifacar/)